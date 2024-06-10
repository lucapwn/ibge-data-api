# IBGE Data API

API para consumir e disponibilizar dados dos municípios brasileiros fornecidos pelo IBGE.

![Badge](https://img.shields.io/static/v1?label=license&message=MIT&color=1E90FF)
![Badge](https://img.shields.io/static/v1?label=build&message=passing&color=00d110)

## Conteúdo

- [Sobre](#sobre)
  - [Funcionalidades](#funcionalidades)
  - [Endpoints da API](#endpoints-da-api)
  - [Filtros](#filtros)
  - [Exemplos](#exemplos)
- [Executando a aplicação](#executando-a-aplicação)
  - [Conteinerizando a aplicação](#conteinerizando-a-aplicação)
- [Autor](#autor)
- [Licença](#licença)

## Sobre

O IBGE Data API é uma interface desenvolvida com o framework [FastAPI](https://fastapi.tiangolo.com/) que permite obter os dados de todos os municípios brasileiros fornecidos pela [API de Localidades do IBGE](https://servicodados.ibge.gov.br/api/docs/localidades#api-Municipios-municipiosGet).

Assista este vídeo de exemplo no YouTube em [```https://www.youtube.com/watch?v=AMdGk-LIUu8```](https://www.youtube.com/watch?v=AMdGk-LIUu8).

![ibge-data-api](https://github.com/lucapwn/ibge-data-api/assets/58787069/f1b2c95f-3242-4a21-9c48-634b8a391fd8)

### Funcionalidades

Os usuários podem obter todas as informações sobre os municípios brasileiros, assim como filtrar os dados por nome do município, região, mesorregião, microrregião, UF e ordenar os dados por cada um dos atributos mencionados. Além disso, também é possível ordenar as informações de ordem crescente e decrescente.

### Endpoints da API

Método | Endpoint                        | Descrição
-------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------
GET    | ```/api/v1/municipalities```    | Obtém as informações de todos os municípios e permite uso de filtros.
GET    | ```/api/v1/municipality/{id}``` | Obtém as informações de um município específico pelo ID.

### Filtros

Filtro            | Descrição
------------------|---------------------------------------------------------
```id```          | ID do município.
```name```        | Nome do município ou caracteres iniciais.
```region```      | Região do município.
```mesoregion```  | Mesorregião do município.
```microregion``` | Microrregião do município.
```state```       | Estado (UF) do município.
```order_by```    | Ordena as informações por um atributo específico.
```descending```  | Ordena as informações por ordem crescente ou decrescente.

### Exemplos

Consultando por cada um dos atributos:

~~~console
foo@bar:~$ curl -X 'GET' 'http://localhost:8000/api/v1/municipality/3304557' -H 'accept: application/json'
foo@bar:~$ curl -X 'GET' 'http://localhost:8000/api/v1/municipalities' -H 'accept: application/json'
foo@bar:~$ curl -X 'GET' 'http://localhost:8000/api/v1/municipalities?name=Brasília' -H 'accept: application/json'
foo@bar:~$ curl -X 'GET' 'http://localhost:8000/api/v1/municipalities?region=Nordeste' -H 'accept: application/json'
foo@bar:~$ curl -X 'GET' 'http://localhost:8000/api/v1/municipalities?mesoregion=Campinas' -H 'accept: application/json'
foo@bar:~$ curl -X 'GET' 'http://localhost:8000/api/v1/municipalities?microregion=Ibiapaba' -H 'accept: application/json'
foo@bar:~$ curl -X 'GET' 'http://localhost:8000/api/v1/municipalities?state=CE' -H 'accept: application/json'
~~~

Mesclando os atributos:

~~~console
foo@bar:~$ curl -X 'GET' 'http://localhost:8000/api/v1/municipalities?name=Santo&mesoregion=Campinas&order_by=name&descending=false' -H 'accept: application/json'
~~~

## Executando a aplicação

Com o Git instalado, clone o repositório do projeto:

~~~console
foo@bar:~$ git clone https://github.com/lucapwn/ibge-data-api.git
~~~

Com o Python instalado, navegue até o diretório do projeto e instale as dependências da aplicação:

~~~console
foo@bar:~$ pip install -r requirements.txt
~~~

Execute o servidor da aplicação:

~~~console
foo@bar:~$ fastapi run
~~~

### Conteinerizando a aplicação

Com o Docker instalado, se necessitar realizar a conteinerização da aplicação, construa a imagem do contêiner:

~~~console
foo@bar:~$ docker build -t ibge-data-api .
~~~

Por fim, execute o contêiner da aplicação:

~~~console
foo@bar:~$ docker run -d -p 8000:8000 ibge-data-api
~~~

Você poderá acessar a documentação Swagger da aplicação em seu computador em [```http://localhost:8000/docs```](http://localhost:8000/docs).

## Autor

Desenvolvido por [Lucas Araújo](https://github.com/lucapwn).

## Licença

Esse software é licenciado pelo [MIT](https://choosealicense.com/licenses/mit/).
