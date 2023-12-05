from django.conf import settings
from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import render

import stripe
from rest_framework.views import APIView


from items.models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


class BuyItemView(View):
    # Рабочая версия
    def get(self, request, id):
        item = Item.objects.get(id=id)
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "unit_amount": int(item.price) * 100,
                            "product_data": {
                                "name": item.name,
                                "description": item.description if item.description else "None",
                            },
                        },
                        "quantity": 1,
                    }
                ],
                metadata={"product_id": item.pk},
                mode="payment",
                success_url="http://localhost:8000/",
                cancel_url="http://localhost:8000/",
            )
            session_id = session.id
            return JsonResponse({"session_id": session_id})
        except stripe.error.StripeError as e:
            # Обработка ошибок, если не удалось создать сессию оплаты
            return JsonResponse({"error": str(e)}, status=500)


class ItemDetailView(APIView):
    def get(self, request, id):
        item = Item.objects.get(id=id)
        context = {
            "item": item,
            "stripe_publishable_key": stripe.api_key,  # Замените на свой ключ
        }

        # Рендерим HTML-страницу с информацией о товаре и кнопкой "Buy"
        return render(request, "item.html", context)
