import xbmc, xbmcaddon
import weblogin
import yaml
import CommonFunctions

common = CommonFunctions
logged_in = False


#with open("resources/data/credentials.yml", 'r') as yamlfile:
#    cfg = yaml.load(yamlfile)
#
#logged_in = weblogin.doLogin('resources/data/',cfg['username'],cfg['password'])
#
#if logged_in == True:
#    print "Login Successful"

def get_credentials ():
    with open("resources/data/credentials.yml", 'r') as yamlfile:
        cfg = yaml.load(yamlfile)

    return cfg['username'], cfg['password']

def Notify ( title, message, times, icon ) :
    xbmc.executebuiltin("XBMC.Notification("+title+","+message+","+times+","+icon+")")

def Login ( username, password, hidesuccess ) :
    uc = username[0].upper() + username[1:]
    lc = username.lower

    logged_in = weblogin.doLogin(__datapath__,username,password)
    if logged_in == True:
        avatar = get_avatar(lc)

def addDir(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok
def addLink(name,url,iconimage):
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
    return ok

 main_menu () :
    if logged_in == False:
        addDir("Sign In")


