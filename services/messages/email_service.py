import requests
import json
import logging

logger = logging.getLogger(__name__)

class EmailService:
    @staticmethod
    def send(subject:str, body:str, to:list):
        url = "https://api.sendinblue.com/v3/smtp/email"
        payload = json.dumps({
            "sender": {
                "name": "Gustavo Ghioldi",
                "email": "gustavoghioldi@gmail.com"
            },
             "to": [
            {
                "email": to[0],
                "name": "John Doe"
            }
            ],
            "subject": subject,
            "htmlContent": f"<html><head></head><body>{body}</body></html>"})
        headers = {
            'accept': 'application/json',
            'api-key': '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',
            'content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)



