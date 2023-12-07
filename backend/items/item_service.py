import stripe

from django.conf import settings

from .models import Item

# создать базовый абстрактный класс создания оплаты
# вынести stripe.api_key в базовый класс создания stripe.checkout.Session
stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemStripeService:
    """Сервис для работы с товарами"""

    def __init__(self, item: Item, success_url: str, cancel_url: str):
        self.item = item
        self.success_url = success_url
        self.cancel_url = cancel_url

    def create_session(self):
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    **self._create_line_items(),
                    "quantity": 1,
                }
            ],
            metadata={"product_id": self.item.pk},
            mode="payment",
            success_url="http://localhost:8000/",
            cancel_url="http://localhost:8000/",
        )
        return session.id

    def _create_line_items(self) -> dict:
        data_dict = {
            "price_data": {
                "currency": self.item.currency,
                "unit_amount": int(self.item.price) * 100,
                "product_data": {
                    "name": self.item.name,
                    "description": self.item.description or "None",
                },
            },
        }
        return data_dict


class OrderTaxDiscountStripeService:
    """Сервис для работы с заказами"""

    def __init__(self, order: list[Item], success_url: str, cancel_url: str, tax, discount):
        self.order = order
        self.success_url = success_url
        self.cancel_url = cancel_url
        # полный бред, нужно формировать словарь и делать проверку до вызова сервиса (пока костыль)
        self.tax = tax if tax else 1
        self.discount = discount if discount else 1

    def create_session(self):
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[self._create_line_items(item) for item in self.order],
            mode="payment",
            success_url="http://localhost:8000/",
            cancel_url="http://localhost:8000/",
        )
        return session.id

    def _create_line_items(self, item: Item) -> dict:
        data_dict = {
            "price_data": {
                "currency": "usd",
                "unit_amount": self._create_unit_amount(item.price),
                "product_data": {
                    "name": item.name,
                    "description": item.description or "None",
                },
            },
            "quantity": 1,
        }
        return data_dict

    def _create_unit_amount(self, item_price) -> int:
        tax_amount = item_price * self.tax
        discount_amount = item_price * self.discount
        unit_amount = item_price + tax_amount - discount_amount

        return int(unit_amount) * 100
