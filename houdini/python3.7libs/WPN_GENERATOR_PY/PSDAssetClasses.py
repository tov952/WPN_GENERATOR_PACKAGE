from WPN_GENERATOR_PY import WPN_Utils

import hou
import fnmatch
import pprint
import pathlib
import imp



debug = False

class Generator(object):

    def __init__(self, PSD):
        self.node = hou.pwd()
        self.psd = PSD
        self.AllChildAssetsObjs = []
        self.AllContainerObjs = []
        self.geoContainer =  self.setupGeoContainer()


    def genContainerObjs(self, containerClass):
        if debug:
            print("Generate Container Objs")
        container = None
        for layer in self.psd.descendants():
            if layer.is_group():
                group = layer
                groupName = group.name
                #print(layer.name + " is group! Creating Container!")
                container = containerClass(group, self)
                self.AllContainerObjs.append(container)
        self.genContainerAssetObjs()

    def setupGeoContainer(self):
        geoContainer = self.node.node("GEO_CONTAINER")
        geoContainer.createNode("null", "Root")
        return geoContainer

    def genContainerAssetObjs(self):
        for container in self.AllContainerObjs:
            container.createAssetObjs()
            self.AllChildAssetsObjs += container.childAssetObjs
        self.postCreation()

    def layoutGeoContainer(self):
        self.geoContainer.layoutChildren()

    def postCreation(self):
        self.AllChildAssetsNames = [childAsset.name for childAsset in self.AllChildAssetsObjs]



class Container(object):

    def __init__(self,psdGroup, generator):

        self.generator = generator
        self.PSDGroup = psdGroup
        self.name = self.PSDGroup.name
        self.subnetNodeName = self.PSDGroup.name +"_CONTAINER"
        self.childAssetObjs = []
        self.subnetContainerNode = None
        self.parent = self.PSDGroup.parent
        self.parentContainerNode = None


    def populateContainerWithChildAssets(self):
        for childAsset in self.childAssetObjs:
            childAsset.createNode()

    """Creates childAssetObjs Flat"""
    def populateChildAssetsOfNodeType(self, ChildAssetClass,layerNames = []):
        if debug:
            print("DEBUG: Creating " + ChildAssetClass.__name__ + " Objs of " + self.name)
        PSDGrpDesc = []
        layersToChild = []
        for desc in self.PSDGroup.descendants():
            PSDGrpDesc.append(desc)

        if len(layerNames) != 0:
            descendantLayerNames = [childLayer.name for childLayer in PSDGrpDesc]
            for layerName in layerNames:
                layerNamePattern = "*_"+layerName+"*"
                for i, layerName in enumerate(descendantLayerNames):
                    if fnmatch.fnmatch(layerName, layerNamePattern):
                        layersToChild.append(PSDGrpDesc[i])
        else:
            layersToChild = PSDGrpDesc



        for childlayer in layersToChild:
            childGunPart = ChildAssetClass(childlayer, self)
            self.childAssetObjs.append(childGunPart)
        if debug:
            print("childAssetObjs of "+ self.name)
            pprint.pprint(self.childAssetObjs)

    def setParentGRPContainerInput(self):
        if self.parentContainerNode != None:
            self.subnetContainerNode.setInput(0, self.parentContainerNode)
        else:
            self.subnetContainerNode.setInput(0,self.generator.geoContainer.node("Root"))

    def getParentContainerNode(self, geoCon):
        if self.parent.name != "Root":
            self.parentContainerNode = geoCon.node(self.parent.name + "_CONTAINER")
            print("Found " + self.parent.name + "_CONTAINER for " + self.name)


    def createContainer(self):
        geoContainer = self.generator.geoContainer
        self.subnetContainerNode = geoContainer.node(self.subnetNodeName)
        if self.subnetContainerNode == None:
            self.subnetContainerNode = geoContainer.createNode("geo", self.subnetNodeName)
            self.subnetContainerNode.moveToGoodPosition()
        print("Created: " + self.subnetNodeName)
        self.getParentContainerNode(geoContainer)
        self.setParentGRPContainerInput()
        return self.subnetContainerNode

    def createAssetObjs(self):
        if debug:
            print("DEBUG: " + self.name + " creating Child Asset Objs")
        for childlayer in self.PSDGroup:
            if not childlayer.is_group():
                childlayerName = childlayer.name.split("_")[-1]
                childAsset = self.childAssetDefinition(childlayerName, childlayer)
                if childAsset != None:
                    self.childAssetObjs.append(childAsset)
                else:
                    pass


    def childAssetDefinition(self, childlayerName, childlayer):
        print(" No Child Asset Definition Logic!")
        return None

"""TODO MAKE INTO ABSTRACT CLASS"""
class ChildAsset(object):

    def __init__(self, layer, containerObj):

        self.layer = layer
        self.name = self.layer.name
        self.layerPrefix = "_".join(self.name.split("_")[0:-1])
        self.layerSuffix = self.name.split("_")[-1]
        self.containerObj = containerObj
        self.parentLayer = self.layer.parent
        self.parentObj = None
        self.childObjs = []


        self.nodeType = ""
        self.node = None
        self.parentContainerNode = self.containerObj.subnetContainerNode
        self.parmSources = []
        self.parmTargets = None
        self.parentNode = hou.pwd()
        self.parmSourceTargetDict = {}
        self.parmLayerDict = {}
        self.PTG = None
        self.flatParmMods = {}  #Parms to add modify (add)
        self.parmModFactor = {} #Parms to mult modify (mult)
        self.factorParmNames = {}
        self.flatParmTarget = {}
        self.masterGroup = self.setMasterGroup()
        self.directChildLayers = self.setDirectChildLayers()

    def setParentObj(self):
        for i, childAssetName in enumerate(self.containerObj.generator.AllChildAssetsNames):
            parentLayerName = self.layer.parent.parent.name + "_" + self.layerSuffix
            if fnmatch.fnmatch(childAssetName, parentLayerName ) :
                self.parentObj = self.containerObj.generator.AllChildAssetsObjs[i]
                break
        if self.parentObj != None:
            if debug:
                print(self.name + " parent obj is " + self.parentObj.name)
        else:
            if debug:
                print(self.name + " parent obj is Root")



    def setDirectChildLayers(self):
        directChildLayers = []
        parentGRP = self.layer.parent
        for layer in parentGRP:
            if layer.is_group():
                directChildLayers.append(layer)
        return directChildLayers

    def appendSelfToParent(self):
        if self.parentObj != None:
            self.parentObj.childObjs.append(self)

    def setChildrenFactorParmNames(self):
        for child in self.childObjs:
            child.factorParmNames = self.factorParmNames

    def debugPrintParentChildObjs(self):
        print("-------------------------")
        print(self.name )
        if self.parentObj != None:
            print("Parent Objs: " + self.parentObj.name)
        else:
            print("Parent Objs: Root ")
        #print("Child Objs: ")
        #pprint.pprint( [o.name for o in self.childObjs])
        print("-----------------------")


    def setMasterGroup(self):
        if self.containerObj.parent.name == "Root":
            return True

    def setLayerNameParms(self):
        for parm, layer in self.parmLayerDict.items():
            try:
                self.node.parm(parm).set(layer.name)
            except:
                pass


    def linkFile(self):
        if debug:
            print("DEBUG: Linking File Parm from: " + self.parentNode.name() + " to " + self.node.name())
        fileParm = self.parentNode.parm("renamedFile")
        self.node.parm("file").set(WPN_Utils.linkExpressionParentParmToParm(fileParm, force_evaluate = True, string = True))

    def getParmsOfPrefix(self, node, parmPrefix):
        if debug:
            print("DEBUG: Getting Parms in " + node.name() + " for " + parmPrefix)
        return node.globParms(parmPrefix+"*")

    def getParmSourceTargetDict(self, node, parmPrefix):
        parmSourceTargetDict = {}
        parmSourceNames = [ parmSource.name() for parmSource in self.parmSources]
        if debug:
            print("Getting ParmSourceTargetDict in " + node.name() + " for " + parmPrefix)
        #pprint.pprint(parmSourceNames)
        for parm in node.parms():
            matchParmList = fnmatch.filter(parmSourceNames, "*" + parm.name())
            if len(matchParmList)>0:
                matchedParm = self.parentNode.parm(matchParmList[0])
                if "crveShpProfile" in matchedParm.name():
                    pass
                else:
                    parmSourceTargetDict[matchedParm] = parm
        return parmSourceTargetDict

    """TODO REFACTOR THIS, maybe too specific?"""
    def genOverallMods(self):
        overallCTRLFolderPT = self.PTG.containingFolder("copyCTRLS")
        #print(self.PTG.name())
        if len(self.flatParmMods) > 0 and self.masterGroup == True:
            modifierFolderPT = hou.FolderParmTemplate(self.layerPrefix + "Modifiers",self.layerPrefix + " Modifiers", folder_type=hou.folderType.Simple)
            modifierFolderName = modifierFolderPT.name()
            self.PTG.appendToFolder(overallCTRLFolderPT, modifierFolderPT)
            self.parentNode.setParmTemplateGroup(self.PTG, rename_conflicting_parms= True)
            for parmToModName, defaultValue in self.flatParmMods.items():
                modifierFolder= self.PTG.find(modifierFolderName)
                parmTemplateToMod = self.PTG.find(self.name + "_" + parmToModName)
                parmModName = parmTemplateToMod.name() + "_MOD"
                self.flatParmTarget[parmModName] = parmToModName
                parmTemplateToMod.setName(parmModName)
                parmTemplateToMod.setDefaultValue((defaultValue,))
                self.PTG.appendToFolder(modifierFolder, parmTemplateToMod)
            for parmToModName, factor in self.parmModFactor.items():
                modifierFolder= self.PTG.find(modifierFolderName)
                factorParmName = self.name + "_" + parmToModName + "_FACTOR"
                factorParmLabel = parmToModName + " Factor"
                factorPT = hou.FloatParmTemplate(factorParmName,factorParmLabel, 1, default_value=(factor,))
                #print(modifierFolderPT.name())
                self.factorParmNames[factorParmName] = parmToModName
                self.PTG.appendToFolder(modifierFolder, factorPT)
            self.parentNode.setParmTemplateGroup(self.PTG, rename_conflicting_parms= True)


    def linkflatParmMods(self):
        for parmModName, targetName in self.flatParmTarget.items():
            sourceParm = self.parentNode.parm(parmModName)
            targetParm = self.node.parm(targetName)
            ogTargetExpression = targetParm.expression()
            modTargetExpression = ogTargetExpression + "+" + WPN_Utils.linkExpressionParentParmToParm(sourceParm)
            targetParm.setExpression(modTargetExpression)

    def linkFactorParmMods(self):
        for parmModName, parmTargetName in self.factorParmNames.items():
            #print("gothere")
            sourceParm = self.parentNode.parm(parmModName)
            for childObj in self.childObjs:
                node = childObj.node
                targetParm = node.parm(parmTargetName)
                parmModBase = self.node.parm(parmTargetName)
                ogTargetExpression = targetParm.expression()
                parmModBaseExpr = WPN_Utils.getlinkExpression(targetParm, parmModBase)

                modTargetExpression = ogTargetExpression + "+" + parmModBaseExpr + "*" + WPN_Utils.linkExpressionParentParmToParm(sourceParm)
                targetParm.setExpression(modTargetExpression)


    def linkParmSourcesToTargets(self):
        if debug:
            print("DEBUG: Linking Parm Sources to Targets for " + self.node.name())
        for source, target in self.parmSourceTargetDict.items():
            if debug:
                print("DEBUG: Linking " + source.name() + " to " + target.name())
            target.setExpression(WPN_Utils.linkExpressionParentParmToParm(source))



    def createNode(self):
        if self.parentContainerNode == None:
            self.parentContainerNode = self.containerObj.subnetContainerNode
        self.node = self.parentContainerNode.createNode(self.nodeType, self.layer.name)
        self.node.moveToGoodPosition()
        print("Created: " + self.node.name())
        self.postNodeCreation()
        return self.node

    def replicateParmsInHDA(self):
        if debug:
            print("DEBUG: " + self.name + " Replicating Parms.")
        self.ptg = self.node.parmTemplateGroup()
        code = "import hou \n"
        code += self.ptg.asCode(function_name = "createPTG")
        parmTemplateLibPath = str(pathlib.Path(__file__).parent.resolve()) + "/parmTemplatelib.py"
        source_file = open(
            parmTemplateLibPath,
            "w")
        source_file.write(code)
        source_file.close()
        from WPN_GENERATOR_PY import parmtemplatelib as PTL
        imp.reload(PTL)
        genPTG = PTL.createPTG()
        self.PTG = self.parentNode.parmTemplateGroup()
        #advancedFolderPT = hou.FolderParmTemplate("advanced", "Advanced", folder_type = hou.folderType.Collapsible)
        #advancedFolder = self.PTG.containingFolder("refreshRamps")
        #self.PTG.append(advancedFolderPT)
        for parmTemplate in genPTG.entries():
            if not fnmatch.fnmatch(parmTemplate.name(), "*exclude*"):
                parmTemplate.setName(self.name)
                parmTemplate.setLabel(self.name)
                advancedFolder = self.PTG.containingFolder("refreshRamps")
                self.PTG.appendToFolder(advancedFolder, parmTemplate)
                self.recursiveSetParmPrefixAndConditionals(parmTemplate)

                #self.parmSources = [ parmTemp for parmTemp in parmTemplate.parmTemplates()]


        self.parentNode.setParmTemplateGroup(self.PTG, rename_conflicting_parms= True)

    def recursiveSetParmPrefixAndConditionals(self, parmTemplate):

        """Sets parm prefix + conditionals"""
        for parmTemplate in parmTemplate.parmTemplates():
            if parmTemplate.type() == hou.parmTemplateType.Folder:
                renamedParmTemplateFolder = self.PTG.find(parmTemplate.name())
                renamedParmTemplateFolder.setName(self.name + "_" + parmTemplate.name())
                for conditionalType, condition in renamedParmTemplateFolder.conditionals().items():
                    conditionSplit = condition.split(" ")
                    conditionReplaced = self.name + "_" + conditionSplit[1]
                    conditionSplit[1] = conditionReplaced
                    condition = " ".join(conditionSplit)


                    renamedParmTemplateFolder.setConditional(conditionalType, condition)
                self.PTG.replace(parmTemplate.name(), renamedParmTemplateFolder)
                self.recursiveSetParmPrefixAndConditionals(parmTemplate)
            else:
                renamedParmTemplate = self.PTG.find(parmTemplate.name())
                renamedParmTemplate.setName(self.name + "_" + parmTemplate.name())
                self.PTG.replace(parmTemplate.name(), renamedParmTemplate)
                """Get parmSources only within this Asset"""
                self.parmSources.append(renamedParmTemplate)







    def postNodeCreation(self):
        self.replicateParmsInHDA()
        self.genOverallMods()
        #self.parmSources = self.getParmsOfPrefix(self.parentNode, self.name)
        self.parmTargets = self.getParmsOfPrefix(self.node, self.name)
        self.parmSourceTargetDict = self.getParmSourceTargetDict(self.node, self.name)
        self.linkParmSourcesToTargets()
        self.linkFile()
        self.setLayerNameParms()
        self.linkflatParmMods()
        self.debug()


    def debug(self):
        if debug:
            print("DEBUG: Parm Sources for " + self.name + " is:")
            pprint.pprint(self.parmSources)
            print("DEBUG: Parm Targets for " + self.name + " is:")
            pprint.pprint(self.parmTargets)
            print("DEBUG: ParmSourceTargetDict for " + self.name + " is:")
            pprint.pprint(self.parmSourceTargetDict)








