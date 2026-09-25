from zarinpal import ZarinPal
from zarinpal.models import RequestInput,VerifyInput


zarinpal = ZarinPal(
    merchant_id="YOUR_MERCHANT_ID"
)


def create_payment(amount, order_id):
    payment_request = RequestInput(
        amount=int(amount),
        description=f"Payment for order {order_id}",
        callback_url="http://127.0.0.1:8000/api/payments/callback/"
    )

    response = zarinpal.request(payment_request)

    return response
def verify_payment(authority,amount):
    verify_request=VerifyInput(
        authority=authority,
        amount=int(amount)
    )
    response=zarinpal.verify(verify_request)
    return response
def get_payment_url(authority):
    return zarinpal.get_payment_link(authority)