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
    for parm in this_node.spareParms():
        if debug:
            print("Saving:" + parm.name() + " : " + str(parm.eval()))
        parmValueDict[parm.name()] = parm.eval()

def setParmValues(this_node):
    global parmValueDict
    for parm in this_node.spareParms():
        if debug:
            print("Setting " + parm.name() + " with :" + str(parmValueDict[parm.name()]))
        if  parm.name().split("_")[-1] in dontCopyParms:
            continue
        else:
            parm.set(parmValueDict[parm.name()])


def reload(this_node, forceVisible = True):
    imp.reload(WPNGEN)
    PCDict = WPNGEN.getPSDGrpAndChildren(this_node)
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


def copyFilePath(this_node):
    fbxNode = this_node.node("EXPORT/filmboxfbx1")
    exportFilepath = fbxNode.parm("sopoutput").eval()

    if exists(exportFilepath):
        pyperclip.copy(exportFilepath.replace("/", '\\'))
        hou.ui.displayMessage("EXPORT FILEPATH has been copied to clipboard!")
    else:
        hou.ui.displayMessage("No export found! Please export first!")
    
def goToFolder(this_node):
    fbxNode = this_node.node("EXPORT/filmboxfbx1")
    exportFilepath = fbxNode.parm("sopoutput").eval()

    if exists(exportFilepath):
        startfile(split(exportFilepath)[0])
    else:
        hou.ui.displayMessage("No export found! Please export first!")
    