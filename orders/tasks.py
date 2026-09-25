from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def send_order_confirmation(order_id):
    order = Order.objects.select_related("user").get(id=order_id)
    send_mail(
        subject=f"Order #{order_id} Confirmation",
        message=f"Your order #{order_id} has been successfully paid.{order.total_price}",
        from_email=None,
        recipient_list=[order.user.email],
    )

    return f"Email sent for order {order_id}"