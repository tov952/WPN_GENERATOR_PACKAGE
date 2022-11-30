def setParms(gunPartNode, targetValueDict):
    for targetParm, value in targetValueDict.items():
        gunPartNode.parm(targetParm).set(value)

def getAllGunPartNodes(this_node, validPSDLayerNames):
    gunPartNodes = []
    for validPSDLayerNames in validPSDLayerNames:
        gunPartNodeName = getNoShapeSuffixName(validPSDLayerNames)
        gunPartNodes.append(this_node.recursiveGlob(gunPartNodeName))
    return gunPartNodes


def getCleanName(name):
    nonDigitName = getNonDigitName(name)
    noShapeName = getNoShapeSuffixName(nonDigitName)
    return noShapeName


def getNonDigitName(name):
    nonDigitName = ''.join([i for i in name if not i.isdigit()])
    return nonDigitName


def getNoShapeSuffixName(name):
    noShapeName = "_".join(name.split("_")[0:-1])
    return noShapeName


def linkExpressionParentParmToParm(parmSource, force_evaluate=False, string=False, replaceStr =""):
    parmSourceName = parmSource.name()
    ch = "ch"
    if force_evaluate == True:
        ch = "`ch"
    if string == True:
        ch += "s"
    return ch + "('../../../" + parmSourceName + "')"

def getlinkExpression(parmTarget, parmSource):
    parmTarget.setExpression("")
    parmTarget.set(parmSource)
    return parmTarget.expression()