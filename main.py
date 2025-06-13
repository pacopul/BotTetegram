import telebot
import logging
import os

# Configuración de logs 
# 💡 Emojis para logs ctrl cmd space 💡
logging.basicConfig(
    filename="telegram.log"
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
token = os.getenv('TOKEN')
id = os.getenv('ID')

# Token del bot de Telegram
# BOT_TOKEN = "7820202353:AAE2kTD8kIK_zIpZYcPiekSeCHEzQhTuRPU"
bot = telebot.TeleBot(token)

# Configuración de id de Telegram
#TELEGRAM_CHAT_ID = "272783109"
TELEGRAM_CHAT_ID = id

def enviar_notificacion_telegram(mensaje):
    try:
        bot.send_message(TELEGRAM_CHAT_ID, mensaje)
        logging.info("✅ Notificación enviada por Telegram.")
    except telebot.apihelper.ApiException as e:
        logging.error(f"⚠️ Error al enviar mensaje: {e}")
        if "chat not found" in str(e):
            logging.error("❌ Verifica que el ID del chat sea correcto.")
        elif "Forbidden" in str(e):
            logging.error("❌ El bot no tiene permisos para enviar mensajes.")
    except Exception as e:
        logging.error(f"❌ Error inesperado: {e}")
   
enviar_notificacion_telegram("Hola desde el bot")