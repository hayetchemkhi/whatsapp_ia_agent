import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

prompt_template = """Tu es un assistant. Voici un message WhatsApp du client :  
"{message}"  
Extrais la commande sous format JSON comme ceci :
[{{"product": "Nom produit", "qty": nombre}}, ...]"""

async def extract_order(message: str):
    model = genai.GenerativeModel("gemini-pro")
    prompt = prompt_template.format(message=message)
    response = model.generate_content(prompt)
    
    try:
        return eval(response.text)
    except:
        return [{"product": "Inconnu", "qty": 1}]
