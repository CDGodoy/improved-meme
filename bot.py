from ast import Or
from cgitb import text
from multiprocessing.connection import wait
import os.path
import time
import re
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
        #---------------LEMBRE-SE DE ALTERAR O CAMINHO DO WEBDRIVER-----------------
        self.driver = webdriver.Chrome(executable_path=r"C:\bin\chromedriver.exe")
    def truckPad(self):
        
        #Abrindo arquivo para salvar
        if os.path.exists("truckpad.csv"):
            arquivo = open("truckpad.csv", 'a')
        else:
            arquivo = open("truckpad.csv", 'a')
            arquivo.write("Origem,Destino,Veiculo,Carroceria,Peso,Preco,Data da Consulta\n")

        try:
            #Formato dos links
            #https://www.truckpad.com.br/fretes/
            #https://www.truckpad.com.br/fretes/carga-de-nome-da-cidade-uf/
            #https://www.truckpad.com.br/fretes/carga-de-nome-da-cidade-uf/para-nome-da-cidade-uf/
            site = 'https://www.truckpad.com.br/fretes/carga-de-sao-paulo-sp/para-sao-paulo-sp/'
            self.driver.get(site)
            self.driver.implicitly_wait(10)

            
            itensPagina = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/main/div[2]/h2').text
            itensPagina = itensPagina.split()
            itensPagina = int(itensPagina[0])
            if itensPagina <= 20:
                itensPagina = itensPagina
            else:
                paginas = itensPagina % 20
                itensPagina = 20

            for j in range(1, itensPagina + 1):
                
                origem = self.driver.find_element(By.XPATH, '//*[@id="freights"]/li['+str(j)+']/div[1]/div[1]/div[2]/p[1]/strong').text
                destino = self.driver.find_element(By.XPATH, '//*[@id="freights"]/li['+str(j)+']/div[1]/div[1]/div[2]/p[2]/strong').text
                veiculo = self.driver.find_element(By.XPATH, '//*[@id="freights"]/li['+str(j)+']/div[1]/div[2]/p[1]/strong').text
                carroceria = self.driver.find_element(By.XPATH, '//*[@id="freights"]/li['+str(j)+']/div[1]/div[2]/p[2]/strong').text
                peso = self.driver.find_element(By.XPATH, '//*[@id="freights"]/li['+str(j)+']/div[1]/div[3]/p[1]/strong').text
                preco = self.driver.find_element(By.XPATH, '//*[@id="freights"]/li['+str(j)+']/div[1]/div[3]/p[2]/strong[1]').text
                hora = datetime.strftime(datetime.now(), '%Y%m%d')
                
                arquivo.write(origem + ',' + destino + ',' + veiculo + ',' + carroceria + ',' + peso + ',' + preco  + ',' + hora + '\n')
                #DEBUG
                # print("-----------------------------------\n")

                # print("Origem: " + origem)
                # print("Destino: "+ destino)
                # print("Veiculo: "+ veiculo)
                # print("Carroceria: " + carroceria)
                # print("Peso: " + peso)
                # print("Preço: "+ preco)
                # print("Hora: "+ hora)

            self.driver.close()        
        except:
            self.driver.close()
        arquivo.close()