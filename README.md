# WPN GENERATOR PACKAGE
 
WPN Generator OTL toolsets for Houdini FX 18.5.596 and Above!

Check out the short explainer here:

https://vimeo.com/716740961

Packaged to be easy-to-install thanks to Christian Akesson and his tutorial!
https://learncreategame.com/techart/houdini-environment-setup/



# To Install:

1. Download and Unzip into a folder of your choice!

   You should see the following structure:

   ![image](https://user-images.githubusercontent.com/59757164/196758728-d9c4990a-3a96-40b3-9391-f02a1b827443.png)

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

Feel free to fork this and make this project better! :)

# TODO:
- [ ] Refactor and Cleanup
- [ ] Fix geometry generation to be more reliable (instead of simply using booleans)
