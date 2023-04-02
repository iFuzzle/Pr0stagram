import logging

from telegram import Update

from telegram.ext import filters
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler


pr0_link_filter = filters.Regex('pr0gramm\.com\/.*\/[0-9]*$')
logging.debug(f'regex used {pr0_link_filter.pattern}')


def start_bot(telegramtoken):
    application = ApplicationBuilder().token(telegramtoken).build()
    logging.debug('application created')

    # handlers
    # x_handler = CommandHandler('text', function_name)
    pr0_link_message_handler = MessageHandler(pr0_link_filter, _pr0_link_)

    application.add_handler(pr0_link_message_handler)
    logging.debug('telegram bot handlers added')

    logging.debug('start polling')
    application.run_polling()
    logging.info('bot up and running')


async def _pr0_link_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)  # echoes

