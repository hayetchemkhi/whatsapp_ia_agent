import httpx
import os

def get_client_info(number):
    # Exemple mock
    return {
        "name": "Client " + number[-4:],
        "address": "123 Rue Exemple"
    }

async def send_whatsapp_message(to, message):
    url = f"https://api.ultramsg.com/{os.getenv('ULTRAMSG_INSTANCE_ID')}/messages/chat"
    payload = {
        "token": os.getenv("ULTRAMSG_TOKEN"),
        "to": to,
        "body": message
    }
    async with httpx.AsyncClient() as client:
        await client.post(url, data=payload)
