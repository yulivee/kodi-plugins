# -*- coding: UTF-8 -*-

"""
 weblogin
 by Anarchintosh @ xbmcforums
 Copyleft (GNU GPL v3) 2011 onwards

 this example is configured for Fantasti.cc login
 See for the full guide please visit:
 http://forum.xbmc.org/showthread.php?p=772597#post772597


 USAGE:
 in your default.py put:

 import weblogin
 logged_in = weblogin.doLogin('a-path-to-save-the-cookie-to','the-username','the-password')

 logged_in will then be either True or False depending on whether the login was successful.
"""

import os
import re
import urllib,urllib2
import cookielib
import sys

### TESTING SETTINGS (will only be used when running this file independent of your addon)
# Remember to clear these after you are finished testing,
# so that your sensitive details are not in your source code.
# These are only used in the:  if __name__ == "__main__"   thing at the bottom of this script.
myusername = ''
mypassword = ''
#note, the cookie will be saved to the same directory as weblogin.py when testing


def check_login(source,username):
    
    #the string you will use to check if the login is successful.
    #you may want to set it to:    username     (no quotes)
    logged_in_string = 'Log Out'

    #search for the string in the html, without caring about upper or lower case
    if re.search(logged_in_string,source,re.IGNORECASE):
        return True
    else:
        return False

def getFormkey( source ):

    formkey_pattern = 'name="form_key" type="hidden" value="(\w+)"'
    match = re.search(formkey_pattern, source)
    formkey = match.group(1) if match else None

    if formkey:
        return formkey
    else:
        return False


def buildRequest(login_url, username, password, formkey):

    return (req, opener)
    

def doLogin(cookiepath, username, password):

    #check if user has supplied only a folder path, or a full path
    if not os.path.isfile(cookiepath):
        #if the user supplied only a folder path, append on to the end of the path a filename.
        cookiepath = os.path.join(cookiepath,'cookies.lwp')
        
    #delete any old version of the cookie file
    try:
        os.remove(cookiepath)
    except:
        pass

    if username and password:

        #the url you will request to.
        # First we fetch the login url. We have to extract a hidden field for the POST-Request
        login_url = 'https://daturaonline.com/customer/account/login/'

        #the header used to pretend you are a browser
        header_string = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'


        #build the GET request we will make
        req = urllib2.Request(login_url)

        #initiate the cookielib class
        jar = cookielib.LWPCookieJar()

        #install cookielib into the url opener, so that cookies are handled
        opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
            urllib2.HTTPSHandler(debuglevel=0),
            urllib2.HTTPCookieProcessor(jar)
        )

        opener.addheaders = [ ('User-Agent',header_string) ]

        preData = opener.open( req ).read()

        # Extract the hidden field (formkey) from the fetched request
        formkey = getFormkey(preData)
        if formkey == False :
            print "No Formkey retrieved"
            sys.exit(0)

        #build the form data necessary for the login
        login_data = urllib.urlencode(
            { 'login[username]':username, 'login[password]':password, 'form_key':formkey, 'send':'' }
        )

        # for the POST-Request we need to use another login-url.
        login_url = 'https://daturaonline.com/customer/account/loginPost/'
        new_request = urllib2.Request(login_url)
        new_request.add_data( login_data )


        #do the login and get the response
        try:  
            response = opener.open(new_request)
        except urllib2.URLError as e:
            if hasattr(e,'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
                sys.exit(0)
            elif hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
                sys.exit(0)
            
        source = response.read()
        response.close()

        #check the received html for a string that will tell us if the user is logged in
        #pass the username, which can be used to do this.
        login = check_login(source,username)

        #if login suceeded, save the cookiejar to disk
        if login == True:
            jar.save(cookiepath)

        #return whether we are logged in or not
        return login
    
    else:
        return False

#code to enable running the .py independent of addon for testing
if __name__ == "__main__":
    if myusername is '' or mypassword is '':
        print 'YOU HAVE NOT SET THE USERNAME OR PASSWORD!'
    else:
        logged_in = doLogin(os.getcwd(),myusername,mypassword)
        print 'LOGGED IN:',logged_in
