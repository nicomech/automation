##tests selenium base linux home

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib2

from loginFunctions import seleniumFF, seleniumPH

def checkPolycomHDX(IP="", loginSan="admin", passwordSan="l3sup11%3F"):

    myIP = IP

    myUrl = "https://" + myIP
    ##URL for http auth logging - specific to HDX codecs
    authUrl = "https://" + loginSan + ":" + passwordSan + "@" + myIP + "/a_oobweblanguage.htm"

    dicTmp = {}

    try:
        testWeb = urllib2.urlopen(myUrl, timeout = 5)
        dicTmp["ip"] = "ok"
    except:
        testWeb = None
        dicTmp["ip"] = "unreachable"

    #test2 = urllib.urlopen(urlNone)
    if testWeb:
        print testWeb.getcode()
        #IP_fetched = seleniumFF(url=myUrl, loginUrl=authUrl, login=loginSan, password=passwordSan)
        IP_fetched = seleniumPH(url=myUrl, loginUrl=authUrl, login=loginSan, password=passwordSan)
        if IP_fetched:
            print "login ok on IP : ", IP_fetched
            dicTmp["https"] = "ok"
        else:
            print "login ko on IP : ", IP_fetched, myIP
            dicTmp["https"] = "auth failed"
    else:
        print "no actions as IP is unreachable"
        dicTmp["https"] = "unreachable"

    return dicTmp

#checkPolycomHDX("X.X.X.X")
