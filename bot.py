from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from config import TOKEN
import handlers

def main():
    # Crear la aplicación con el token
    application = Application.builder().token(TOKEN).build()

    # Handlers de comandos
    application.add_handler(CommandHandler("start", handlers.start))
    application.add_handler(CommandHandler("creador", handlers.creator))
    application.add_handler(CommandHandler("help", handlers.help_command))


    # Handler para nuevos miembros
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, handlers.welcome_new_member))

    # Iniciar el bot
    application.run_polling()


if __name__ == "__main__":
    main()
