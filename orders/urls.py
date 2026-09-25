from rest_framework.routers import DefaultRouter
from .views import CartViewSet,CartItemViewSet,OrderViewSet,PaymentViewSet



router=DefaultRouter()
router.register('cart',CartViewSet,basename='cart')
router.register('cart-items',CartItemViewSet,basename='cart-item')
router.register('orders',OrderViewSet,basename='order')
router.register("payments", PaymentViewSet, basename="payment")
urlpatterns=router.urls