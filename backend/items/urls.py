from items.views import ItemDetailView, ItemRetriveView
from django.urls import path


urlpatterns = [
    path("item/<int:id>", ItemDetailView.as_view(), name="item_detail"),
    path("item_buy/<int:id>", ItemRetriveView.as_view(), name="item_detail"),
]
