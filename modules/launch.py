import subprocess
import os
import config
USERPROFILE=os.environ['USERPROFILE']
APPDATA=os.environ['APPDATA']
def Launch(Version):
    Java_Path=config.ConfigRead(Version,"Java_Path")
    Directory=config.ConfigRead(Version,"Directory")
    Cosmetics=config.ConfigRead(Version,"Cosmetics")
    Arguments = config.ConfigRead(Version,"Arguments_List")
    if Version=="1.7":
        AssetIndex="1.7.10"
    else:
        AssetIndex=Version
    if Cosmetics=="On":
        Cosmetics_Path=USERPROFILE+"\\.lunarclient\\textures"
    else:
        Cosmetics_Path=" "
    subprocess.Popen([Java_Path,
                     "--add-modules",
                    "jdk.naming.dns",
                     "--add-exports",
                    "jdk.naming.dns/com.sun.jndi.dns=java.naming",
                     "-Djna.boot.library.path="+USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\natives",
                     "--add-opens",
                    "java.base/java.io=ALL-UNNAMED",
                     "-Djava.library.path="+USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\natives",
                     "-cp",
                     USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\lunar-assets-prod-1-optifine.jar;"
                      +USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\lunar-assets-prod-2-optifine.jar;"
                      +USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\lunar-assets-prod-3-optifine.jar;"
                      +USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\lunar-libs.jar;"
                      +USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\lunar-prod-optifine.jar;"
                      +USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\OptiFine.jar;"
                      +USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\vpatcher-prod.jar",
                     "com.moonsworth.lunar.patcher.LunarMain",
                    "--version",
                      str(Version),
                    "--accessToken",
                      "0", 
                    "--assetIndex",
                      str(AssetIndex),
                    "--userProperties",
                      "{}",
                    "--gameDir",
                      Directory,
                     "--width",
                      "854",
                    "--height",
                      "480",
                      "--texturesDir",
                      Cosmetics_Path,
                      "--assetsDir",
                      APPDATA+"\\.minecraft\\assets"]+Arguments) 
                     
                 