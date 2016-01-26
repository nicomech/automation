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

    except:
        #auth is failing : taking too much time
        pass

    driver.close()

    return IPseen


def seleniumPH(url="", loginUrl="", login="", password=""):
    ##web auth PHJS
    driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs-2', service_args=['--ignore-ssl-errors=true'])
    #driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])

    driver.set_page_load_timeout(30)

    IPseen = "127.0.0.1"

    try:
        driver.get(loginUrl)
        driver.get(url)

        #driver.save_screenshot('img/screenshotPhantomJS-1.png')

        elem = driver.find_element_by_id("home_tools")
        elem.click()
        #driver.save_screenshot('img/screenshotFF-1.png')

        elem = driver.find_element_by_id("home_tools_info")
        elem.click()

        time.sleep(3)
        #driver.save_screenshot('img/screenshotPhantomJS-2.png')
        IPseen = driver.execute_script("return kIpAddress;")

    except:
        #auth is failing : taking too much time
        pass

    driver.close()

    return IPseen