from ast import Or
from cgitb import text
from multiprocessing.connection import wait
import os
import time
import re
import json
from datetime import datetime
from numpy import obj2sctype
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
            

            itensPagina= 20
            for j in range(1, int(itensPagina)):
                print("Entrou no for")
                
                origem = self.driver.find_element(By.XPATH, '//*[@id="freights"]/li['+str(j)+']/div[1]/div[1]/div[2]/p[1]/strong').text
                destino = self.driver.find_element(By.XPATH, '//*[@id="freights"]/li['+str(j)+']/div[1]/div[1]/div[2]/p[2]/strong').text
                veiculo = self.driver.find_element(By.XPATH, '//*[@id="freights"]/li['+str(j)+']/div[1]/div[2]/p[1]/strong').text
                carroceria = self.driver.find_element(By.XPATH, '//*[@id="freights"]/li['+str(j)+']/div[1]/div[2]/p[2]/strong').text
                peso = self.driver.find_element(By.XPATH, '//*[@id="freights"]/li['+str(j)+']/div[1]/div[3]/p[1]/strong').text
                preco = self.driver.find_element(By.XPATH, '//*[@id="freights"]/li['+str(j)+']/div[1]/div[3]/p[2]/strong[1]').text

                # print("Origem: " + origem)
                # print("Destino: "+ destino)
                # print("Veiculo: "+ veiculo)
                # print("Carroceria: " + carroceria)
                # print("Peso: " + peso)
                # print("Preço: "+ preco)
        except:
            self.driver.close()