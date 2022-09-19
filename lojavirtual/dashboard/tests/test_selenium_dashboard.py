import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.selenium  # marcador pytest 'selenium'
def test_dashboard_admin_Login(
    live_server, db_fixture_setup, chrome_browser_instance
):

    """
    Teste de login no admin Django.
    1. Pytest carrega 3 fixtures:
        - live_server: runserver do django. Através dele consegue a url da aplicação e concatena com "/admin/login/"
        - db_fixture_setup: insere os dados de superuser no DB para proporcionar teste pelo selenium.
        - chrome_browser_instance: cria instancia do browser chrome pelo selenium
    """
    browser = chrome_browser_instance

    browser.get(("%s%s" % (live_server.url, "/admin/login/")))

    username = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, '//input[@value="Log in"]')

    username.send_keys("admin")
    password.send_keys("password")
    submit.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source
