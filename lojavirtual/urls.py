from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from lojavirtual.drf import views

router = routers.DefaultRouter()
router.register(r"api", views.AllProductsViewset, basename="allproducts")
router.register(
    r"product/(?P<slug>[^/.]+)",
    views.ProductInventoryViewset,
    basename="products",
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("demo/", include("lojavirtual.demo.urls", namespace="demo")),
    path("", include(router.urls)),
]
