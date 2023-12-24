from django.urls import path

from payments.views import PurchaseOneItemView, PayOrderView, PurchaseOneItemWithIntentView

urlpatterns = [
    path("buy/<int:id>", PurchaseOneItemView.as_view(), name="buy_item"),
    path("order_buy/<int:id>", PayOrderView.as_view(), name="make_order"),
    path("intent_buy/<int:id>", PurchaseOneItemWithIntentView.as_view(), name="intent_buy"),
]
