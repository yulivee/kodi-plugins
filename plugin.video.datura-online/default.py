import weblogin
import yaml


with open("resources/data/credentials.yml", 'r') as yamlfile:
    cfg = yaml.load(yamlfile)

logged_in = weblogin.doLogin('resources/data/',cfg['username'],cfg['password'])

if logged_in == True:
    print "Login Successful"
