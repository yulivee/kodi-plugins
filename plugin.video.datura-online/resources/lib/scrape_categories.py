import urllib2
import CommonFunctions
from urls import URL

kodi_common = CommonFunctions
kodi_common.dbg = True
common.dbglevel = 3

get_categories()

def get_HTML(url):
    return urllib2.urlopen(url).read()

def get_categories():
    html = get_HTML(URL)
    footer = kodi_common.parseDOM(html, ul, attrs={'class':'navigation clearFloat'})
    kodi_common.log(footer)

