from django.http import JsonResponse

from rest_framework.generics import RetrieveAPIView

from items.models import Item
from orders.models import Order
from service.stripe_service import (
    ItemStripeService,
    ItemPaymentIntendStripeService,
    OrderTaxDiscountStripeService,
)


class PurchaseOneItemView(RetrieveAPIView):
    """Выполняет функционал создание платежа для одного Item
    используя stripe.Session.create"""

    queryset = Item.objects.all()
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        stripe_service = ItemStripeService(
            instance, "http://localhost:8000/", "http://localhost:8000/"
        )
        session_id = stripe_service.create_session()
        return JsonResponse({"session_id": session_id})


class PurchaseOneItemWithIntentView(RetrieveAPIView):
    """ItemRetriveView выполняет функционал создание платежа для одного Item
    с помощью stripe.PaymentIntent.create"""

    queryset = Item.objects.all()
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


class PayOrderView(RetrieveAPIView):
    """OrderRetriveView выполняет функционал для создание платежа для Order"""

    queryset = Order.objects.all()
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
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
