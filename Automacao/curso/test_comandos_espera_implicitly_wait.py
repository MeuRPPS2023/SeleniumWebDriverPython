import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.implicitly_wait(12) #Espera os comandos estar visível e habilitado

browser.maximize_window()
browser.get("C:\Automacao\WebSites\Componentes.html")

buttonEspera = browser.find_element(By.ID, "buttonDelay")
buttonEspera.click()

novoCampo = browser.find_element(By.ID, "novoCampo")
novoCampo.is_displayed(), "Oculto!"
novoCampo.is_enabled(), "Disabilitado!"
novoCampo.send_keys("Válido!")

print("Visivel: ", novoCampo.is_displayed())

time.sleep(3)
browser.quit()