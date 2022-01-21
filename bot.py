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
            itensPagina= 20
            for j in range(1, int(itensPagina)):
                print("Entrou no for")
                
                origem = self.driver.find_element(By.XPATH, '//*[@id="freights"]/li['+str(j)+']/div[1]/div[1]/div[2]/p[1]/strong').text
                destino = self.driver.find_element(By.XPATH, '//*[@id="freights"]/li['+str(j)+']/div[1]/div[1]/div[2]/p[2]/strong').text


                print("Origem: "+ origem)
                print("Destino: " + destino)




            
        except:
            self.driver.close()

        # //*[@id="freights"]/li[1]/div[1]/div[1]/div[2]/p[1]/strong

        # /html/body/div[1]/div[1]/div[3]/main/div[3]/ul/li[1]/div[1]/div[1]/div[2]/p[1]/strong
        # //*[@id="freights"]/li[1]/div[1]/div[1]/div[2]/p[1]/strong

        # /html/body/div[1]/div[1]/div[3]/main/div[3]/ul/li[1]/div[1]/div[1]/div[2]/p[2]/strong
        # //*[@id="freights"]/li[1]/div[1]/div[1]/div[2]/p[2]/strong

        # /html/body/div[1]/div[1]/div[3]/main/div[3]/ul/li[2]/div[1]/div[1]/div[2]/p[1]/strong
        # //*[@id="freights"]/li[2]/div[1]/div[1]/div[2]/p[1]/strong

        # /html/body/div[1]/div[1]/div[3]/main/div[3]/ul/li[2]/div[1]/div[1]/div[2]/p[2]/strong
        # //*[@id="freights"]/li[2]/div[1]/div[1]/div[2]/p[2]/strong