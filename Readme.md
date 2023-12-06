# Django + Stripe API бэкенд (MVP gen)

**NOTE**: Не конечная версия проекта !

Архитектура проекта, логика сервисов будет изменена 

Версия релизнута исключительно для демонстрации работы ручек:

## Описание

### Этот проект представляет собой реализацию Django + Stripe API бэкенда с базовым функционалом для продажи товаров.
- Django Модель Item с полями (name, description, price)
- API методы:
  - GET /buy/{id} - получение Stripe Session Id для оплаты выбранного Item
  - GET /item/{id} - получение информации о выбранном Item

## Бонусные функции

  - Запуск используя Docker
  - Использование environment variables
  - Просмотр Django Моделей в Django Admin панели
  - Запуск приложения на удаленном сервере, доступном для тестирования
  - Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
  - Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.
  - Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
  - Реализовать не Stripe Session, а Stripe Payment Intent.


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

