@Echo off
title GD AutoPatcher

:Echo
Echo.
Echo GD AutoPatcher type 'help' for list of commands
Echo Type 'error' if you encounter issues 
Echo.
REM help. 
REM error.

REM A lot of options there
REM --------------------------------------------------
REM 1.9. Download 1.9
REM 2.0. Download 2.0
REM 2.11. Download 2.11
REM 2.204. Download 2.204
REM 2.206. Download 2.206
REM -----------------------------------
REM 4GB1.9. Download 1.9 4GB Patch
REM 4GB2.0. Download 2.0 4GB Patch
REM 4GB2.11. Download 2.11 4GB Patch
REM 4GB2.204. Download 2.204 4GB Patch
REM 4GB2.206. Download 2.206 4GB Patch
REM -----------------------------------
REM 1.9Geode. Download 1.9 Geode
REM 2.0Geode. Download 2.0 Geode
REM 2.11Geode. Download 2.11 Geode
REM 2.204Geode. Download 2.204 Geode
REM 2.206Geode. Download 2.206 Geode
REM -----------------------------------
REM 4GB2.204Geode. Download 2.204 4GB Patch w/ Geode
REM --------------------------------------------------

REM way too fucking long help command jesus christ
set /p a=
IF %a%==help (Echo "1.9" Downloads 1.9,
Echo "2.0" Downloads 2.0,
Echo "2.11" Downloads 2.11,
Echo "2.204" downloads 2.204,
Echo "2.206" Downloads 2.206,
Echo ADDITIONAL: Using "4GB" before any download command will result in the 4GB patch being automatically applied As long as it is NOT a version AFTER 2.204 eg: "4GB2.11",
Echo Using "Geode" after any download command will result in Geode being automatically downloaded along with gd as long as it's NOT a version BEOFRE 2.204 eg: "2.206Geode",
Echo Both arugments can be used inbetween the version number and will result in the 4GB patch being automatically applied as well as Geode this is only available for 2.204 eg: "4GB2.204Geode",
Echo "ALL" will result in every unmodded version of gd being downloaded from 1.9-2.206
GOTO Echo)

REM Error troubleshoot 
IF %a%==error (Echo If the console closed after tpying a command you either don't have gdown installed instructions are on the github
Echo Or you typed the command wrong this is CaSe-SenSiTive or you typed a command that doesn't exist type 'help' for the list of commands
Echo If the game didn't start then you're pirating or you didn't have steam oppened 
Echo Try running GD as Admin see if that fixes it
Echo If the zip file was unable to download then there might be an issue with the google drive contact realshadow69 on discord in this case
Echo If all else fails just download the zip files from the google drive that this is being downloaded from: https://drive.google.com/drive/folders/1kusyH0-15UvrJCqLAhBfJn2YyQDPQb9z?usp=drive_link
Echo Or use the Steam Console or Steam Depot Downloader to get the files
GOTO Echo)

REM --------------------------------------------------------------

REM I need to find some way other then gdown to download these
IF %a%==1.9 (Echo Download starting please wait...
gdown 1y1O9WxcXU0aSHo9yggYm8EHN0Igvg9-I
Echo Download finished
Echo in the case of an error restart the tool and type 'error'
pause)

IF %a%==2.0 (Echo Download starting please wait...
gdown 1ZY749tBKNbvcdPZT3QynX5HvxFMetBGO
Echo Download finished
Echo in the case of an error restart the tool and type 'error'
pause)

IF %a%==2.11 (Echo Download starting please wait...
gdown 1HYp696x0QB1U38HYpeB1l9qLEOOmMyI8
Echo Download finished
Echo in the case of an error restart the tool and type 'error'
pause)

IF %a%==2.204 (Echo Download starting please wait...
gdown 1d-4YYA5CXw-FF3BFksHRGNsis7YujeUL
Echo Download finished
Echo in the case of an error restart the tool and type 'error'
pause)

IF %a%==2.206 (Echo Download starting please wait...
gdown 18XWf9PaG9IJT8FbpOLQaKw4M6gigHysD
Echo Download finished
Echo in the case of an error restart the tool and type 'error'
pause)

REM ----
IF %a%==4GB1.9 (Echo Download starting please wait...
gdown 1R7VhR4Y8FrTorTpTJm8rJx-m8wy0NwkE
Echo Download finished
Echo in the case of an error restart the tool and type 'error'
pause)

IF %a%==4GB2.0 (Echo Download starting please wait...
gdown 1saO1D5pp6s9V0Iw7zkPlP7L9aw8uryrp
Echo Download finished
Echo in the case of an error restart the tool and type 'error'
pause)

IF %a%==4GB2.11 (Echo Download starting please wait...
gdown 1y0j3_rPWcuVxHJWw9ROcmgPTi8YxtHlY
Echo Download finished
Echo in the case of an error restart the tool and type 'error'
pause)

IF %a%==4GB2.204 (Echo Download starting please wait...
gdown 1ZarpTnCG-wbrDWVOEgk3lCR6aJC4puyV
Echo Download finished
Echo in the case of an error restart the tool and type 'error'
pause)
REM ----

IF %a%==2.204Geode (Echo Download starting please wait...
gdown 1IgqttHt-xz7Xda_8OdvMnY6uxho9gD6v
Echo Download finished
Echo in the case of an error restart the tool and type 'error'
pause)

IF %a%==2.206Geode (Echo Download starting please wait...
gdown 1vj2V9BiaKQtf1TtbKnZ8dmAXsO6Gj1aZ
Echo Download finished
Echo in the case of an error restart the tool and type 'error'
pause)
REM ---

IF %a%==4GB2.204Geode (Echo Download starting please wait...
gdown 1snhxxPHsFdAmJP8hc49v-eiGUSYf9FpG
Echo Download finished
Echo in the case of an error restart the tool and type 'error'
pause)
REM ---

IF %a%==ALL (Echo Download starting please wait...
gdown 1tEp1WMeq70_nugGVWuAvJQw9P1_k3K9S
Echo Download finished
Echo in the case of an error restart the tool and type 'error'
pause)

REM --------------------------------------------------------------
REM E
