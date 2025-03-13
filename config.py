import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("Token no encontrado. Asegúrate de haber configurado la variable de entorno.")
