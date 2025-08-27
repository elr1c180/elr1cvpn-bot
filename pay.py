import uuid
import json
from yookassa import Configuration, Payment

Configuration.account_id = '1047999'
Configuration.secret_key = 'live_eMwXg05gQLpetUZN-mp2E3Hc88KfjjzkiVZwsIdUkRI'

def generate_payment_link(price, description, user_id, username, period):
    payment = Payment.create({
        "amount": {
            "value": f"{price}",
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://elr1c.ru/return_url"
        },
        "capture": True,
        "description": f"{description}",
        "metadata": {
            "user_id": f"{user_id}",
            "username": f"{username}",
            "period": f"{period}"
        }
    }, uuid.uuid4())

    return payment.confirmation.confirmation_url