from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Firefox()
driver = webdriver.PhantomJS('./phantomjs')
driver.get("http://www.copro-eco.fr/")
elem = driver.find_element_by_name("login")
elem.send_keys("copro@mechin.org")

elem = driver.find_element_by_name("pwd")
elem.send_keys("azerty")

elem.submit()

driver.close()