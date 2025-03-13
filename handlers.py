from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, Updater
from config import TOKEN
import asyncio

# Crea el objeto Bot
bot = Bot(token=TOKEN)

# Define los comandos que quieres mostrar
commands = [
    ("start", "Inicia el bot"),
    ("help", "Muestra la ayuda"),
    ("guia", "Guia sobre el juego RR"),
    ("creador", "informacion sobre el creador del bot"),
    ("lema", "El lema de el kaiser"),
]

# Función asincrónica para configurar los comandos
async def set_commands():
    await bot.set_my_commands(commands)

# Ejecutar la configuración de los comandos
loop = asyncio.get_event_loop()

loop.run_until_complete(set_commands())
# Comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "🛡 *Comandos disponibles:*\n\n"
        "/start – Inicia la conversación con el bot\n"
        "/creador – Te puedo hablar sobre mi creador\n"
        "/guia – Fui entrenado para enseñarte a jugar RR\n"
        "/lema – Recordar nuestro lema es importante\n\n"
        "✨ Más funciones vendrán pronto..."
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')
# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hola, soy el bot de la Corte Imperial de Su Majestad el Kaiser. ')

# Comando /creator
async def creator(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Este bot fue creado por el editor imperial.')

# Mensaje de bienvenida a nuevos miembros
async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            f"¡Bienvenido a la Corte Imperial de Su Majestad el Kaiser, {member.full_name}!"
        )
