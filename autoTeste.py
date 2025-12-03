from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)

driver.get("https://google.com")
input("Pressione ENTER para sair...")
