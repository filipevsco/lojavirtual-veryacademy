import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.selenium  # marcador pytest 'selenium'
def test_dashboard_admin_Login(
    live_server, db_fixture_setup, chrome_navegador_instancia
):

    """
    Teste de login no admin Django.
    1. Pytest carrega 3 fixtures:
        - live_server: runserver do django. Através dele consegue a url da aplicação e concatena com "/admin/login/"
        - db_fixture_setup: insere os dados de superuser no DB para proporcionar teste pelo selenium.
        - chrome_navegador_instancia: cria instancia do navegador chrome pelo selenium
    """
    navegador = chrome_navegador_instancia

    navegador.get(("%s%s" % (live_server.url, "/admin/login/")))

    nome_usuario = navegador.find_element(By.NAME, "username")
    senha_usuario = navegador.find_element(By.NAME, "password")
    submit = navegador.find_element(By.XPATH, '//input[@value="Log in"]')

    nome_usuario.send_keys("admin")
    senha_usuario.send_keys("password")
    submit.send_keys(Keys.RETURN)

    assert "Site administration" in navegador.page_source
