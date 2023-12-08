# Django + Stripe API бэкенд (MVP gen)

**NOTE**: Не конечная версия проекта !
Версия релизнута исключительно для демонстрации работы ручек:

## Следующий релиз
**NOTE**: Описание будущих релизов находиться в файле `release_version.md`!

- Архитектура проекта, логика сервисов будет изменена 

- Правки по оставленным замечаниям в коде

- Реализовать Stripe Payment Intent для Order

## Описание

### Этот проект представляет собой реализацию Django + Stripe API бэкенда с базовым функционалом для продажи товаров.
## Основные задачи
- Django Модель Item с полями (name, description, price) `(Done)`
- API методы:
  - GET /buy/{id} - получение Stripe Session Id для оплаты выбранного Item `(Done)`
  - GET /item/{id} - получение информации о выбранном Item `(Done)`

## Бонусные функции

  - Запуск используя Docker `(Done)`
  - Использование environment variables `(Done)`
  - Просмотр Django Моделей в Django Admin панели `(Done)`
  - Запуск приложения на удаленном сервере, доступном для тестирования `(Will made after refactoring)` 
  - Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items `(Done)`
  - Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. `(Done)`
  - Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте `(Done)` 
  - Реализовать не Stripe Session, а Stripe Payment Intent. `(Done)` 


**NOTE**: Root of the django project is at the `backend` folder

Here is a short instruction on how to quickly set up the project:

## Before start
- Create `.env`
- Check and fill `.env` environment variables from `.env.example`

### Environment variables
#### Django:

- `DEBUG` - variable for defining environment for project `(True/False)`
- `DJANGO_SECRET_KEY` - secret key of django project, generates via
- `STRIPE_PUBLISHABLE_KEY` - stripe publik key for
- `STRIPE_SECRET_KEY` - stripe secret key for

### To start project run
```
$ docker-compose up --build
```
- Перейти в localhost/admin и создать экземпляры всех моделей

## Описание ручек 

- `localhost:8000/api/v1/items/item/<id>` - просмотр одного товара

- `localhost:8000/api/v1/items/buy/<id>` - создать сессию оплаты товара(url будет изменен)

- `localhost:8000/api/v1/items/order_buy/<id>` - создать сессию оплаты заказа(url будет изменен)

- `localhost:8000/api/v1/items/intent_buy/<id>` - создать оплату через 
PaymentIntend


## Описание релизов

### Релиз 0.0.2

- К модели Item добавлено поле currency

- Создано 2 Stripe Keypair на две разные валюты

- Реализована Stripe Payment Intent

- Добавлены все модели в DjnagoAdmin

### Релиз 0.0.3

- ...
