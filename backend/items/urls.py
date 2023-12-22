from items.views import ItemDetailView
from django.urls import path


urlpatterns = [
    path("item/<int:id>", ItemDetailView.as_view(), name="item_detail"),  #
    # Это нужно перенести в приложение payments, как и логику сервисов
    # path("buy/<int:id>", ItemRetriveView.as_view(), name="buy_item"),
    # path("order_buy/<int:id>", OrderRetriveView.as_view(), name="make_order"),
    # path("intent_buy/<int:id>", ItemIntentRetriveView.as_view(), name="intent_buy"),
]
