from ast import Or
from multiprocessing.connection import wait
import os
import time
import re
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from collections import Counter as cnt
from selenium.webdriver.common.by import By

class newBot:
    
    def __init__(self, nome_bot):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(executable_path=r"C:\bin\chromedriver.exe")
    
    def truckPad(self):
        
        try:
            site = 'https://www.truckpad.com.br/fretes/'
            self.driver.get(site)
            self.driver.implicitly_wait(10)

            origens = []
            
            i=0

            elements = self.driver.find_elements_by_class_name('freight-card')

            for elem in elements:
                # leitura = elem.find_element_by_class_name('information-content').text
                # print(leitura)
                leitura = elem.find_element(By.CLASS_NAME, 'information-content').text
                print(leitura)
            


            # while i<5:

            #     elements = self.driver.find_element_by_class_name('freight-card')

            #     for elem in elements:
            #         print("Entrou no for")
            #         leitura = elem.get_attribute('innerText')
            #         print(leitura)


            #     i+=1
        except:
            self.driver.close()