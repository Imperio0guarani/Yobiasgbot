import os
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, Application, ChatMemberHandler
import asyncio

# Obtén el token de la variable de entorno
TOKEN = os.getenv('TELEGRAM_TOKEN')

if TOKEN is None:
    raise ValueError("El token de Telegram no está configurado como variable de entorno.")

# Definir la función start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('A su servicio.')

# Definir la función creator
async def creator(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Este bot fue creado por Tobiasg.')

# Función que maneja la bienvenida a nuevos miembros
async def welcome_new_member(update: Update, context: CallbackContext) -> None:
    # Verifica si hay nuevos miembros
    new_members = update.message.new_chat_members
    if new_members:
        for member in new_members:
            await update.message.reply_text(f"¡Bienvenido a la Corte Imperial de Su Majestad el Kaiser {member.full_name}!")

def main():
    # Crea la aplicación y pasa el token de tu bot.
    application = Application.builder().token(TOKEN).build()

    # Añade el handler para el comando /start
    application.add_handler(CommandHandler('start', start))

    # Añade el handler para el comando /creator
    application.add_handler(CommandHandler('creator', creator))

    # Añade el handler para los nuevos miembros
    application.add_handler(ChatMemberHandler(welcome_new_member, chat_member_types=['member']))

    # Inicia el bot
    application.run_polling()

if __name__ == '__main__':
    main()