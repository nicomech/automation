#!/usr/bin/env python

#import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common import action_chains
from urllib import urlencode
import urllib2
import time

def seleniumFF(url="", loginUrl="", login="", password=""):
    ##web auth Firefox with special profile and credentials sent through URL
    profile = webdriver.FirefoxProfile()
    profile.set_preference('network.http.phishy-userpass-length', 255)
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.set_page_load_timeout(30)

    tabResult = []

    IPseen = "127.0.0.1"
    SN = "None"
    modele = "None"

    try:
        driver.get(loginUrl)
        driver.get(url)

        elem = driver.find_element_by_id("home_tools")
        elem.click()
        #driver.save_screenshot('img/screenshotFF-1.png')

        elem = driver.find_element_by_id("home_tools_info")
        elem.click()

        time.sleep(3)

        IPseen = driver.execute_script("return kIpAddress;")
        modele = driver.execute_script("return model;")

        driver.get(url)

        time.sleep(3)
        #driver.save_screenshot('img/screenshotPhantomJS-2.png')
        iframe = driver.find_element_by_id('contentFrame')
        #print "iframe : ", iframe
        driver.switch_to.frame(iframe)
        #print "switch done"
        SN = driver.find_element_by_id('serialnumbervalue').text
        #print "SN : ",SN

    except:
        #auth is failing : taking too much time
        pass

    driver.close()

    tabResult.append(IPseen)
    tabResult.append(SN)
    tabResult.append(modele)
    #print tabResult

    return tabResult

def seleniumBrowser(browser = "", url="", loginUrl="", login="", password=""):
    ##web auth Firefox with special profile and credentials sent through URL
    if browser == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.http.phishy-userpass-length', 255)
        driver = webdriver.Firefox(firefox_profile=profile)
    elif browser == "phantomjs":
        driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs-2', service_args=['--ignore-ssl-errors=true', '--web-security=no'])

    driver.set_page_load_timeout(30)

    tabResult = []

    IPseen = "127.0.0.1"
    SN = "None"
    modele = "None"

    try:
        driver.get(loginUrl)
        driver.get(url)

        elem = driver.find_element_by_id("home_tools")
        elem.click()
        #driver.save_screenshot('img/screenshotFF-1.png')

        elem = driver.find_element_by_id("home_tools_info")
        elem.click()

        time.sleep(3)

        IPseen = driver.execute_script("return kIpAddress;")
        modele = driver.execute_script("return model;")

        driver.get(url)

        #driver.save_screenshot('img/screenshotPhantomJS-2.png')
        iframe = driver.find_element_by_id('contentFrame')
        #print "iframe : ", iframe
        driver.switch_to.frame(iframe)
        #print "switch done"
        SN = driver.find_element_by_id('serialnumbervalue').text
        #print "SN : ",SN

    except:
        #auth is failing : taking too much time
        pass

    driver.close()

    tabResult.append(IPseen)
    tabResult.append(SN)
    tabResult.append(modele)
    #print tabResult

    return tabResult


def seleniumPH(url="", loginUrl="", login="", password=""):
    ##web auth PHJS
    driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs-2', service_args=['--ignore-ssl-errors=true', '--web-security=no'])
    #driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])

    driver.set_page_load_timeout(30)

    IPseen = "127.0.0.1"

    try:
        driver.get(loginUrl)
        driver.get(url)

        elem = driver.find_element_by_id("home_tools")
        elem.click()
        #driver.save_screenshot('img/screenshotFF-1.png')

        elem = driver.find_element_by_id("home_tools_info")
        elem.click()

        time.sleep(3)

        IPseen = driver.execute_script("return kIpAddress;")

        driver.get(url)

        time.sleep(3)
        #driver.save_screenshot('img/screenshotPhantomJS-2.png')
        iframe = driver.find_element_by_id('contentFrame')
        print "iframe : ", iframe
        driver.switch_to.frame(iframe)
        print "switch done"
        SN = driver.find_element_by_id('serialnumbervalue').text
        print "SN : ",SN

    except:
        #auth is failing : taking too much time
        pass

    driver.get(url)

    time.sleep(3)
    #driver.save_screenshot('img/screenshotPhantomJS-2.png')
    iframe = driver.find_element_by_id('contentFrame')
    print "iframe : ", iframe
    driver.switch_to.frame(iframe)
    print "switch done"
    SN = driver.find_element_by_id('serialnumbervalue').text
    print "SN : ",SN

    driver.close()

    return IPseen