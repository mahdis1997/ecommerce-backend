import zarinpal
from rest_framework.viewsets import ModelViewSet
from .models import Cart, CartItem,Order,OrderItem,Payment
from products.models import Product
from .serializers import CartSerializer, CartItemSerializer,OrderItemSerializer,OrderSerializer,PaymentSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from zarinpal import ZarinPal
from zarinpal.models import RequestInput
from rest_framework.decorators import action
from django.shortcuts import redirect
from .services.zarinpal import create_payment, verify_payment, get_payment_url
class CartViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user=request.user).first()

        if not cart:
            cart = Cart.objects.create(user=request.user)

        serializer = CartSerializer(cart)
        return Response(serializer.data)


class CartItemViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart = Cart.objects.filter(user=self.request.user).first()

        if not cart:
            return CartItem.objects.none()

        return cart.items.all()

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user=request.user).first()

        if not cart:
            cart = Cart.objects.create(user=request.user)

        product_id = request.data["product"]
        product = Product.objects.get(id=product_id)

        quantity = int(request.data["quantity"])

        if quantity > product.stock:
            raise ValidationError("Not enough stock.")

        cart_item = CartItem.objects.filter(
            cart=cart,
            product=product
        ).first()

        if cart_item:
            if cart_item.quantity + quantity > product.stock:
                raise ValidationError("Not enough stock.")

            cart_item.quantity += quantity
            cart_item.save()

        else:
            cart_item = CartItem.objects.create(
                cart=cart,
                product=product,
                quantity=quantity
            )

        serializer = CartItemSerializer(cart_item)

        return Response(serializer.data)

class OrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.filter(
            user=request.user
        ).first()
        if not cart:
            raise ValidationError("Cart not found.")
        cart_items = cart.items.all()
        if not cart_items.exists():
            raise ValidationError("Cart is empty.")
        total_price = 0
        for item in cart_items:
            total_price += item.product.price * item.quantity
        order = Order.objects.create(
            user=request.user,
            total_price=total_price
        )
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        cart_items.delete()
        serializer = OrderSerializer(order)
        return Response(serializer.data)
class PaymentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(
            order__user=self.request.user
        )

    def create(self, request, *args, **kwargs):

        order = Order.objects.filter(
            id=request.data["order"],
            user=request.user
        ).first()

        if not order:
            raise ValidationError("Order not found.")

        payment, created = Payment.objects.get_or_create(
            order=order,
            defaults={
                "amount": order.total_price
            }
        )

        response = create_payment(
            amount=payment.amount,
            order_id=order.id
        )

        authority = response.data.authority

        payment.authority = authority
        payment.save()

        payment_url = get_payment_url(authority)

        return Response({
            "payment_url": payment_url,
            "authority": authority
        })

    @action(
        detail=False,
        methods=["get"],
        url_path="callback",
        permission_classes=[]
    )
    def callback(self, request):

        authority = request.query_params.get("Authority")
        status = request.query_params.get("Status")

        if status != "OK":
            return Response({
                "message": "Payment cancelled"
            })

        payment = Payment.objects.filter(
            authority=authority
        ).first()

        if not payment:
            return Response({
                "message": "Payment not found"
            }, status=404)

        response = verify_payment(
            authority=authority,
            amount=payment.amount
        )

        print(response)

        return Response({
            "message": "Verify response",
            "response": str(response)
        })

    def callback(self, request):

        authority = request.query_params.get("Authority")
        status = request.query_params.get("Status")

        if status != "OK":
            return Response({
                "message": "Payment cancelled"
            })

        payment = Payment.objects.filter(
            authority=authority
        ).first()

        if not payment:
            return Response({
                "message": "Payment not found"
            }, status=404)

        response = verify_payment(
            authority=authority,
            amount=payment.amount
        )

        if response.data.code == 100:
            payment.status = "paid"
            payment.ref_id = response.data.ref_id
            payment.save()

            payment.order.status = "paid"
            payment.order.save()

            return Response({
                "message": "Payment successful",
                "ref_id": response.data.ref_id
            })

        return Response({
            "message": "Payment failed"
        })