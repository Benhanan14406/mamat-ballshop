from django.urls import path
from . import views

urlpatterns = [
    # URLS using api_view
    path("", views.homepage, name="homepage"),
    path("create_item", views.createProduct, name="createProduct"),
    path("<uuid:productId>", views.productDetails, name="productDetails"),
    path("create_employee", views.addEmployee, name="addEmployee"),
]
