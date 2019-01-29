import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement




class God:


    def theStart(self):
        driver = webdriver.Chrome()
        driver.get('https://www.radwell.com/en-US/')
        time.sleep(2)

        listy = []


        #list_length = driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li').length

        grabs = driver.find_elements_by_xpath('//*[@id="nav"]/div/ul/li/a')
        for  grab in grabs:
            href = grab.get_attribute('href')


            listy.append(href)




        return listy;



