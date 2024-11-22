# GDAutoPatcher
Batch Script that can download downgraded Geometry Dash game files from 1.9-2.206
# Disclaimer
This is not piracy you still need to own the game for this to work also do not worry about save coruption as the files have the exe renamed so your game saves in a different folder just copy your save data over 
# This Script uses GDown
[GDown](https://github.com/wkentaro/gdown) must be installed to use this script as well as [Python](https://www.python.org) with pip to install it

# Usage
Start the script and type a version number to start downloading (also see additional options below) full list of available versions include, 1.93, 2.01, 2.113, 2.204, 2.206
After the download is done unzip the file and start the game then copy your save data over to the new folder created in the localappdata directory 
Consult the 'error' command in the script if you encounter issues 
Command | Description
--------| -----------
help | help
error | Provides troubleshooting steps
4GB | Used BEFORE a version number from 1.9-2.204 (no spaces) will result in the [4GB Patch](https://ntcore.com/4gb-patch) being automatically applied 
Geode | Used AFTER a version number from 2.204-2.206 (no spaces) will result in [Geode](https://geode-sdk.org) being automatically downloaded along with GD
ALL | Using this command will result in all available versions being downloaded
4GB2.204Geode | You can prob guess by looking at the command only available for 2.204 

More detalied instructions via the "help" command in the script 
