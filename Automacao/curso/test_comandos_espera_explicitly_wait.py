import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #Necessário para usar wait
from selenium.webdriver.support import expected_conditions as EC #Necessário para usar wait

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("C:\Automacao\WebSites\Componentes.html")

wait = WebDriverWait(browser, 20) #Necessário declarar wait

buttonEspera = browser.find_element(By.ID, "buttonDelay")
buttonEspera.click()

#novoCampo1 = wait.until(EC.visibility_of_element_located((By.ID, "novoCampo"))) Aguarda o elemento ficar visível
#novoCampo1 = wait.until(EC.invisibility_of_element_located((By.ID, "novoCampo"))) Aguarda o elemento sumir

novoCampo1 = wait.until(EC.visibility_of_element_located((By.ID, "novoCampo")))
assert novoCampo1.is_displayed(), "Oculto!"
assert novoCampo1.is_enabled(), "Disabilitado!"
novoCampo1.send_keys("Válido!")
wait.until_not(EC.invisibility_of_element_located((By.ID, "novoCampo")))

time.sleep(3)
browser.quit()