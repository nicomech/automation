##tests selenium base linux home

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib2

from loginFunctions import seleniumFF, seleniumPH, seleniumBrowser

def checkPolycomHDX(IP="", loginSan="", passwordSan=""):

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
        #tabResult = seleniumFF(url=myUrl, loginUrl=authUrl, login=loginSan, password=passwordSan)
        tabResult = seleniumBrowser(browser = "firefox", url=myUrl, loginUrl=authUrl, login=loginSan, password=passwordSan)
        #IP_fetched = seleniumPH(url=myUrl, loginUrl=authUrl, login=loginSan, password=passwordSan)
        if tabResult[1] != "None":
            print "login ok on IP : ", tabResult[0]
            dicTmp["https"] = "ok"
            dicTmp["SN"] = tabResult[1]
            dicTmp["model"] = tabResult[2]
        else:
            print "login ko on IP : ", tabResult[0], myIP
            dicTmp["https"] = "auth failed"
            dicTmp["SN"] = "None"
            dicTmp["model"] = "None"
    else:
        print "no actions as IP is unreachable"
        dicTmp["https"] = "unreachable"
        dicTmp["SN"] = "None"
        dicTmp["model"] = "None"

    return dicTmp

#checkPolycomHDX("X.X.X.X")
