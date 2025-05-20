from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os
from database import init_db, get_db
from models import Message
from llm import extract_order
from invoice import generate_invoice
from utils import send_whatsapp_message, get_client_info
import uuid

load_dotenv()
app = FastAPI()
init_db()

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    sender = data.get("from")
    body = data.get("body")

    order_items = await extract_order(body)

    client_info = get_client_info(sender)
    invoice_id = str(uuid.uuid4())[:8]
    pdf_path, pdf_url = generate_invoice(order_items, client_info, invoice_id)

    message = f"Bonjour {client_info['name']} ! Voici votre facture : {pdf_url}"
    await send_whatsapp_message(sender, message)

    db = get_db()
    db.add(Message(number=sender, body=body, invoice_url=pdf_url))
    db.commit()

    return {"status": "ok"}
