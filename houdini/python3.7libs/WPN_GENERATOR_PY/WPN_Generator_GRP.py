import sys
import hou
import pprint
import os
import itertools
from WPN_GENERATOR_PY import WPN_Enums
from WPN_GENERATOR_PY import WPN_Utils
sys.path.append(r"E:\Users\Jason\Documents\houdini18.5\python3.7libs\WPN_GENERATOR_PY\venv\Lib\site-packages")
from WPN_GENERATOR_PY import PSDAssetClasses as psdAsset
from WPN_GENERATOR_PY import WPNAssetClasses as wpnAsset
from WPN_GENERATOR_PY import gunPartParmTemplatesGRP as GPpT

import fnmatch
from psd_tools import PSDImage
from psd_tools.constants import Resource


#GLOBALS
GEO_CONTAINER = "GEO_CONTAINER"
debug = False


gunPartList = []   #Stores instances of generated gunparts
parentChildDict = {} #Stores dict of <Group> : <Layer>/<Group> Children[]
gunPartContainerList = [] #Stores instances of generated psdAsset containers

psdFilepath = ""
psd = None #stores PSD
savedPSD = None #Stores the saved PSD
groupParentDict = {} #Stores dict of <Group> : str parentName



def rebuild(this_node):
    global savedPSD
    print("Build Grp")
    geoContainer = this_node.node(GEO_CONTAINER)

    print("---------------------Removing all Spare Parms------------------------")
    this_node.removeSpareParms()
    print("---------------------Cleaning Geo Container--------------------------")
    # Cleans Geo Container
    for child in geoContainer.children():
        child.destroy()



    if debug:
        print("---------------------Get Parent-Child Dict---------------------------")
    PCDict = getPSDGrpAndChildren(this_node)
    print("---------------------Saving Renamed PSDs-----------------------------")
    savedPSDPath = renameChildLayersAndSave(PCDict)
    savedPSD = PSDImage.open(savedPSDPath)
    generator = psdAsset.Generator(savedPSD)
    generator.genContainerObjs(wpnAsset.GunPartContainer)

    for ContainerObj in generator.AllContainerObjs:
        # print("Gunpartcontainer name:" + gunPartContainer.name)
        # pprint.pprint(gunPartContainer.childAssetObjs)
        ContainerObj.createContainer()

    for childAsset in generator.AllChildAssetsObjs:
        childAsset.createNode()
    for childAsset in generator.AllChildAssetsObjs:
        if debug:
            print(childAsset.name + "_" + ContainerObj.name)
        try:
        #     childAsset.getCutoutObjs()
        #     childAsset.linkCutoutObj()
        #     childAsset.triggerCutoutObjLink()
        #     childAsset.setCutoutPattern()
            childAsset.setParentObj()
        except:
            pass

    for childAsset in generator.AllChildAssetsObjs:
        childAsset.appendSelfToParent()


    for childAsset in generator.AllChildAssetsObjs:
        childAsset.setChildrenFactorParmNames()
        #childAsset.debugPrintParentChildObjs()
        childAsset.linkFactorParmMods()

    generator.layoutGeoContainer()


    # for childAsset in generator.AllChildAssetsObjs:
    #     childAsset.linkFactorParmMods()
    # if debug:
    #     print("---------------------Get Group:Parent Dict---------------------------")
    # groupParentDict = getGroupParentDict()
    # print("---------------------Building Parm Templates-------------------------")
    # BuildParmTemplateHeirarchy(groupParentDict, this_node)
    # print("---------------------Generating Gun Parts----------------------------")
    # genGunPartNodes(geoContainer, this_node)



def BuildParmTemplateHeirarchy(groupParentDict, this_node):
    #Build Parent Parm Templates
    for parent, children in parentChildDict.items():
        containingFolder = ()
        parmNames = [parm.name() for parm in this_node.parms()]
        if parent.name not in parmNames:
            if debug:
                print("Debug: No Parent! Making Parent!")
            parentParmTemplate = buildParmTemplates(this_node, parent.name, WPN_Enums.parmType.GROUP)
        else:
            i = parmNames.index(parent.name)
            parentParmTemplate = this_node.parms()[i].parmTemplate()
            if debug:
                print("Parent found: " + parentParmTemplate.name())

        #Build Child Templates
        for child in children:
            if child.is_group() != True:
                if fnmatch.fnmatch(child.name, "*SIDE*"):
                    parentParmTemplate.addParmTemplate(buildParmTemplates(this_node, child.name, WPN_Enums.parmType.GUNPART))
                elif fnmatch.fnmatch(child.name, "*CUTOUT*"):
                    parentParmTemplate.addParmTemplate(buildParmTemplates(this_node, child.name, WPN_Enums.parmType.CUTOUT))
                if debug:
                    print("Parenting " + child.name + " Parms into " + parent.name + " ParmFolder")
        if parentParmTemplate != None:
            if parent.is_group:
                containingFolder = groupParentDict[parent]
                if len(containingFolder) != 0:
                    parentFolder = containingFolder[-1] + " ParmFolder"
                else:
                    parentFolder = "Root"
                print("Parenting " + parent.name + " ParmFolder into " + parentFolder)

            this_node.addSpareParmTuple(parentParmTemplate, in_folder=containingFolder)



def removeNone(list):
    strList = []
    if list == None or isinstance(list, str):
        #print(list + " is a string")
        return strList
    else:
        for sublist in list:
            #print(list)
            if isinstance(sublist, str):
                #print(sublist)
                strList.append(sublist)
            else:
                strList.append(removeNone(sublist))
    return strList

def flatten(A):
    rt = []
    for i in A:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt

def getGroupParentDict():
    for parent, child in parentChildDict.items():
        parentList = getParentOfLayer(parent)
        cleanParentlist = removeNone(parentList)
        flatParentList = flatten(cleanParentlist)
        flatParentList.reverse()
        pop = flatParentList.pop(0)
        groupParentDict[parent] = tuple(flatParentList)
        if len(flatParentList) != 0:
            printParentList = ", ".join(flatParentList) + " ParmFolders" #Only for printing
        else:
            printParentList = "None" #Only for printing
        if debug:
            print(parent.name + " ParmFolder's Ancestors are: " + printParentList)
    if debug:
        print("DEBUG: Group Parent Dict  ( <Group> : Tuple of all Parents.name ) ")
        pprint.pprint(groupParentDict)
    return groupParentDict

def getParentOfLayer(layer):
    #print(layer.name)
    if layer.parent:
        return [layer.parent.name] + [getParentOfLayer(layer.parent)]



def SetValidLayerName(this_node, validPSDLayerNames):
    for validLayerName in validPSDLayerNames:
        noShapeName = WPN_Utils.getNoShapeSuffixName(validLayerName)
        #print(noShapeName + "_layer_name1")
        try:
            this_node.parm(noShapeName + "_layer_name1").set(validLayerName)
        except:
            print("ERROR: Setting " + noShapeName + "_layer_name1 failed, Check LayerName Conventions; [psdAsset]#_[shapeType]")


def renameChildLayersAndSave(PCDict):
    (dirname, filename) = os.path.split(psdFilepath)
    (filename, ext) = os.path.splitext(filename)
    psdPath = dirname + "/" + filename + "_renamed" + ext

    for parent, children in PCDict.items():
        parent.visible = True
        newChildNameList = []
        for child in children:
            #print("child:" + child.name +  ".parent is: " + child.parent.name)
            newChildNameList.append(child.parent.name + "_" + child.name)
            # parentList = getParentOfLayer(child)
            # print(parentList)
            # cleanParentlist = removeNone(parentList)
            # flatParentList = flatten(cleanParentlist)
            # flatParentList.reverse()
            # pop = flatParentList.pop(0)
            # splitParentList = [ parentName.split("_") for parentName in flatParentList]
            # #print(splitParentList)
            # flatSplitParentlist = list(set(flatten(splitParentList)))
            # #print(flatSplitParentlist)
            # newChildNameList.append("_".join(flatSplitParentlist) + "_" + child.name)
        """Rename group first"""
        for i, child in enumerate(children):
            child.visible = True
            if child.is_group():
                group = child
                ogGroupName = group.name
                newGroupName = newChildNameList[i]
                group.name = newGroupName
                if debug:
                    print("DEBUG: Renaming " + ogGroupName + " to " + newGroupName)
                for childLayer in group:
                    if not childLayer.is_group():
                        ogChildName = childLayer.name
                        newChildName = newGroupName + "_" + ogChildName
                        childLayer.name = newChildName
                        if debug:
                            print("DEBUG: Renaming " + ogChildName + " to " + newChildName)
            elif child.parent.parent.name == "Root":
                ogChildName = child.name
                newChildName = newChildNameList[i]
                child.name = newChildName

    psd.save(psdPath)
    print("Saved Renamed PSD into: " + psdPath)
    return psdPath



def genGunPartNodes(geoContainer, this_node):
    # Gen psdAsset Nodes as needed
    for parent, children in parentChildDict.items():
        if parent.parent.name == "Root":
            gunPartContainerObj = psdAsset.Container(parent)
            gunPartContainerNode = gunPartContainerObj.createContainer()
            gunPartContainerObj.populateChildAssetsOfNodeType(wpnAsset.CutoutAsset, layerNames = ["CUTOUT"])
            gunPartContainerObj.populateChildAssetsOfNodeType(wpnAsset.GunPartAsset, layerNames = ["SIDE"])
            gunPartContainerObj.populateContainerWithChildAssets()
            gunPartContainerList.append(gunPartContainerObj)
        #gunPartNode = psdAsset.createGunpartNode()
        #gunPartList.append(psdAsset)
        #print(gunPartNode)
        #gunPartNode.parm("file").set(WPN_Utils.linkExpressionParentParmToParm("file", True, True))
        #linkParms(this_node, gunPartNode, psdAsset.parmPrefix)

    # for gpType in gpTypes:
    #     multiparm = this_node.parm("numOf_" + gpType.name)
    #     if multiparm != None:
    #         #print(gpType.name + " multiparm found :" + multiparm.name())
    #         #print("MultiParm Length :" + str(multiparm.eval()))
    #         multiparmLen = multiparm.eval()
    #         for i in range(multiparmLen):
    #             gunPartNodeName = gpType.name
    #             psdAsset = psdAsset.psdAsset(gunPartNodeName, gpType, i)
    #             gunPartNode = psdAsset.createGunpartNode()
    #             gunPartList.append(psdAsset)
    #             #print(gunPartNode)
    #             gunPartNode.parm("file").set(WPN_Utils.linkExpressionParentParmToParm("file", True, True))
    #             linkParms(this_node, gunPartNode, psdAsset.parmPrefix)

    geoContainer.layoutChildren()
    for child in geoContainer.children():
        child.layoutChildren()





def SetMultiParmNums(layerNameCountDict, this_node):
    for key, value in layerNameCountDict.items():
        multiParmName = "numOf_" + key
        print("Setting " + multiParmName + " to " + str(value))
        this_node.parm(multiParmName).set(value)


def buildParmTemplates(this_node, layerName, parmType):
    if parmType == 0:
        parmFolderTemplate = GPpT.genGunpartParentTemplates(layerName)
    elif parmType == 1:
        parmFolderTemplate = GPpT.genGunpartParmTemplates(layerName)
    elif parmType == 2:
        parmFolderTemplate = GPpT.genCutoutParmTemplates(layerName)

    # print(this_node.parms())
    return parmFolderTemplate



def createAssetObjs(this_node, group):
    #print("Enter createAssetObjs")
    for layer in group.descendants():
        if layer.is_group():
            group = layer
            groupName = group.name
            #print(layer.name + " is group! Creating Container!")
            gunPartContainer = psdAsset.Container(group)
            gunPartContainerList.append(gunPartContainer)

    for gunPartContainer in gunPartContainerList:
        for childlayer in gunPartContainer.PSDGroup:
            if not childlayer.is_group():
                childlayerName = childlayer.name.split("_")[-1]
                #print("childlayerName is " + childlayerName)
                childAsset = None
                if childlayerName == "SIDE":
                    #print(childlayer.name + " is SIDE! Creating GunPartAsset")
                    childAsset = wpnAsset.GunPartAsset(childlayer, gunPartContainer)
                elif childlayerName == "CUTOUT":
                    #print(childlayer.name + " is CUTOUT! Creating CutoutAsset")
                    childAsset = wpnAsset.CutoutAsset(childlayer, gunPartContainer)
                if childAsset != None:
                    gunPartContainer.childAssetObjs.append(childAsset)
                else:
                    pass
                    #print(layer.name + ": Not a BaseGeo ChildLayer!")

            # else:
            #     print(childlayer.name  + " is group! Creating Asset Objs!")
            #     createAssetObjs(this_node, childlayer)


    #     getChildOfLayer(layer)
    # if debug:
    #     print("DEBUG: ParentChildDict ( Parent <Group> : Child <Group>/<Layer> )")
    #     pprint.pprint(parentChildDict)


def getPSDGrpAndChildren(this_node):
    # Gets list of Grps
    global psd
    global psdFilepath
    psdFilepath = this_node.parm("file").eval()
    psd = PSDImage.open(psdFilepath)
    for i, layer in enumerate(psd):
        getChildOfLayer(layer)
    if debug:
        print("DEBUG: ParentChildDict ( Parent <Group> : Child <Group>/<Layer> )")
        pprint.pprint(parentChildDict)


    return parentChildDict


def getChildOfLayer(layer):
    if layer.is_group():
        if debug:
            print( "DEBUG: " + layer.name + " is Group")
        for childLayer in layer:
            parentName = layer.name
            if debug == True:
                print("DEBUG: Child of " + parentName + " is " + childLayer.name)
            getChildOfLayer(childLayer)
            if parentChildDict.get(layer) == None: #if non-existent key
                parentChildDict[layer] = [childLayer] #make new parent:Child
            else:
                parentChildDict[layer].append(childLayer) #append to child list if not group
        #parentChildDict[layer].append(layer.parent.name)







def getValidPSDLayerNames(this_node):
    global savedPSD
    # Gets list of valid layers based on enum and not empty layers.
    gpTypesNames = [gpType.name for gpType in WPN_Enums.GPTypes]
    layerNames = []
    validLayerNames = []
    # print(gpTypesNames)

    for i, layer in enumerate(savedPSD):
        for child in layer.descendants():
            #print(child.name)
        #print(layer.name.split(' '))
        #if layer.size != (0, 0):
            #if len(layer.name.split(' ')) > 1:
                #print(layer.name + " removed because it contained spaces")
            #else:
                #layerNames.append(layer.name)
        #else:
            #print(layer.name + " removed because layer empty")
            layerNames.append(child.name)

    if debug:
        print("DEBUG: LayerNames")
        print(layerNames)
        #print("DEBUG: gpTypeNames ")
        #print(gpTypesNames)
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
