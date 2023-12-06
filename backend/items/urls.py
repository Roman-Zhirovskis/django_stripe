from items.views import ItemDetailView, ItemRetriveView, OrderRetriveView
from django.urls import path


urlpatterns = [
    path("item/<int:id>", ItemDetailView.as_view(), name="item_detail"),
    # Это нужно перенести в приложение payments, как и логику сервисов
    path("item_buy/<int:id>", ItemRetriveView.as_view(), name="buy_item"),
    path("order_buy/<int:id>", OrderRetriveView.as_view(), name="make_order"),
    # path("order_tax/<int:id>", OrderTaxRetriveView.as_view(), name="tax_order"),
]
