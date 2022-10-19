import sys
import hou
from WPN_GENERATOR_PY import WPN_Enums
from WPN_GENERATOR_PY import WPN_Utils

sys.path.append(r"E:\Users\Jason\Documents\houdini18.5\python3.7libs\WPN_GENERATOR_PY\venv\Lib\site-packages")

from WPN_GENERATOR_PY import GunPart
from WPN_GENERATOR_PY import gunPartParmTemplates as GPpT

import fnmatch
from psd_tools import PSDImage

GEO_CONTAINER = "GEO_CONTAINER"

debug = False

gunPartList = []   #Stores instances of generated gunparts


def rebuild(this_node):
    geoContainer = this_node.node(GEO_CONTAINER)

    print("---------------------Removing all Spare Parms------------------------")
    this_node.removeSpareParms()
    print("---------------------Cleaning Geo Container--------------------------")
    # Cleans Geo Container
    for child in geoContainer.children():
        child.destroy()

    print("---------------------Getting Valid PSD Layer Names-------------------")
    validPSDLayerNames, layerNameCountDict = getValidPSDLayerNames(this_node)
    print("---------------------Building Parm Templates-------------------------")
    buildParmTemplates(this_node, validPSDLayerNames)
    print("---------------------Setting MultiParmNums---------------------------")
    SetMultiParmNums(layerNameCountDict, this_node)
    print("---------------------Generating Gun Parts----------------------------")
    genGunPartNodes(geoContainer, this_node)
    print("---------------------Setting Layer Names-----------------------------")
    SetValidLayerName(this_node, validPSDLayerNames)
    print("---------------------Setting Gun Part Shape--------------------------")
    for gunpart in gunPartList:
        gunpart.setValidLayerName()
        gunpart.setShapeType()



def SetValidLayerName(this_node, validPSDLayerNames):
    for validLayerName in validPSDLayerNames:
        noShapeName = WPN_Utils.getNoShapeSuffixName(validLayerName)
        #print(noShapeName + "_layer_name1")
        try:
            this_node.parm(noShapeName + "_layer_name1").set(validLayerName)
        except:
            print("ERROR: Setting " + noShapeName + "_layer_name1 failed, Check LayerName Conventions; [gunPart]#_[shapeType]")




def genGunPartNodes(geoContainer, this_node):
    # Gen Gunpart Nodes as needed
    gpTypes = WPN_Enums.GPTypes
    for gpType in gpTypes:
        multiparm = this_node.parm("numOf_" + gpType.name)
        if multiparm != None:
            #print(gpType.name + " multiparm found :" + multiparm.name())
            #print("MultiParm Length :" + str(multiparm.eval()))
            multiparmLen = multiparm.eval()
            for i in range(multiparmLen):
                gunPartNodeName = gpType.name
                gunPart = GunPart.gunpart(gunPartNodeName, gpType, i)
                gunPartNode = gunPart.createGunpartNode()
                gunPartList.append(gunPart)
                #print(gunPartNode)
                gunPartNode.parm("file").set(WPN_Utils.linkExpressionParentParmToParm("file", True, True))
                linkParms(this_node, gunPartNode, gunPart.parmPrefix)

    geoContainer.layoutChildren()
    for child in geoContainer.children():
        child.layoutChildren()





def SetMultiParmNums(layerNameCountDict, this_node):
    for key, value in layerNameCountDict.items():
        multiParmName = "numOf_" + key
        print("Setting " + multiParmName + " to " + str(value))
        this_node.parm(multiParmName).set(value)


def buildParmTemplates(this_node, validPSDLayerNames):
    for validLayerName in validPSDLayerNames:
        noShapeName = WPN_Utils.getCleanName(validLayerName)
        #print(noShapeName)
        folderName = "numOf_" + noShapeName
        #print("ValidLayerName is:" + validLayerName)
        parmFolderTemplate = GPpT.genGunpartParmTemplates(noShapeName, WPN_Enums.GPTypesNiceName[WPN_Enums.GPTypes[noShapeName]], validLayerName)
        # print(this_node.parms())
        if len(this_node.globParms(folderName)) < 1:
            this_node.addSpareParmTuple(parmFolderTemplate)
        else:
            print(folderName + " already exists, Skipping")


        # print(GPTypes[nonDigitName])
        #print(GPTypesNiceName[GPTypes[nonDigitName]])


def getValidPSDLayerNames(this_node):
    # Gets list of valid layers based on enum and not empty layers.
    filepath = this_node.parm("file").eval()
    psd = PSDImage.open(filepath)
    gpTypesNames = [gpType.name for gpType in WPN_Enums.GPTypes]
    layerNames = []
    validLayerNames = []
    # print(gpTypesNames)

    for i, layer in enumerate(psd):
        #print(layer.name)
        #print(layer.name.split(' '))
        if layer.size != (0, 0):
            if len(layer.name.split(' ')) > 1:
                print(layer.name + " removed because it contained spaces")
            else:
                layerNames.append(layer.name)

        else:
            print(layer.name + " removed because layer empty")

    if debug:
        print("DEBUG: gpTypeNames ")
        print(gpTypesNames)
    layerNameCountDict = {}
    for gpTypesName in gpTypesNames:

        layerNameCount = 0
        matchList = fnmatch.filter(layerNames, gpTypesName + "*")
        if len(matchList) != 0:
            layerNameCount = len(matchList)
            if debug:
                print("DEBUG: " + gpTypesName +" MatchList:")
                print(matchList)
                #print("LayerNameCount: " +layerNameCount)
            validLayerNames += fnmatch.filter(layerNames, gpTypesName + "*")
        if layerNameCount != 0:
            layerNameCountDict[gpTypesName] = layerNameCount
    for validLayerName in validLayerNames:
        print("Found " + validLayerName)

    #print(layerNameCountDict)
    #print(list(set(validLayerNames)))
    return list(set(validLayerNames)), layerNameCountDict



def linkParms(this_node, gunPartNode, gunPartPrefix):
    gunPartParms = this_node.globParms(gunPartPrefix + "_*")
    unprefixedParmsName = [parm.name().replace(gunPartPrefix + "_", "") for parm in gunPartParms]
    for i, unprefixedParmName in enumerate(unprefixedParmsName):
        parmSource = gunPartParms[i]
        parmTarget = gunPartNode.parm(unprefixedParmName)
        #print(parmTarget.parmTemplate().type())
        if parmTarget.parmTemplate().type() == hou.parmTemplateType.String:
            #print(parmTarget.parmTemplate().type)
            parmTarget.set(WPN_Utils.linkExpressionParentParmToParm(parmSource.name(), True, True))
        elif "crveShpProfile" in parmTarget.name():
            pass
        else:
            parmTarget.setExpression(WPN_Utils.linkExpressionParentParmToParm(parmSource.name()))
    # print(gunPartParmsNameOnly)
