from decimal import Decimal
import stripe

from .models import Item


class ItemStripeService:
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
                "currency": "usd",
                "unit_amount": int(self.item.price) * 100,
                "product_data": {
                    "name": self.item.name,
                    "description": self.item.description or "None",
                },
            },
        }
        return data_dict
