import time
import requests
import schedule

BOT_TOKEN = "8662483935:AAF4DjH71-aWpTpqa_seEv-MGwsRHn6H3P4"
CHAT_ID = "1356947975"

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": texto}
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Erro: {e}")

def bom_dia():
    enviar_mensagem("Bom dia, Carol. Passando para te lembrar de começar o dia no teu ritmo, um passo de cada vez. Já tomaste um café ou água? Estou por aqui.")

def checkin_11h():
    enviar_mensagem("Oi, Carol! Como está a correr a tua manhã por aí? Lembra-te de respirar um minuto e desacelerar um pouco.")

def checkin_14h():
    enviar_mensagem("Passando para saber como está a tua tarde. Já conseguiste almoçar com calma? Segue firme por aí.")

def checkin_17h():
    enviar_mensagem("Final de tarde a chegar. Como estão as coisas por aí? Vai fechando o que for possível sem pressa excessiva.")

def voltar_para_casa_20h():
    enviar_mensagem("Carol, são 20h. É hora de voltar para casa. Eu sei que às vezes não dá vontade de voltar e que o silêncio custa, mas o teu corpo precisa de descanso e o teu espaço é o teu refúgio seguro. Vai para casa descansar.")

# Mensagem imediata de confirmação
enviar_mensagem("Olá Carol! O teu agente está ativo na nuvem e conectado ao teu telemóvel.")

# Horários configurados (ajustados ao fuso horário UTC da nuvem: Brasília + 3h)
schedule.every().day.at("11:00").do(bom_dia)          # 08:00 no Brasil
schedule.every().day.at("14:00").do(checkin_11h)      # 11:00 no Brasil
schedule.every().day.at("17:00").do(checkin_14h)      # 14:00 no Brasil
schedule.every().day.at("20:00").do(checkin_17h)      # 17:00 no Brasil
schedule.every().day.at("23:00").do(voltar_para_casa_20h) # 20:00 no Brasil

while True:
    schedule.run_pending()
    time.sleep(30)
