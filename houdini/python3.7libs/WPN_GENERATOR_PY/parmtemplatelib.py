import hou 
def createPTG():
    hou_parm_template_group = hou.ParmTemplateGroup()
    # Code for parameter template
    hou_parm_template = hou.FolderParmTemplate("assetInfo_exclude", "Asset Info", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template2 = hou.StringParmTemplate("file", "File", 1, default_value=(["$JOB/test2.psd"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.FileReference, file_type=hou.fileType.Image, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
    hou_parm_template2.setJoinWithNext(True)
    hou_parm_template2.setTags({"autoscope": "0000000000000000", "filechooser_pattern": "*.psd"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.ButtonParmTemplate("reload", "Reload PSD")
    hou_parm_template2.setTags({"autoscope": "0000000000000000"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.StringParmTemplate("layer_name1", "Layer Name", 1, default_value=(["LWR_RCVR"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="opmenu -l -a trace_psd_file1 layer_name1", item_generator_script_language=hou.scriptLanguage.Hscript, menu_type=hou.menuType.StringReplace)
    hou_parm_template2.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.StringParmTemplate("FRONT_layer_name1", "Front Layer Name", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="opmenu -l -a FRONT_PROFILE layer_name1", item_generator_script_language=hou.scriptLanguage.Hscript, menu_type=hou.menuType.StringReplace)
    hou_parm_template2.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.StringParmTemplate("TOP_layer_name1", "TOP Layer Name", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="opmenu -l -a FRONT_PROFILE layer_name1", item_generator_script_language=hou.scriptLanguage.Hscript, menu_type=hou.menuType.StringReplace)
    hou_parm_template2.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.StringParmTemplate("SPINE_layer_name1", "SPINE Layer Name", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="opmenu -l -a SPINE layer_name1", item_generator_script_language=hou.scriptLanguage.Hscript, menu_type=hou.menuType.StringReplace)
    hou_parm_template2.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.StringParmTemplate("cutoutPattern", "CUTOUT Pattern", 1, default_value=(["node = hou.pwd()\nparentContainer = node.parent()\nparentName = \"_\".join(parentContainer.name().split(\"_\")[0:-1])\nreturn parentName + \"*CUTOUT*\"\n"]), default_expression=(["node = hou.pwd()\nparentContainer = node.parent()\nparentName = \"_\".join(parentContainer.name().split(\"_\")[0:-1])\nreturn parentName + \"*CUTOUT*\"\n"]), default_expression_language=([hou.scriptLanguage.Python]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
    hou_parm_template2.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template2.setTags({"script_callback_language": "python"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.StringParmTemplate("addonPattern", "ADDON Pattern", 1, default_value=(["node = hou.pwd()\nparentContainer = node.parent()\nparentName = \"_\".join(parentContainer.name().split(\"_\")[0:-1])\nreturn parentName + \"*ADDON*\""]), default_expression=(["node = hou.pwd()\nparentContainer = node.parent()\nparentName = \"_\".join(parentContainer.name().split(\"_\")[0:-1])\nreturn parentName + \"*ADDON*\""]), default_expression_language=([hou.scriptLanguage.Python]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
    hou_parm_template2.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template2.setTags({"script_callback_language": "python"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.StringParmTemplate("parentSideObject", "Parent SIDE Object", 1, default_value=(["try:\n    node = hou.pwd()\n    parentContainer = node.parent()\n    geoContainer = parentContainer.parent()\n    parentName = \"_\".join(parentContainer.name().split(\"_\")[0:-2])\n    parentContainer = geoContainer.node(parentName+\"_CONTAINER\")\n    targetNode = parentContainer.node(parentName + \"_SIDE\")\n    return \"../../\" +parentContainer.name() + \"/\" + targetNode.name()\nexcept:\n    return \"\"\n"]), default_expression=(["try:\n    node = hou.pwd()\n    parentContainer = node.parent()\n    geoContainer = parentContainer.parent()\n    parentName = \"_\".join(parentContainer.name().split(\"_\")[0:-2])\n    parentContainer = geoContainer.node(parentName+\"_CONTAINER\")\n    targetNode = parentContainer.node(parentName + \"_SIDE\")\n    return \"../../\" +parentContainer.name() + \"/\" + targetNode.name()\nexcept:\n    return \"\"\n"]), default_expression_language=([hou.scriptLanguage.Python]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
    hou_parm_template2.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template2.setTags({"autoscope": "0000000000000000", "oprelative": ".", "script_callback_language": "python"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    hou_parm_template_group.append(hou_parm_template)
    # Code for parameter template
    hou_parm_template = hou.FolderParmTemplate("gunPartName", "Gun Part Name", folder_type=hou.folderType.Collapsible, default_value=0, ends_tab_group=False)
    hou_parm_template.setTags({"group_type": "collapsible"})
    # Code for parameter template
    hou_parm_template2 = hou.FolderParmTemplate("trcCTRLs", "Trace Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template2.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("shpTension", "Shape Tension", 1, default_value=([0.8]), min=0.8, max=1.5, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.FolderParmTemplate("genShpCTRLs", "General Shape Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template2.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template3 = hou.MenuParmTemplate("shpSwitch", "Shape Switch", menu_items=(["0","1","2"]), menu_labels=(["Cylindrical","Flat","Thin-Part"]), default_value=1, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.ToggleParmTemplate("excludeParentCutouts", "Exclude Parent Cutouts", default_value=False)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.FolderParmTemplate("cylCTRLs", "Cylindrical Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ shpSwitch != 0 }")
    hou_parm_template2.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("scale2", "Scale", 3, default_value=([1, 1, 1]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.IntParmTemplate("sides", "Sides", 1, default_value=([100]), min=1, max=100, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("WallThickness", "Wall Thickness", 1, default_value=([0.3]), min=0.2, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.FolderParmTemplate("thinPartCTRLs", "Thin-Part Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ shpSwitch != 2 }")
    hou_parm_template2.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template3 = hou.ToggleParmTemplate("mirrorToggle", "Mirror", default_value=False)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.ToggleParmTemplate("leftRightToggle", "LEFT/RIGHT", default_value=False)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("thinPartThickness", "Thickness", 1, default_value=([0.0017]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("thinPartZPos", "Z-Position", 1, default_value=([0.005]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.FolderParmTemplate("flatCTRLs", "Flat Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ shpSwitch != 1 }")
    hou_parm_template2.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("zThickness", "Z-Thickness", 1, default_value=([0]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.ToggleParmTemplate("thinWallToggle", "Thin-Walled", default_value=False)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("thinWallThickness", "Thin-Walled Thickness", 1, default_value=([2]), min=1, max=4, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.MenuParmTemplate("crveShp", "Carved Shape", menu_items=(["0","1","2","3"]), menu_labels=(["NONE","FRONT","TOP","FRONT AND TOP"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
    hou_parm_template2.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.FolderParmTemplate("xShpCTRLs", "Cross-Section Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ crveShp != 1 }")
    hou_parm_template2.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("xChamfer", "Chamfer", 1, default_value=([0.096]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.ToggleParmTemplate("drawnToggle", "Use drawn layer", default_value=True, default_expression='on', default_expression_language=hou.scriptLanguage.Hscript)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.ToggleParmTemplate("flipDrawnLayer", "FlipDrawnLayer", default_value=False, default_expression='off', default_expression_language=hou.scriptLanguage.Hscript)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.RampParmTemplate("crveShpProfile", "Carved Shape Profile", hou.rampParmType.Float, default_value=3, default_basis=None, color_type=None)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "rampfloatdefault": "1pos ( 0 ) 1value ( 0 ) 1interp ( linear ) 2pos ( 0.0066137565299868584 ) 2value ( 1 ) 2interp ( linear ) 3pos ( 1 ) 3value ( 1 ) 3interp ( linear )", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.ToggleParmTemplate("contourBased", "Contour-based", default_value=False, default_expression='off', default_expression_language=hou.scriptLanguage.Hscript)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FolderParmTemplate("contourControls", "Contour Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template3.setConditional(hou.parmCondType.HideWhen, "{ contourBased != 1 }")
    hou_parm_template3.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template4 = hou.ToggleParmTemplate("useDrawnSpine", "Use Drawn Spine", default_value=True, default_expression='on', default_expression_language=hou.scriptLanguage.Hscript)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.ToggleParmTemplate("yxAxis", "Y/X Axis", default_value=False, default_expression='off', default_expression_language=hou.scriptLanguage.Hscript)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate("scaleY", "Carver Margin Scale ", 1, default_value=([4.06]), min=-10, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate("scaleX", "Carver Thickness Scale", 1, default_value=([1]), min=-10, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate("strength", "Carver Smoothness", 1, default_value=([0]), min=0, max=50, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.IntParmTemplate("segs", "Carver Resolution", 1, default_value=([9]), min=1, max=50, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate("bias", "Carver Spine Bias", 1, default_value=([1]), min=0, max=2, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    hou_parm_template.addParmTemplate(hou_parm_template2)
    hou_parm_template_group.append(hou_parm_template)
    return hou_parm_template_group
    
