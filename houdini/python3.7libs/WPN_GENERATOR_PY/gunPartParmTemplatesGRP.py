# Code for parameter template
import hou

def genGunpartParmTemplates(gunpartName):
    #hou_parm_template = hou.FolderParmTemplate("numOf_"+ gunpartName, "Num Of "+gunpartName, folder_type=hou.folderType.TabbedMultiparmBlock, default_value=0, ends_tab_group=False)
    # Code for parameter template
    hou_parm_template2 = hou.FolderParmTemplate(gunpartName, gunpartName, folder_type=hou.folderType.Tabs, ends_tab_group=False)
    # Code for parameter template
    hou_parm_template3 = hou.FolderParmTemplate("trcCTRLs", "Trace Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template3.setTags({"group_type": "simple"})
    # Code for parameter template
    # hou_parm_template4 = hou.ButtonParmTemplate(gunpartName+"_reload", "Reload PSD")
    # hou_parm_template4.setTags({"autoscope": "0000000000000000"})
    # hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    # hou_parm_template4 = hou.StringParmTemplate(gunpartName+"_layer_name1", "Layer Name", 1, default_value=([""]),
    #                                             naming_scheme=hou.parmNamingScheme.Base1,
    #                                             string_type=hou.stringParmType.Regular, menu_items=([]),
    #                                             menu_labels=([]), icon_names=([]),
    #                                             item_generator_script="opmenu -l -a GEO_CONTAINER/BRRL_CONTAINER/BRRL1 layer_name1",
    #                                             item_generator_script_language=hou.scriptLanguage.Hscript,
    #                                             menu_type=hou.menuType.StringReplace)
    # hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    # hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    # hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_thresh1", "Brightness Threshold", 1, default_value=([0.01]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setTags({"autoscope": "0000000000000000"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_step1", "Resample Step", 1, default_value=([0.52]), min=0.001, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setTags({"autoscope": "0000000000000000"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FolderParmTemplate("genShpCTRLs", "General Shape Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template3.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template4 = hou.MenuParmTemplate(gunpartName+"_shpSwitch", "Shape Switch", menu_items=(["0","1"]), menu_labels=(["Cylindrical","Flat"]), default_value=1, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FolderParmTemplate("cylCTRLs", "Cylindrical Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template3.setConditional(hou.parmCondType.HideWhen, "{ " + gunpartName + ""+ "_shpSwitch != 0 }")
    hou_parm_template3.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_scale2", "Scale", 3, default_value=([1, 1, 1]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.IntParmTemplate(gunpartName+"_sides", "Sides", 1, default_value=([12]), min=1, max=50, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_WallThickness", "Wall Thickness", 1, default_value=([0]), min=-0.2,
                                               max=0.2, min_is_strict=False, max_is_strict=False,
                                               look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FolderParmTemplate("flatCTRLs", "Flat Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template3.setConditional(hou.parmCondType.HideWhen, "{ " + gunpartName + ""+ "_shpSwitch != 1 }")
    hou_parm_template3.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_zThickness", "Z-Thickness", 1, default_value=([0.012]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FolderParmTemplate("xShpCTRLs", "X-Axis Shape Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template3.setTags({"group_type": "simple"})
    # Code for parameter template
    #hou_parm_template4 = hou.ToggleParmTemplate(gunpartName+"_crveShp", "Carved Shape", default_value=False)
    hou_parm_template4 = hou.MenuParmTemplate(gunpartName+"_crveShp", "Carved Shape", menu_items=(["0", "1", "2", "3"]),
                                             menu_labels=(["NONE", "FRONT", "TOP", "FRONT AND TOP"]), default_value=0,
                                             icon_names=([]), item_generator_script="",
                                             item_generator_script_language=hou.scriptLanguage.Python,
                                             menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False,
                                             strip_uses_icons=False)

    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_xChamfer", "Chamfer", 1, default_value=([0.096]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setConditional(hou.parmCondType.HideWhen, "{ " + gunpartName + ""+ "_crveShp != 1 }")
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    targetContainerName = gunpartName.split("_")[0]
    hou_parm_template4 = hou.RampParmTemplate(gunpartName+"_crveShpProfile", "Carved Shape Profile", hou.rampParmType.Float, default_value=3, default_basis=None, color_type=None, script_callback = "hou.phm().setRamp(kwargs['parm'],kwargs['node']," + "'GEO_CONTAINER/"+targetContainerName+"_CONTAINER/"+ gunpartName + "')")
    hou_parm_template4.setConditional(hou.parmCondType.HideWhen, "{ " + gunpartName + ""+ "_crveShp != 1 }")
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "rampfloatdefault": "1pos ( 0 ) 1value ( 0 ) 1interp ( linear ) 2pos ( 0.0066137565299868584 ) 2value ( 1 ) 2interp ( linear ) 3pos ( 1 ) 3value ( 1 ) 3interp ( linear )", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FolderParmTemplate("bvlCTRLs", "Bevel Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template3.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_bvlFlatAngle", "Bevel Flat Angle", 1, default_value=([51.8]), min=0, max=180, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_bvlWidth", "Bevel Width", 1, default_value=([0.002]), min=0, max=1, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    #hou_parm_template.addParmTemplate(hou_parm_template2)
    return hou_parm_template2

def genGunpartParentTemplates(gunpartName):
    # Code for parameter template
    hou_parm_template = hou.FolderParmTemplate(gunpartName, gunpartName, folder_type=hou.folderType.Tabs, ends_tab_group=False)
    return hou_parm_template

def genCutoutParmTemplates(gunpartName):
    #hou_parm_template = hou.FolderParmTemplate("numOf_"+ gunpartName, "Num Of "+gunpartName, folder_type=hou.folderType.TabbedMultiparmBlock, default_value=0, ends_tab_group=False)
    # Code for parameter template
    hou_parm_template2 = hou.FolderParmTemplate(gunpartName, gunpartName, folder_type=hou.folderType.Tabs, ends_tab_group=False)
    # Code for parameter template
    hou_parm_template3 = hou.FolderParmTemplate("trcCTRLs", "Trace Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template3.setTags({"group_type": "simple"})
    # Code for parameter template
    # hou_parm_template4 = hou.ButtonParmTemplate(gunpartName+"_reload", "Reload PSD")
    # hou_parm_template4.setTags({"autoscope": "0000000000000000"})
    # hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    # hou_parm_template4 = hou.StringParmTemplate(gunpartName+"_layer_name1", "Layer Name", 1, default_value=([""]),
    #                                             naming_scheme=hou.parmNamingScheme.Base1,
    #                                             string_type=hou.stringParmType.Regular, menu_items=([]),
    #                                             menu_labels=([]), icon_names=([]),
    #                                             item_generator_script="opmenu -l -a GEO_CONTAINER/BRRL_CONTAINER/BRRL1 layer_name1",
    #                                             item_generator_script_language=hou.scriptLanguage.Hscript,
    #                                             menu_type=hou.menuType.StringReplace)
    # hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    # hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    # hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_thresh1", "Brightness Threshold", 1, default_value=([0.01]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setTags({"autoscope": "0000000000000000"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_step1", "Resample Step", 1, default_value=([0.52]), min=0.001, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setTags({"autoscope": "0000000000000000"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FolderParmTemplate("genShpCTRLs", "General Shape Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template3.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template4 = hou.MenuParmTemplate(gunpartName+"_shpSwitch", "Shape Switch", menu_items=(["0","1"]), menu_labels=(["Cylindrical","Flat"]), default_value=1, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    hou_parm_template4 = hou.IntParmTemplate(gunpartName+"_leftRight", "LEFT/RIGHT", 1, default_value=([0]), min=0, max=1,
                                            min_is_strict=True, max_is_strict=False,
                                            naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]),
                                            icon_names=([]), item_generator_script="",
                                            item_generator_script_language=hou.scriptLanguage.Python,
                                            menu_type=hou.menuType.Normal, menu_use_token=False)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.ToggleParmTemplate(gunpartName+"_mirrored", "Mirrored", default_value=True)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FolderParmTemplate("cylCTRLs", "Cylindrical Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template3.setConditional(hou.parmCondType.HideWhen, "{ " + gunpartName + ""+ "_shpSwitch != 0 }")
    hou_parm_template3.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_scale2", "Scale", 3, default_value=([1, 1, 1]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.IntParmTemplate(gunpartName+"_sides", "Sides", 1, default_value=([12]), min=1, max=50, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # # Code for parameter template
    # hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_WallThickness", "Wall Thickness", 1, default_value=([0]), min=-0.2,
    #                                            max=0.2, min_is_strict=False, max_is_strict=False,
    #                                            look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    # hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    # hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    # hou_parm_template3.addParmTemplate(hou_parm_template4)
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName + "_cylThickness", "Cylindrical Thickness", 1,
                                               default_value=([0]), min=-10,
                                               max=10, min_is_strict=False, max_is_strict=False,
                                               look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FolderParmTemplate("flatCTRLs", "Flat Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template3.setConditional(hou.parmCondType.HideWhen, "{ " + gunpartName + ""+ "_shpSwitch != 1 }")
    hou_parm_template3.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_zThickness", "Z-Thickness", 1, default_value=([0.012]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)

    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    # hou_parm_template3 = hou.FolderParmTemplate("xShpCTRLs", "X-Axis Shape Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    # hou_parm_template3.setTags({"group_type": "simple"})
    # # Code for parameter template
    # hou_parm_template4 = hou.ToggleParmTemplate(gunpartName+"_crveShp", "Carved Shape", default_value=False)
    # hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    # hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    # hou_parm_template3.addParmTemplate(hou_parm_template4)
    # # Code for parameter template
    # hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_xChamfer", "Chamfer", 1, default_value=([0.096]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    # hou_parm_template4.setConditional(hou.parmCondType.HideWhen, "{ " + gunpartName + ""+ "_crveShp != 1 }")
    # hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    # hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    # hou_parm_template3.addParmTemplate(hou_parm_template4)
    # # Code for parameter template
    # targetContainerName = gunpartName.split("_")[0]
    # hou_parm_template4 = hou.RampParmTemplate(gunpartName+"_crveShpProfile", "Carved Shape Profile", hou.rampParmType.Float, default_value=3, default_basis=None, color_type=None, script_callback = "hou.phm().setRamp(kwargs['parm'],kwargs['node']," + "'GEO_CONTAINER/"+targetContainerName+"_CONTAINER/"+ gunpartName + "')")
    # hou_parm_template4.setConditional(hou.parmCondType.HideWhen, "{ " + gunpartName + ""+ "_crveShp != 1 }")
    # hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    # hou_parm_template4.setTags({"autoscope": "0000000000000000", "rampfloatdefault": "1pos ( 0 ) 1value ( 0 ) 1interp ( linear ) 2pos ( 0.0066137565299868584 ) 2value ( 1 ) 2interp ( linear ) 3pos ( 1 ) 3value ( 1 ) 3interp ( linear )", "script_callback_language": "python"})
    # hou_parm_template3.addParmTemplate(hou_parm_template4)
    #hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FolderParmTemplate("bvlCTRLs", "Bevel Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template3.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_bvlFlatAngle", "Bevel Flat Angle", 1, default_value=([51.8]), min=0, max=180, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    # Code for parameter template
    hou_parm_template4 = hou.FloatParmTemplate(gunpartName+"_bvlWidth", "Bevel Width", 1, default_value=([0.002]), min=0, max=1, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template4.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template4.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template3.addParmTemplate(hou_parm_template4)
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    #hou_parm_template.addParmTemplate(hou_parm_template2)
    return hou_parm_template2