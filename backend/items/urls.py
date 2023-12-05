from items.views import BuyItemView, ItemDetailView
from django.urls import path


urlpatterns = [
    path("buy/<int:id>", BuyItemView.as_view(), name="buy_item"),
    path("item/<int:id>", ItemDetailView.as_view(), name="item_detail"),
]
# api/v1/items/buy/1
