import requests
from bs4 import BeautifulSoup
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1502493507557003305/AR96DTBR24lMnFrxuMUmIuFzHOksces65ZVSObb93lpFOcD3ZsHJu61hGLLk6NMLuV2U"
URL = "https://www.pekora.zip/home"

itens_vistos = set()

def enviar_discord(mensagem):
    data = {
        "content": mensagem
    }

    requests.post(WEBHOOK_URL, json=data)

while True:
    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")

        textos = soup.get_text("\n")
        linhas = [x.strip() for x in textos.split("\n") if x.strip()]

        for linha in linhas:
            if linha not in itens_vistos:
                itens_vistos.add(linha)

                if len(linha) > 15:
                    enviar_discord(f"🛒 Novo texto detectado: {linha}")
                    print("Novo:", linha)

        time.sleep(60)

    except Exception as e:
        print("Erro:", e)
        time.sleep(30)