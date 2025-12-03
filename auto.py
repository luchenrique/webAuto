from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())


navegador = webdriver.Chrome(service=servico)

navegador.get("https://docs.google.com/forms/d/e/1FAIpQLSe8FPkMAr5tG4OzWtidLGZNX7NrmRg-uQ1QR8eq37S9yZ7YTQ/viewform?usp=dialog")
navegador.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Lucas")


input("Pressione ENTER para sair...")