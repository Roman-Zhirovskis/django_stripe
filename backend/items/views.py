from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView

from items.models import Item


class ItemDetailView(RetrieveAPIView):
    """ItemRetriveView выполняет функционал отображения одного Item,
    а также кнопки Buy, которая редиректит на форму оплаты твоара"""

    queryset = Item.objects.all()
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        item = self.get_object()

        return render(request, "item.html", context={"item": item})
