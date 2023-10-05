from WPN_GENERATOR_PY import WPN_Generator_GRP as WPNGEN

import imp
import pyperclip
import hou

from os.path import exists
from os.path import split
from os import startfile
from os import sep
""" ------------------GLOBALS------------------------ """
parmValueDict = {}
dontCopyParms = ['crveShp', 'contourBased','useDrawnSpine', 'shpSwitch', 'excludeParentCutouts']
debug = False
""" ------------------GLOBALS------------------------ """

def copyCTRLs(this_node):
    print("Copying Controls")
    saveParmValues(this_node)

def pasteCTRLs(this_node):
    print("Pasting Controls")
    setParmValues(this_node)


def empty(this_node):
    geoCon = this_node.node("GEO_CONTAINER")
    for child in geoCon.children():
        child.destroy()
    this_node.removeSpareParms()

def saveParmValues(this_node):
    global parmValueDict
    if len(this_node.spareParms()) != 0:
        for parm in this_node.spareParms():
            if debug:
                print("Saving:" + parm.name() + " : " + str(parm.eval()))
            parmValueDict[parm.name()] = parm.eval()
    else:
        if debug:
            print("No spare parms found. Not saving parm values.")

def setParmValues(this_node):
    global parmValueDict
    if len(parmValueDict) != 0:
        for parm in this_node.spareParms():
            if  parm.name().split("_")[-1] in dontCopyParms:
                continue
            else:
                if debug:
                    print("Setting " + parm.name() + " with :" + str(parmValueDict[parm.name()]))
                try:
                    parm.set(parmValueDict[parm.name()])
                except:
                    continue


def reload(this_node, forceVisible = True):
    imp.reload(WPNGEN)
    WPNGEN.cleanUpPSD(this_node)
    PCDict = WPNGEN.getPSDGrpAndChildren()
    WPNGEN.renameChildLayersAndSave(PCDict, forceVisible)
    geoCon = this_node.node("GEO_CONTAINER")
    containers = geoCon.glob("*_CONTAINER")
    for container in containers:
        nodes = container.children()
        for node in nodes:
            node.parm("recook").pressButton()


def setRamp(this_parm, this_node, targetNodePath):
    this_parmNameSplit = this_parm.name().split("_")
    this_parmPrefix = '_'.join(this_parmNameSplit[0:-1])
    targetParmName = this_parmNameSplit[-1]
    targetNode = this_node.node(targetNodePath)
    target = targetNode.parm(targetParmName)

    this_ramp = this_parm.eval()

    target.set(this_parm.evalAsRampAtFrame(0))

def refreshRamps(this_node):
    rampParms = getAllRampParms(this_node)
    for rampParm in rampParms:
        rampParm.pressButton()


def getAllRampParms(this_node):
    rampParms = []
    parms = this_node.parms()
    for parm in parms:
        try:
            parm.evalAsRamp()
            rampParms.append(parm)
        except:
            pass

    return rampParms

def preExportSetup(this_node):
    preExportNode = this_node.node("PRE_EXPORT_PROCESS")
    hiResExportNode = preExportNode.node("OUT_HIGH_RES_EXPORT")
    lowResExportNode = preExportNode.node("OUT_LOW_RES_EXPORT")

    hiResMeshNames = hiResExportNode.geometry().stringListAttribValue("MESHES")
    lowResMeshNames = lowResExportNode.geometry().stringListAttribValue("MESHES")

    exportNode = this_node.node("EXPORT")
    lowResExportGeoNode = exportNode.node("LOW_RES_GEOMETRY")
    hiResExportGeoNode = exportNode.node("HIGH_RES_GEOMETRY")

    populateExportGeometries(hiResMeshNames, hiResExportNode, hiResExportGeoNode )
    populateExportGeometries(lowResMeshNames, lowResExportNode, lowResExportGeoNode )

def populateExportGeometries(meshNames, exportNode, targetNode):

    targetNode.deleteItems(targetNode.allItems())
    for meshName in meshNames:
        geo = targetNode.createNode("geo", meshName)
        objMerge = geo.createNode("object_merge")
        objMerge.parm("objpath1").set(exportNode.path())
        blast = geo.createNode("blast")
        blast.parm("group").set(f"@MESH_NAME={meshName}")
        blast.parm("negate").set(True)
        blast.setFirstInput(objMerge)
        blast.setDisplayFlag(True)
        blast.setRenderFlag(True)
        geo.layoutChildren()
    targetNode.layoutChildren()



def copyFilePath(this_node, exportType = "fbx"):
    if exportType=="fbx":
        node = this_node.node("EXPORT/HI_RES_FBX")
    elif exportType=="obj":
        node = this_node.node("EXPORT/HI_RES_OBJ")
    exportFilepath = node.parm("sopoutput").eval()

    pyperclip.copy(exportFilepath.replace("/", '\\'))
    hou.ui.displayMessage("EXPORT FILEPATH has been copied to clipboard!")

    
def goToFolder(this_node):
    fbxNode = this_node.node("EXPORT/HI_RES_FBX")
    objNode = this_node.node("EXPORT/HI_RES_OBJ")
    fbxExportFilepath = fbxNode.parm("sopoutput").eval()
    objExportFilepath = objNode.parm("sopoutput").eval()

    if not exists(fbxExportFilepath) and not exists(objExportFilepath):
        hou.ui.displayMessage("No export found! Please export first!")
    else:
        startfile(split(fbxExportFilepath)[0])

    