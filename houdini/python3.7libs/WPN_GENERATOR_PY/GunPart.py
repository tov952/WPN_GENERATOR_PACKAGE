import hou

from WPN_GENERATOR_PY import WPN_Enums


class gunpart():

    def __init__(self, name, GPType,  index):


        self.name = name + str(index+1)
        self.parmPrefix = GPType.name + str(index+1)
        self.nodeType = "WPN::GUNPART_ASSET::1.0"
        self.GPType = GPType
        self.node = None
        self.containerName = name+"_CONTAINER"
        self.container = None
        self.shapeType = None
        self.validLayerName = ""


    def createGunpartNode(self):
        #print(self.containerName)
        HDA = hou.pwd()
        geoContainer = HDA.node("GEO_CONTAINER")
        inputGeoContainer1 = geoContainer.indirectInputs()[0]
        self.container = geoContainer.node(self.containerName)
        if self.container == None:
            self.container = geoContainer.createNode("subnet", self.containerName)
            self.container.setInput(0, inputGeoContainer1)
            self.container.moveToGoodPosition()
        input1 = self.container.indirectInputs()[0]
        gunpartNode = self.container.createNode(self.nodeType, self.name)
        gunpartNode.setInput(0, input1)
        gunpartNode.moveToGoodPosition()
        print("Created: " + gunpartNode.name())
        self.node = gunpartNode
        return gunpartNode

    def setValidLayerName(self):
        try:
            self.validLayerName= self.node.globParms("*layer_name1")[0].evalAsString()
            #print(self.name + "'s ValidLayerName is: " + self.validLayerName)
        except:
            pass



    def setShapeType(self):
        if self.validLayerName == "":
            self.setValidLayerName()

        shapeSuffix = self.validLayerName.split("_")[-1]
        try:
            self.shapeType = WPN_Enums.shapeType[shapeSuffix]
            #print(self.validLayerName + "'s Shape Type is: " + self.shapeType.name)
            print("Setting " + self.validLayerName + "/" + self.node.name() + " to " + WPN_Enums.shapeTypeNiceNames[self.shapeType])
            self.node.parm("shpSwitch").set(self.shapeType.value)
        except:
            print("ERROR: " + self.validLayerName + "/" + self.node.name() + " ShapeType Setting failed, Check LayerName Conventions; [gunPart]#_[shapeType]")









