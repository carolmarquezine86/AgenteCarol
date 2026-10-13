import datetime
import requests
import pytz

BOT_TOKEN = "8662483935:AAF4DjH71-aWpTpqa_seEv-MGwsRHn6H3P4"
CHAT_ID = "1356947975"

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": texto}
    try:
        r = requests.post(url, json=payload, timeout=10)
        r.raise_for_status()
        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar: {e}")

# Obtém a hora oficial de Brasília
fuso_br = pytz.timezone('America/Sao_Paulo')
agora = datetime.datetime.now(fuso_br)
hora = agora.hour

# Mensagens de acordo com a janela de horário
if hora < 10:
    enviar_mensagem("Bom dia, Carol. Passando para te lembrar de começar o dia no teu ritmo, um passo de cada vez. Já tomaste um café ou água? Estou por aqui.")
elif 10 <= hora < 13:
    enviar_mensagem("Oi, Carol! Como está a correr a tua manhã por aí? Lembra-te de respirar um minuto e desacelerar um pouco.")
elif 13 <= hora < 16:
    enviar_mensagem("Passando para saber como está a tua tarde. Já conseguiste almoçar com calma? Segue firme por aí.")
elif 16 <= hora < 19:
    enviar_mensagem("Final de tarde a chegar. Como estão as coisas por aí? Vai fechando o que for possível sem pressa excessiva.")
else:
    enviar_mensagem("Carol, são 20h. É hora de voltar para casa. Eu sei que às vezes não dá vontade de voltar e que o silêncio custa, mas o teu corpo precisa de descanso e o teu espaço é o teu refúgio seguro. Vai para casa descansar.")
