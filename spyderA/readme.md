## Difficulty Level (1-easy to 5-hard)

2

## Environment

mac/linux

python 2.7.13

## Database

mysql

## lib

```
mysql-connector
scrapy
lxml
```

## You can start your spider with:

```
    scrapy startproject spyderA
    cd spyderA
    scrapy genspider cuiqingcai cuiqingcai.com
```

## Create database and/or table in your mysql database

see ddl.sql

## Test/Debug in pycharm ide

right click entrypoint.py file

run/debug entrypoint

## run scrapy

```
scrapy crawl cuiqingcai
```