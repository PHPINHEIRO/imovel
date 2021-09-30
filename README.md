<h1 align="center">Venda de Imoveis</h1>

<p align="center">Projeto para o processo seletivo de Dev full stack python na empresa <a href="http://strategibrasil.com.br/)">Strategi</a></p>

## Objetivo

Criar uma aplicação web para venda de imoveis


### Tecnologias

* Python
* Django
* Postgresql
* Docker / Docker-Compose
* Pipenv

## Executando a aplicação

#### Executando o container

```
docker-compose up -d
```

#### Executando as migracoes 

```
docker-compose exec web python manage.py migrate
```

#### Criando user admin

```
docker-compose exec web python manage.py createsuperuser
```

#### Parar a aplicação

```
docker-compose down
```

## Utilizando a aplicação

https://user-images.githubusercontent.com/5932141/135460157-19baad77-447a-4a53-b234-440df78bfe71.mp4
