import urllib2
import CommonFunctions
from urls import URL

kodi_common = CommonFunctions

get_categories()

def get_HTML(url):
    return urllib2.urlopen(url).read()

def get_categories():
    html = get_HTML(URL)
    parseDOM(html, ul, attrs={'class':'navigation clearFloat'})
