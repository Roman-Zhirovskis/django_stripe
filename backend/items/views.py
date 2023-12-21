from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.generics import RetrieveAPIView
from .serrializer import ItemSerializer


from items.models import Item, Order
from .item_service import (
    ItemStripeService,
    OrderTaxDiscountStripeService,
    ItemPaymentIntendStripeService,
)


# Оптимизироват запросы в БД, раскидать логику по соответсвующим модулям (Общее замечание)
class ItemDetailView(RetrieveAPIView):
    """ItemRetriveView выполняет функционал отображения одного Item,
    а также кнопки Buy, которая редиректит на форму оплаты твоара"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        return render(request, "item.html", context={"item": instance})


class ItemRetriveView(RetrieveAPIView):
    """ItemRetriveView выполняет функционал создание платежа для одного Item
    используя stripe.Session.create"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        stripe_service = ItemStripeService(
            instance, "http://localhost:8000/", "http://localhost:8000/"
        )
        session_id = stripe_service.create_session()
        return JsonResponse({"session_id": session_id})


class ItemIntentRetriveView(RetrieveAPIView):
    """ItemRetriveView выполняет функционал создание платежа для одного Item
    с помощью stripe.PaymentIntent.create"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Добавить в DI
        payment_intend = ItemPaymentIntendStripeService(instance)
        payment = payment_intend.create_paymentIntent()

        status = payment_intend.polling(payment.id)
        return JsonResponse(
            {
                "payment_intend": payment.client_secret,
                "payment_id": payment.id,
                "status": status,
            }
        )


class OrderRetriveView(RetrieveAPIView):
    """OrderRetriveView выполняет функционал для создание платежа для Order"""

    queryset = Order.objects.all()
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        instance: Order = self.get_object()
        # Это убрать, добавить валидацию выходных данных для обработки
        tax, discount = None, None
        if instance.tax:
            tax = instance.tax.percent
        if instance.discount:
            discount = instance.discount.percent
        # отправлять данные в сервис после обработки
        order_service = OrderTaxDiscountStripeService(
            instance.items.all(), "http://localhost:8000/", "http://localhost:8000/", tax, discount
        )
        # добавить обработчик ошибок
        session_id = order_service.create_session()

        return JsonResponse({"session_id": session_id})


# class OrderRetriveView(RetrieveAPIView):
#     queryset = Order.objects.all()
#     lookup_field = "id"

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         order_service = OrderTaxDiscountStripeService(
#             instance.items.all(), "http://localhost:8000/", "http://localhost:8000/"
#         )
#         session_id = order_service.create_session()
#         return JsonResponse({"session_id": session_id})


# class OrderTaxRetriveView(RetrieveAPIView):
#     queryset = Order.objects.all()
#     lookup_field = "id"

#     def retrieve(self, request, *args, **kwargs):
#         item = Item.objects.get(id=1)
#         tax = Tax.objects.get(id=1)
#         discount = Discount.objects.get(id=2)
#         tax_amount = item.price * 100 * tax.percent
#         discount_amount = item.price * 100 * discount.percent
#         session = stripe.checkout.Session.create(
#             payment_method_types=["card"],
#             line_items=[
#                 {
#                     "price_data": {
#                         "currency": "usd",
#                         "product_data": {
#                             "name": item.name,
#                         },
#                         "unit_amount": int(item.price) * 100
#                         + int(tax_amount)
#                         - int(discount_amount),
#                     },
#                     "quantity": 1,
#                 }
#             ],
#             mode="payment",
#             success_url="http://localhost:8000/",
#             cancel_url="http://localhost:8000/",
#         )
#         return JsonResponse({"session_id": [session.id, tax_amount, discount_amount]})


# class OrderRetriveView(RetrieveAPIView):
#     queryset = Order.objects.all()
#     lookup_field = "id"

#     def retrieve(self, request, *args, **kwargs):
#         instance: Order = self.get_object()
#         if instance.tax.percent:
#             tax = instance.tax.percent
#         if instance.discount.percent:
#             discount = instance.discount.percent

#         order_service = OrderTaxDiscountStripeService(
#             instance.items.all(), "http://localhost:8000/", "http://localhost:8000/", tax, discount
#         )
#         session_id = order_service.create_session()
#         return JsonResponse({"session_id": session_id})


"""
import stripe
from django.conf import settings
from django.shortcuts import render

def create_checkout_session(request, product_id):
    # Retrieve the product and associated discount (if any)
    product = Product.objects.get(id=product_id)
    discount = Discount.objects.filter(code=request.GET.get("discount_code")).first()

    # Calculate the total amount (including discount if applicable)
    unit_amount = int(product.price) * 100
    if discount:
        unit_amount -= int(discount.amount) * 100

    # Create metadata for Stripe Checkout session
    metadata = {
        "product_id": product.id,
        "discount_code": discount.code if discount else None,
        "tax_rate": Tax.objects.first().rate if Tax.objects.exists() else None,
    }

    # Create the Stripe Checkout session
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": unit_amount,
                    "product_data": {
                        "name": product.name,
                        "description": product.description,
                        "images": [f"{settings.BACKEND_DOMAIN}/{product.thumbnail}"],
                    },
                },
                "quantity": product.quantity,
            }
        ],
        metadata=metadata,
        mode="payment",
        success_url=settings.PAYMENT_SUCCESS_URL,
        cancel_url=settings.PAYMENT_CANCEL_URL,
    )

    # Render the checkout page with the session ID
    return render(request, "checkout.html", {"session_id": checkout_session.id})
"""
