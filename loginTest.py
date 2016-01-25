##tests selenium base linux home

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Stockholm
#myUrl = "https://87.60.87.90"
#Finland
#myUrl = "https://194.111.72.47"
#test
myUrl = "https://www.ebay.com"
driver = webdriver.Firefox()
#driver = webdriver.PhantomJS()
driver.get(myUrl)
#elem = driver.find_element_by_name("login")
#elem.send_keys("copro@mechin.org")

#elem = driver.find_element_by_name("pwd")
#elem.send_keys("azerty")

#elem.submit()

driver.close()