
import scrapy
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement




#start the spider
class RadwellSpider(scrapy.Spider):
    name = "Radwell"

    #fetch the intended URLs with automated web browser
    driver = webdriver.Chrome()
    driver.get('https://www.radwell.com/en-US/')
    time.sleep(2)
    listy = []

   

    grabs = driver.find_elements_by_xpath('//*[@id="nav"]/div/ul/li/a')
        for grab in grabs:
            href = grab.get_attribute('href')

            listy.append(href)
            
        start_urls = listy

    print(start_urls)
    
    #troubleshooting with print statements if necessary
    print ('you are here in the program')



    def parse(self, response):

        
        #extracting content using css extractors then put into dictionary 
        for tool in response.css('a.searchResult'):

            model_num = tool.css('h2.partnoi::text').extract()
            mfg = tool.css('h2.mfgri::text').extract()
            description = tool.css('p.desc.searchResulti::text').extract()
            price = tool.css('span.searchPr::text').extract()

            for item in zip(model_num, mfg, description, price):

                scraped_info = {

                    'model_num': item[0],
                    'mfg': item[1],
                    'description': item[2],
                    'price': item[3].strip(),
                }

                yield scraped_info





        




