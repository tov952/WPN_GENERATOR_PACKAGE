#FutureShotgun Rendered in Houdini, Generated using this Toolset!

![FutureShotgun_Setup2_renderSETUP mantra1 0001](https://user-images.githubusercontent.com/59757164/207116271-09e9e082-59e3-4a39-b38f-20ead954351b.png)



# WPN GENERATOR PACKAGE
 
WPN Generator OTL toolsets for Houdini FX 18.5.596 and Above!

Check out the Showcase for an idea of what this can do! 
https://vimeo.com/780432219

Check out the short quickstart here on more details on how to use this tool!
https://vimeo.com/776701566

Packaged to be easy-to-install thanks to Christian Akesson and his tutorial!
https://learncreategame.com/techart/houdini-environment-setup/



# To Install:

1. Download and Unzip into a folder of your choice!

   You should see the following structure:

   ![image](https://user-images.githubusercontent.com/59757164/204878762-a7a11d1d-cf51-417e-8690-4cedaa3c0ef7.png)

2. In Houdini > File > Import > Houdini Digital Asset:

   ![image](https://user-images.githubusercontent.com/59757164/196758971-b4df2657-4671-4594-a917-bf081190f999.png)

3. In that window, select the Installer.hda and click "Install and Create"!

   ![image](https://user-images.githubusercontent.com/59757164/196759119-b83d2da3-bb2c-411e-9d4d-7b8af0d7ac2d.png)

4. Success!

   ![image](https://user-images.githubusercontent.com/59757164/196759185-7edf5855-574c-4d3b-b4b5-83b2c5fdd443.png)

   It will generate a JSON in your {HOUDINI_USER_PREF}/packages folder that allows houdini to treat this folder as a package!

   ![image](https://user-images.githubusercontent.com/59757164/196759456-65c2cfd0-6f14-4c63-9f9b-5c64723f97cf.png)


# To Uninstall:
Perform the same steps as above but with the Uninstaller.hda!

# To Test:

Add "WPN_Generator" into an obj context:

![image](https://user-images.githubusercontent.com/59757164/171493149-6c9ac786-f53e-4a3c-900a-8ff678ac1ccc.png)

Choose one of the TEST_PSDs included in this repo (under TEST_PSD folder)

![image](https://user-images.githubusercontent.com/59757164/171493304-e54555c6-c8a9-4c82-a657-7caf9ccc9fbb.png)

It should generate a renamed PSD, use that PSD to instance SIDE, CUTOUT, ADDON hdas as needed, and dynamically generate parms and link them!

You would see a nice interface + a somewhat normal looking model:

![image](https://user-images.githubusercontent.com/59757164/171493973-bc793129-4d97-4561-b91d-4926aec0a283.png)

You can now play around with the parms to get something out of it! (Or go with your creativity and use the TEST_PSDs as a template to draw up something you like)

Alternatively, you can test with these files! (Just open up and they should work after installing the package)
![image](https://user-images.githubusercontent.com/59757164/204879372-0d298656-e083-4e4a-8702-91a49cb3e6bb.png)

Various Renders of the files:

AK:
![AK](https://user-images.githubusercontent.com/59757164/204882246-91340fea-4579-423a-9fc3-fe02a085d986.png)
AK_Modded:
![AK_modify](https://user-images.githubusercontent.com/59757164/204882379-488ee9fb-70a5-4df4-930e-6bbe373335a5.png)
BattleRifle:
![BattleRifleV04](https://user-images.githubusercontent.com/59757164/204883788-8a911656-2879-4930-915b-b6f39275d3fd.png)
FutureCarbine:
![FutureCarbine](https://user-images.githubusercontent.com/59757164/204883863-82588d17-79a3-4463-a706-ec715e25f9cd.png)

