from django.contrib import admin
from django.urls import include, path

# from .yasg import urlpatterns as yasg_doc


v1 = [
    path("items/", include("items.urls")),
    path("orders/", include("orders.urls")),
    path("payments/", include("payments.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(v1)),
]

# urlpatterns += yasg_doc
