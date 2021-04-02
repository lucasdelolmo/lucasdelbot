#!/usr/bin/env python
# pylint: disable=C0116
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        f'Usa /help para obtener la ayuda {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Hola, ¿como estas? Estoy aquí para ayudarte, y lo prometido es deuda. Sigue estos pasos para poder comenzar a ganar $20 DOLARES sin invertir tiempo ni dinero PASO 1: Guarda mi contacto para que puedas estar al pendiente y no te pierdas las oportunidades que ofrezco. PASO 2: Descarga la APP aqui: https://www.honeygain.com PASO 3: Una vez descargada la APK, registrate con este link: https://r.honeygain.me/LUCASF66E2 PASO 4: Inicia sesión hasta 3 dispositivos para poder sacarle el máximo provecho a este método PASO 5: Disfruta de la miel que generes y canjeala por dinero. (Mínimo para retirar: 20$) NOTA: Solo disponible para ANDROID, WINDOWS, MacOS y LINUX')





def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1783583118:AAE-7Qu4ipdETMJfX54LAwHiFT4ma1FZsTk")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
