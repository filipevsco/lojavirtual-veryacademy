import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def chrome_navegador_instancia(request):
    """
    Provide a selenium webdriver instance
    """
    opcoes = Options()
    opcoes.headless = False
    navegador = webdriver.Chrome(options=opcoes)
    yield navegador
    navegador.close()
