from WPN_GENERATOR_PY import WPN_Utils
from WPN_GENERATOR_PY import PSDAssetClasses as psdAsset
from WPN_GENERATOR_PY import WPNAssetClasses as wpnAsset

import hou
import pprint
import os

from psd_tools import PSDImage

""" ------------------GLOBALS------------------------ """
GEO_CONTAINER = "GEO_CONTAINER"

gunPartList = []   #Stores instances of generated gunparts
parentChildDict = {} #Stores dict of <Group> : <Layer>/<Group> Children[]
gunPartContainerList = [] #Stores instances of generated psdAsset containers

psdFilepath = ""
psd = None #stores PSD
savedPSD = None #Stores the saved PSD
groupParentDict = {} #Stores dict of <Group> : str parentName

debug = False
""" ------------------GLOBALS------------------------ """


def rebuild(this_node):
    global savedPSD
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
    print("---------------------Creating Containers-----------------------------")
    for ContainerObj in generator.AllContainerObjs:
        ContainerObj.createContainer()
    print("---------------------Creating Assets-----------------------------")
    for childAsset in generator.AllChildAssetsObjs:
        childAsset.createNode()
    for childAsset in generator.AllChildAssetsObjs:
        if debug:
            print(childAsset.name + "_" + ContainerObj.name)
        try:
            childAsset.setParentObj()
        except:
            pass

    for childAsset in generator.AllChildAssetsObjs:
        childAsset.appendSelfToParent()


    for childAsset in generator.AllChildAssetsObjs:
        childAsset.setChildrenFactorParmNames()
        childAsset.linkFactorParmMods()

    generator.layoutGeoContainer()


def removeNone(list):
    strList = []
    if list == None or isinstance(list, str):
        return strList
    else:
        for sublist in list:
            if isinstance(sublist, str):
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
    if layer.parent:
        return [layer.parent.name] + [getParentOfLayer(layer.parent)]

def SetValidLayerName(this_node, validPSDLayerNames):
    for validLayerName in validPSDLayerNames:
        noShapeName = WPN_Utils.getNoShapeSuffixName(validLayerName)
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
            newChildNameList.append(child.parent.name + "_" + child.name)
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
        

    geoContainer.layoutChildren()
    for child in geoContainer.children():
        child.layoutChildren()

def SetMultiParmNums(layerNameCountDict, this_node):
    for key, value in layerNameCountDict.items():
        multiParmName = "numOf_" + key
        print("Setting " + multiParmName + " to " + str(value))
        this_node.parm(multiParmName).set(value)

def createAssetObjs(this_node, group):
    for layer in group.descendants():
        if layer.is_group():
            group = layer
            groupName = group.name
            gunPartContainer = psdAsset.Container(group)
            gunPartContainerList.append(gunPartContainer)

    for gunPartContainer in gunPartContainerList:
        for childlayer in gunPartContainer.PSDGroup:
            if not childlayer.is_group():
                childlayerName = childlayer.name.split("_")[-1]
                childAsset = None
                if childlayerName == "SIDE":
                    childAsset = wpnAsset.GunPartAsset(childlayer, gunPartContainer)
                elif childlayerName == "CUTOUT":
                    childAsset = wpnAsset.CutoutAsset(childlayer, gunPartContainer)
                if childAsset != None:
                    gunPartContainer.childAssetObjs.append(childAsset)
                else:
                    pass



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


def linkParms(this_node, gunPartNode, gunPartPrefix):
    gunPartParms = this_node.globParms(gunPartPrefix + "_*")
    unprefixedParmsName = [parm.name().replace(gunPartPrefix + "_", "") for parm in gunPartParms]
    for i, unprefixedParmName in enumerate(unprefixedParmsName):
        parmSource = gunPartParms[i]
        parmTarget = gunPartNode.parm(unprefixedParmName)
        if parmTarget.parmTemplate().type() == hou.parmTemplateType.String:
            parmTarget.set(WPN_Utils.linkExpressionParentParmToParm(parmSource.name(), True, True))
        elif "crveShpProfile" in parmTarget.name():
            pass
        else:
            parmTarget.setExpression(WPN_Utils.linkExpressionParentParmToParm(parmSource.name()))
