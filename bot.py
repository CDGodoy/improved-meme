from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
            while i<5:

                elements = self.driver.find_element_by_class_name('freight-card')

                for elem in elements:
                    leitura = elem.get_attribute('innerText')
                    print(leitura)



        except:
            self.driver.close()