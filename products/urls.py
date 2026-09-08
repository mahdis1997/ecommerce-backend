from  django.urls import path
from .views import ProductListView,ProductDetailView,ProductViewSet
from rest_framework.routers import DefaultRouter
urlpatterns=[
    path("product/",ProductListView.as_view()),
    path("product/<int:pk>/",ProductDetailView.as_view())
]
router=DefaultRouter()
router.register("products", ProductViewSet, basename="product")

urlpatterns = router.urls