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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class newBot:
    
    def __init__(self, nome_bot):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        #---------------LEMBRE-SE DE ALTERAR O CAMINHO DO WEBDRIVER-----------------
        self.driver = webdriver.Chrome(executable_path=r"C:\bin\chromedriver.exe")
    
    
    def allItems(self):
        #Abrindo arquivo para salvar
        data = datetime.strftime(datetime.now(), '%d-%m-%Y')
        if os.path.exists("truckpad"+data+".csv"):
            arquivo = open("truckpad"+data+".csv", 'a')
        else:
            arquivo = open("truckpad"+data+".csv", 'w')
            arquivo.write('Origem;Destino;distancia;caminhoes;carroceria;rastreador;Carga Completa / Complemento;tipo de carregamento;natureza da carga;peso;valor;Frete(R$) por Km;Data da Consulta\n')
            # origem, destino, distancia, caminhoes, carroceria, rastreador, 
            # Carga Completa / Complemento,  tipo de carregamento, 
            # natureza da carga, peso, valor, Frete(R$) por Km

        try:
            site = 'https://www.truckpad.com.br/fretes/'
            self.driver.get(site)
            # self.driver.implicitly_wait(50)

            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="freights"]/li[1]/div[2]/div/a')))

            self.driver.find_element(By.XPATH, '//*[@id="freights"]/li[1]/div[2]/div/a').click()
            
            origem = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/aside/div/div[1]/p[1]/strong').text
            destino = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/aside/div/div[1]/p[2]/strong').text
            distancia = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/aside/div/p[2]/strong').text
            caminhoes = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/main/div[5]/div/section[1]/ul[1]').text
            carroceria = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/main/div[5]/div/section[1]/ul[2]').text
            rastreador = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/main/div[5]/div/section[2]/p[1]/strong').text
            cargaCompleta = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/main/div[6]/div/section[1]/p[2]/strong').text
            tipoDeCarga = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/main/div[6]/div/section[1]/p[3]/strong').text
            naturezaDaCarga = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/main/div[6]/div/section[2]/p[3]/strong').text
            peso = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/main/div[6]/div/section[2]/p[1]/strong').text
            valor = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/aside/div/p[1]/strong[1]').text
            fretePorKm = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/main/div[7]/div/section[1]/p[2]/strong').text

            print('Origem:', origem)
            print('Destino:', destino)
            print('Distancia:', distancia)
            print('Caminhoes:', caminhoes)
            print('Carroceria:', carroceria)
            print('Rastreador:', rastreador)
            print('cargaCompleta:', cargaCompleta)
            print('tipo de carga:', tipoDeCarga)
            print('Natureza da Carga:', naturezaDaCarga)
            print('Peso:', peso)
            print('valor:', valor)
            print('Frete por KM:', fretePorKm)
            

            self.driver.close()
        except:
            self.driver.close()
    
    
    
    def frontPage(self):
        
        #Abrindo arquivo para salvar
        if os.path.exists("truckpad.csv"):
            arquivo = open("truckpad.csv", 'a')
        else:
            arquivo = open("truckpad.csv", 'a')
            arquivo.write('"Origem";"Destino";"Veiculo";"Carroceria";"Peso";"Preço";"Data da Consulta"\n')

        try:
            #Formato dos links
            #https://www.truckpad.com.br/fretes/
            #https://www.truckpad.com.br/fretes/carga-de-nome-da-cidade-uf/
            #https://www.truckpad.com.br/fretes/carga-de-nome-da-cidade-uf/para-nome-da-cidade-uf/
            #https://www.truckpad.com.br/fretes/carga-de-nome-da-cidade-uf/para-nome-da-cidade-uf/?pagina=2
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
                hora = datetime.strftime(datetime.now(), '%Y/%m/%d')
                
                arquivo.write(origem + ';' + destino + ';' + veiculo + ';' + carroceria + ';' + peso + ';' + preco  + ';' + hora + '\n')

            self.driver.close()        
        except:
            self.driver.close()
        arquivo.close()