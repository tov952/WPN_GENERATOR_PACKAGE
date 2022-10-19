# WPN GENERATOR PY
 
This is the source for WPN_GENERATOR meant to work with the WPN Generator OTL toolsets for Houdini FX 18.5.596!



# Installation:

Download Jason-Houdini-OTls, unzip and "install Asset Library" into "Scanned Asset Library Directories":

https://github.com/tov952/Jason-Houdini-OTLs

![image](https://user-images.githubusercontent.com/59757164/171492255-1c51e0b6-452e-49a5-8905-a5bde1929bfe.png)


Download and unzip WPN_GENERATOR_PY into:
E:\Users\[YOURNAME]\Documents\houdini18.5\python3.7libs\WPN_GENERATOR_PY

![image](https://user-images.githubusercontent.com/59757164/171492792-9731bc25-1fc7-4441-953c-14323604d22e.png)

# To Test:

Add "WPN_Generator" into an obj context:

![image](https://user-images.githubusercontent.com/59757164/171493149-6c9ac786-f53e-4a3c-900a-8ff678ac1ccc.png)

Choose one of the TEST_PSDs included in this repo (under TEST_PSD folder)

![image](https://user-images.githubusercontent.com/59757164/171493304-e54555c6-c8a9-4c82-a657-7caf9ccc9fbb.png)

It should generate a renamed PSD, use that PSD to instance SIDE, CUTOUT, ADDON hdas as needed, and dynamically generate parms and link them!

You would see a nice interface + a somewhat normal looking model:

![image](https://user-images.githubusercontent.com/59757164/171493973-bc793129-4d97-4561-b91d-4926aec0a283.png)

You can now play around with the parms to get something out of it! (Or go with your creativity and use the TEST_PSDs as a template to draw up something you like)

**I'll properly package this whole thing in the future into one nice repo once more kinks are hammered out!**
