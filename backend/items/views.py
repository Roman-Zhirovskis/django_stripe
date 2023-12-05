from django.conf import settings
from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import render

import stripe
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .serrializer import ItemSerializer


from items.models import Item
from .item_service import ItemStripeService

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        return render(request, "item.html", context={"item": instance})


class ItemRetriveView(RetrieveAPIView):
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
