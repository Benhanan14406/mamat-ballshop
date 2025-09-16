from django.urls import path
from . import views

urlpatterns = [
    # URLS using api_view
    path("", views.homepage, name="homepage"),
    path("create_item", views.createProduct, name="createProduct"),
    path("<uuid:productId>", views.productDetails, name="productDetails"),
    path("create_employee", views.addEmployee, name="addEmployee"),
    path("xml", views.show_xml, name="showXML"),
    path("json", views.show_json, name="showJSON"),
    path("xml/<uuid:productId>", views.show_xml_by_id, name="showXMLbyID"),
    path("json/<uuid:productId>", views.show_json_by_id, name="showJSONbyID"),
]
