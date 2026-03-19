import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 10)

    # Declaração dos elementos
    def username(self):
        return self.driver.find_element(By.ID, "txtLogin")

    def password(self):
        return self.driver.find_element(By.ID, "txtSenha")

    def buttonLogin(self):
        return self.driver.find_element(By.ID, "btnLogin")

    def tituloLogin(self):
        return self.driver.find_element(By.LINK_TEXT, "Perícia Médica")

    def toastTitulo(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-title")))

    def toastMensagem(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))

    login = "1340"
    senha = "fgh38a"