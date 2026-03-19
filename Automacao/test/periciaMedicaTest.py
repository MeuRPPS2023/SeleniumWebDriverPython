import time
import pytest

from page.periciaMedicaPO import LoginPage
from selenium import webdriver

@pytest.fixture
def setup():
    pm = webdriver.Chrome()
    pm.maximize_window()
    pm.get("http://proxima2.sisprevweb.com.br/estado_01/pericia/Login/Login.aspx")
    page = LoginPage(pm)
    yield pm, page        # ← entrega pm e page para os testes
    time.sleep(5)
    pm.quit()             # ← fecha o Chrome após CADA teste

# ✅ Opção 1 — usando == False
# assert relembrar.is_displayed() == False, "Elemento deveria estar oculto!"

# ✅ Opção 2 — usando not (mais pythônico)
# assert not relembrar.is_displayed(), "Elemento deveria estar oculto!"

# ✅ Verifica que está visível
# assert relembrar.is_displayed() == True, "Elemento não está visível!"

def test_TC001_validarTitulos(setup):
    pm, page = setup
    assert pm.title == "Pericia | Login", f"Errado! Encontrado: '{pm.title}'"
    assert page.tituloLogin().text == "Perícia Médica", f"Errado! Encontrado: '{page.tituloLogin().text}'"

def test_TC002_validarCamposLogin(setup):
    pm, page = setup
    page.buttonLogin().is_displayed(), "Não!"
    page.buttonLogin().is_enabled(), "Não!"
    page.buttonLogin().click()
    assert page.toastTitulo().text == "Atenção!", f"Encontrado: '{page.toastTitulo().text}'"
    assert page.toastMensagem().text == "Esse usuário não pertence ao grupo Perícia Médica!", f"Encontrado: '{page.toastMensagem().text}'"

def test_TC003_efetuarLogin(setup):
    pm, page = setup
    page.username().send_keys(page.login)
    page.password().send_keys(page.senha)
    page.buttonLogin().click()