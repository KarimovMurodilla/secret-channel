import asyncio
import json
from data import config
from yookassa import Configuration, Payment


Configuration.account_id = config.SHOP_ID
Configuration.secret_key = config.SHOP_API_TOKEN


def payment(value,description):
	payment = Payment.create({
    "amount": {
        "value": value,
        "currency": "RUB"
    },
    "payment_method_data": {
        "type": "bank_card"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": "https://t.me/teeessstbot"
    },
    "capture": True,
    "description": description
	})

	return json.loads(payment.json())


async def check_payment(payment_id):
    payment = json.loads((Payment.find_one(payment_id)).json())
    while payment['status'] == 'pending':
        print(payment['status'])
        payment = json.loads((Payment.find_one(payment_id)).json())
        await asyncio.sleep(3)
    
    if payment['status']=='succeeded':
        print(payment['status'])
        return True