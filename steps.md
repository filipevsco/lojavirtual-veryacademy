# PASSO-A-PASSO PROJETO

### 1. DATABASE DESIGN

![DATABASE](https://user-images.githubusercontent.com/12896853/189552961-850ea950-0adf-46a7-bd27-1cf2b447acce.png)

### 2. INSTALAÇÃO INICIAL

1. Criado pasta do projeto `lojavirtual-veryacademy`;
2. Criando ambiente virtual [virtualenv](https://virtualenv.pypa.io/en/latest/)
3. Instalado django e iniciado um novo projeto `lojavirtual`;
4. Instalado pytest, pytest-django, pytest-factoryboy, pytest-selenium;
5. Gerado arquivo requirements.txt;
6. Criando um novo app `dashboard` (dentro da pasta do projeto);

### 3. PREPARAÇÃO DOS TESTES (TDD)

1. Criar uma pasta "tests" dentro da pasta `dashboard` e incluir arquivo `__init__.py`;
2. Crar o arquivo `test_selenium_dashboard`;

##### Pytest

1. Na pasta raiz do projeto criar o arquivo `pytest.ini`:
```
[pytest]
DJANGO_SETTINGS_MODULE = lojavirtual.setttings
python_files = test_*.py
```
2. Na pasta raiz do projeto criar o arquivo `conftest.py`;


#### SELENIUM

