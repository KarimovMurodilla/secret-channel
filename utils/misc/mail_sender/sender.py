from mailjet_rest import Client

from app.config import API_KEY as api_key
from app.config import API_SECRET as api_secret


class SendMail:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
    
    def send_mail(self, sender, sender_name, recipient, recipient_name, subject, text_part):
        mailjet = Client(auth=(self.api_key, self.api_secret), version='v3.1')

        data = {
        'Messages': [
            {
            "From": {
                "Email": sender,
                "Name": sender_name
            },
            "To": [
                {
                "Email": recipient,
                "Name": recipient_name
                }
            ],
            "Subject": subject,
            "TextPart": text_part,
            "HTMLPart": text_part,
            "CustomID": "AppGettingStartedTest"
            }
        ]
        }

        result = mailjet.send.create(data=data)
        return result
        