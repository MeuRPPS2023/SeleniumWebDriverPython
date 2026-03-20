import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 10)
        self.login = "1340"
        self.senha = "fgh38a"

    # Declaração dos elementos
    def username(self):
        return self.driver.find_element(By.ID, "txtLogin")

    def password(self):
        return self.driver.find_element(By.ID, "txtSenha")

    def buttonLogin(self):
        return self.driver.find_element(By.ID, "btnLogin")

    def tituloLogin(self):
        return self.driver.find_element(By.LINK_TEXT, "Perícia Médica")
    
    def acessarModuloConfiguracoes(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "liConfiguracoes")))
    
    def acessarMenuGruposPermissoes(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "liGrupoPermissoes")))
    
    def validarTituloGrupoPermissoes(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Grupos - Permissões']")))

    def buttonNovoGrupoPermissoes(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "btnNovo")))
    
    def modalCadastroGruposPermissao(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "modalcadastronome1")))
    
    def campoNomeGrupo(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_txtNomeGrupo")))
    
    def buttonSalvarCadastroGrupo(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "btnSalvarDocumento")))
    
    def linhaGrupoPermissao(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(),'Automação')]")))
    
    # Editar Permissão de Grupo Permissões
    def buttonEditarGrupoPermissao(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//tr[td[contains(.,'Automação')]]//a[contains(@class,'editor_edit')]")))
    
    def buttonExcluirGrupoPermissao(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//tr[td[contains(.,'Automação')]]//a[contains(@class,'editor_remove')]")))
    
    def buttonPermissoesGrupoPermissao(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//tr[td[contains(.,'Automação')]]//a[contains(@class,'editor_perm')]")))

    #-------------------------------------------------------------------------------------------------#
    #Validar mensagem de erro ou sucesso
    def toastTitulo(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-title")))

    def toastMensagem(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))

    def toastTituloOculto(self):
        return self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "toast-title")))

    def toastMensagemOculto(self):
        return self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "toast-message")))

    #Métodos
    def efetuarLogin(self):
        self.username().send_keys(self.login)
        self.password().send_keys(self.senha)
        self.buttonLogin().click()