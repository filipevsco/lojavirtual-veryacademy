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


#### INVENTORY

1. Criar novo app inventory;
2. criar pasta `/tests` dentro da pasta do app;
3. criar arquivo `test_db_fixtures.py` -> testar db_fixtures, inserção de dados (através de factoryboy)


#### FACTORY BOY
plugin para fabricar dados automaticamente com o objetivo de "popular" o banco de dados (principalmente para testes)


#### MPPT 
[Modified Preorder Tree Traversal]
MPTT é uma técnica para armazenar dados hierárquicos em um banco de dados. O objetivo é tornar as operações de recuperação muito eficientes.


#### LOADING DATA FIXTURES 

Criando um comando personalizado.

1. Criar um novo app django. Nesse caso nomeado como `demo`;
2. Excluir arquivos inúteis como: `views.py`, `tests.py`, `models.py` e `admin.py`;
3. Criar novas pastas dentro da pasta `demo` nomeada como `/management/commands/`;
4. Criar arquivo `load-fixtures.py` dentro da pasta commands -> Dentro deste arquivo poderemos configurar uma 
sequência de comandos que queremos executar ao digitar `> python manage.py load-fixtures`
  Dentro deste arquivo devemos importar a função `call-command` de django.core.management e
  importar também a classe `BaseCommand`;
5. Criamos a classe Command herdando de BaseCommand para chamar todas os comandos que queremos rodar.


#### SEQUÊNCIA DE DESENVOLVIMENTO (TDD)

##### 1. CONSTRUÇÃO DOS TESTES:
  Em `test_db_fixtures.py` elaboramos alguns testes:

      a - teste de consulta do bando de dados: o db será populado com os dados `.json` (somente durante o teste = "Session") e através do **parametrize** verificamos se coincidem com o esperado. 

      b - teste de inserção de dados: com a ferramenta `factory` criamos dados e testamos a inserção no db verificamo se os mesmo estão persistindo.

      c - teste de atributo unico (uniqueness): tentamos inserir duas vezes um atributo unico esperando a mensagem de erro.

  Após a elaboração dos testes, precisamos construir as **factories** e arquivos `json`necessários para realização dos testes.

  Em seguida, construímos nossos models e realizamos os testes. 


  #### Product Filter Prototype (part 3)

Consultas básicas e complexas no bando de dados.

- annotate
- distinct
- 


### POSTGRESQL via DOCKER

1. Criado arquivo `docker-compose.yml` na raiz do projeto. Este arquivo será um script responsável para dizer ao docker instalar o banco de dados postgresql.
2. para roda basta digitar no shell `docker compose up`


### ELASTICSEARCH (part 4)

Ferramenta especializada em consulta em banco de dados focada em desempenho. Permite pesquisar e analizar grande volume de dados.
Ela trabalha criando indices(index) a partir dos tipos de dados apra otimizar as consulta aos dados.

((((index) shard) node ) Cluster)

- Index -> Coleção de documentos que tem características semelhantes; (precisa ser unico - unique name);
- Shard -> È a capacidade de dividir um indice em fragmentos menores;
- Node -> É um unico servidor/instancia do elasticsearc que faz parte de um cluster;
- Cluster -> Composto por um ou mas nós, cada cluster um um unico atctive master node;

(Esta API é escrita em JAVA, portanto usa JVM.)



#### Implementação

Para este projeto criaremos outro container docker para hospedar a API Elasticsearch:
- No arquivo `docker-compose.yml` preencher os dados do servidor elasticsearch que será carregado no docker.

- Instalar o pacote via terminal: `pip install django-elasticsearch-dsl` (nao esquecer de incluir nos app do settings.py);
-rodar o docker para ver se funcionou corretamente;