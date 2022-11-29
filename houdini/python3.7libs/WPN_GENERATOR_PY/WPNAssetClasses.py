from WPN_GENERATOR_PY import PSDAssetClasses as psdAsset

import fnmatch
import imp
imp.reload(psdAsset)

""" ------------------GLOBALS------------------------ """
gunPartHDAName = "WPN::GUNPART_ASSET::1.0"
cutoutHDAName = "WPN::SIDE_CUTOUT_ASSET::1.0"
frontCutoutHDAName = "WPN::FRONT_CUTOUT_ASSET::1.0"

debug = False
""" ------------------GLOBALS------------------------ """

class GunPartContainer(psdAsset.Container):
    def childAssetDefinition(self, childLayerName, childlayer):
        if childLayerName == "SIDE":
            childAsset = GunPartAsset(childlayer, self)
        elif fnmatch.fnmatch(childlayer.name, "*FRONT_CUTOUT*"):
            childAsset = FrontCutoutAsset(childlayer, self)
        elif fnmatch.fnmatch(childlayer.name, "*SIDE_ADDON*"):
            childAsset = AddonAsset(childlayer, self)
        elif fnmatch.fnmatch(childlayer.name, "*SIDE_CUTOUT*"):
            childAsset = CutoutAsset(childlayer, self)
        else:
            childAsset = None
        return childAsset



class GunPartAsset(psdAsset.ChildAsset):
    def __init__(self, *args, **kwargs):
        super( GunPartAsset, self).__init__(*args, **kwargs)
        self.nodeType = gunPartHDAName
        self.frontLayer = self.setToSameDepthLayer(self.layerPrefix + "_FRONT")
        self.spineLayer = self.setToSameDepthLayer(self.layerPrefix + "_SPINE")
        self.topLayer = self.setToSameDepthLayer(self.layerPrefix + "_TOP" )
        self.cylShape = self.setToSameDepthLayer(self.layerPrefix + "_CYL")
        self.thinPart = self.setToSameDepthLayer(self.layerPrefix + "_THIN")
        self.exclParentCutout = self.setToSameDepthLayer(self.layerPrefix + "_EXCLUDE_PRNT_CUTOUT")
        self.cutoutObjs = []


        self.parmLayerDict = { "layer_name1": self.layer,
                          "FRONT_layer_name1": self.frontLayer,
                          "TOP_layer_name1": self.topLayer,
                          "SPINE_layer_name1": self.spineLayer,
                          }
        self.flatParmMods = {"zThickness": 0.012}
        self.parmModFactor = {"zThickness": [0.85, 0.5, 1.0]} #Parm to create factor for : [default value, minimum value, maximum value]


    def setToSameDepthLayer(self, layerName):
        if debug:
            print("DEBUG: Finding: " + layerName)
        foundLayer = None
        for layer in self.containerObj.PSDGroup.descendants():
            #print("parentObj.psdGroup :" + layer.name)
            if fnmatch.fnmatch(layer.name, layerName):
                foundLayer = layer
                if debug:
                    print("DEBUG: " + self.name + " Found " + layer.name)
                return foundLayer
        if foundLayer == None:
            if debug:
                print("No " + layerName + " layer found!" )



    def setCarvedShape(self):

        if self.frontLayer != None and self.topLayer != None:
            if debug:
                print("DEBUG: Both Front and Top Layer Exists! Setting Shape Profile to Both")
            self.node.parm("crveShp").set(3)
        elif self.frontLayer != None:
            if debug:
                print("DEBUG: Front Layer Exists! Setting Shape Profile to FRONT")
            self.node.parm("crveShp").set(1)
        elif self.frontLayer != None:
            if debug:
                print("DEBUG: Top Layer Exists! Setting Shape Profile to TOP")
                self.node.parm("crveShp").set(2)

    def setUseDrawnSpine(self):

        if self.spineLayer != None:
            if debug:
                print("DEBUG: Spine Layer Exists! Setting Shape Profile to True")
            self.node.parm("contourBased").set(1)
            self.node.parm("useDrawnSpine").set(1)

    def setShape(self):
        if self.cylShape != None:
            if debug:
                print("DEBUG: Cyl Layer Exists! Setting Shape Switch to Cylindrical")
            self.node.parm("shpSwitch").set(0)
        elif self.thinPart != None:
            if debug:
                print("DEBUG: ThinPart Layer Exists! Setting Shape Switch to ThinPart")
            self.node.parm("shpSwitch").set(2)


    def setCutoutPattern(self):
        if len(self.cutoutObjs) != 0:
            if debug:
                print("DEBUG: CutoutObjs Exists! Setting CutoutPattern")
            CutoutPattern = ''.join([i for i in self.cutoutObjs[0].name if not i.isdigit()])+"*"
            self.node.parm("cutoutPattern").set(CutoutPattern)

    def setExclude(self):
        if self.exclParentCutout != None:
            if debug:
                print("DEBUG: Exclude Parent Cutouts Layer Exists! Toggle on excludeParentCutouts")
            self.node.parm("excludeParentCutouts").set(1)
            #print("set exclude parent cutouts")

    def postNodeCreation(self, *args, **kwargs):
        super( GunPartAsset, self).postNodeCreation(*args, **kwargs)
        self.setLayerNameParms()
        self.setCarvedShape()
        self.setUseDrawnSpine()
        self.setShape()
        self.setExclude()
        self.node.setDisplayFlag(True)







class CutoutAsset(psdAsset.ChildAsset):
    def __init__(self, *args, **kwargs):
        super( CutoutAsset, self).__init__(*args, **kwargs)
        self.nodeType = cutoutHDAName
        self.parmLayerDict = { "layer_name1": self.layer}


    def postNodeCreation(self, *args, **kwargs):
        super(CutoutAsset, self).postNodeCreation(*args, **kwargs)
        self.node.setDisplayFlag(False)

class AddonAsset(CutoutAsset):
    def __init__(self, *args, **kwargs):
        super( AddonAsset, self).__init__(*args, **kwargs)
        self.nodeType = cutoutHDAName
        self.parmLayerDict = { "layer_name1": self.layer}



class FrontCutoutAsset(CutoutAsset):
    def __init__(self, *args, **kwargs):
        super( FrontCutoutAsset, self).__init__(*args, **kwargs)
        self.nodeType = frontCutoutHDAName


