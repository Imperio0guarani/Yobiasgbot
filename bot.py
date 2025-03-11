import os
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, Application
import asyncio

# Reemplaza 'TU_TOKEN' con el token que te proporcionó BotFather
TOKEN = os.getenv('TELEGRAM_TOKEN')

if TOKEN is None:
    raise ValueError("El token de Telegram no está configurado como variable de entorno.")


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('A su servicio.')

def main():
    # Crea la aplicación y pasa el token de tu bot.
    application = Application.builder().token(TOKEN).build()

    # Añade el handler para el comando /start
    application.add_handler(CommandHandler('start', start))

    # Añade el handler para el comando /creator
    application.add_handler(CommandHandler('creator', creator))

    # Inicia el bot
    application.run_polling()

    



if __name__ == '__main__':
    main()