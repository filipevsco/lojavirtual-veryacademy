# PASSO-A-PASSO PROJETO

### 1. DATABASE DESIGN

![DATABASE](https://user-images.githubusercontent.com/12896853/189552961-850ea950-0adf-46a7-bd27-1cf2b447acce.png)

### 2. INSTALAÇÃO INICIAL

1. Criado pasta do projeto `lojavirtual-veryacademy`;
2. Criando ambiente virtual [virtualenv](https://virtualenv.pypa.io/en/latest/)
3. Instalado django e iniciado um novo projeto `lojavirtual`;
4. Instalado pytest, pytest-django, pytest-factoryboy, pytest-selenium;
5. Gerado arquivo requirements.txt;
6. Criando um novo app `dashboard` (dentro da pasta do projeto). Registrar no `settings.py` e corrigir `apps.py` (path);

### 3. PREPARAÇÃO DOS TESTES (TDD)

##### PYTEST

1. Na pasta raiz do projeto criar o arquivo `pytest.ini`:
```
[pytest]
DJANGO_SETTINGS_MODULE = lojavirtual.setttings
python_files = test_*.py
```
2. Na pasta raiz do projeto criar o arquivo `conftest.py`;
3. Na pasta raiz do projeto criar pasta `tests`;

#### SELENIUM

Objetivo de testar o login admin pelo navegador.

1. Criar uma pasta "tests" dentro da pasta `dashboard` e incluir arquivo `__init__.py`;
2. Crar o arquivo `test_selenium_dashboard.py` para implementar testes (necessita das _fixtures_ abaixo);
3. Baixar `ChromeDriver` (talvez seja necessário configurar PATH do SO);

#### FIXTURES
(@pytest.fixture)
Na pasta `/tests` criar arquivos:
  - `selenium.py` -> responável por criar instância do chrome browser;
  - `fixtures.py` -> Cria superuser(create_user_admin) e carregar **fixtures** de apps (db_fixture_setup); 


Registrar arquivos no arquivo `conftest.py`:
```
python_pluguins = [
  "lojavirtual.tests.selenium",
  "lojavirtual.tests.fixtures",
]
```
Em cada app criar pasta `/fixtures` e criar arquivo `db_*****_fixture.json` -> responsável por dados do db.

#### MARK
(`@pytest.mark.****`)

No arquivo `pytest.ini` registrar os **makerns**:

```
markers =
    selenium: selenium test
    dbfixture: database fixture tests
```

#### Inventory

1. Criar novo app inventory;
2. criar pasta tests dentro da pasta do app;
3. criar arquivo 
   'test_db_fixtures.py' -> testar db fixtures, insercao de dados (atraves de factoryboy)