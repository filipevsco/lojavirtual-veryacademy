import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.mark.selenium
def test_dashboard_admin_Login(live_server, db_fixture_setup, chrome_navegador_instancia):

    navegador = chrome_navegador_instancia

    navegador.get(("%s%s" % (live_server.url, "/admin/login/")))

    nome_usuario = navegador.find_element(By.NAME, "username")
    senha_usuario = navegador.find_element(By.NAME, "password")
    submit = navegador.find_element(By.XPATH, '//input[@value="Log in"]')

    nome_usuario.send_keys("admin")
    senha_usuario.send_keys("password")
    submit.send_keys(Keys.RETURN)

    assert "Site administration" in navegador.page_source