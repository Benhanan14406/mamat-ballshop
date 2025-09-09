from django.urls import path
from . import views

urlpatterns = [
    # URLS using api_view
    path("", views.homepage, name="homepage"),
    path("create_item", views.createProduct, name="createProduct"),
    path("<int:productId>", views.productDetails, name="productDetails"),
]
