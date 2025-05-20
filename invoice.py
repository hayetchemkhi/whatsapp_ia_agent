from fpdf import FPDF
import os

def generate_invoice(order_items, client_info, invoice_id):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Facture #{invoice_id}", ln=True, align="C")
    pdf.cell(200, 10, f"Client : {client_info['name']}", ln=True)
    pdf.cell(200, 10, f"Adresse : {client_info['address']}", ln=True)
    pdf.ln(10)

    total = 0
    for item in order_items:
        line = f"{item['qty']} x {item['product']} - {item['qty']*10}€"
        total += item['qty'] * 10
        pdf.cell(200, 10, line, ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, f"Total : {total} €", ln=True)

    folder = "invoices"
    os.makedirs(folder, exist_ok=True)
    pdf_path = f"{folder}/facture_{invoice_id}.pdf"
    pdf.output(pdf_path)

    return pdf_path, f"http://localhost:8000/{pdf_path}"
