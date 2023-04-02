import logging

from telegram import Update

from telegram.ext import filters
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler


logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.setLevel(logging.DEBUG)
log_to_console = logging.StreamHandler()
log_to_console.setLevel(logging.DEBUG)
log_to_console.formatter = formatter
logger.addHandler(log_to_console)
log_to_file = logging.FileHandler(filename='sh1t.log', mode='a', encoding='utf-8')
log_to_file.formatter = formatter
logger.addHandler(log_to_file)

pr0_link_filter = filters.Regex('pr0gramm\.com\/.*\/[0-9]*$')
logger.debug(f'regex used {pr0_link_filter.pattern}')


def start_bot(telegramtoken):
    logger.debug('beginning of start_bot in telegram_handler')
    application = ApplicationBuilder().token(telegramtoken).build()
    logger.debug('application created')

    # handlers
    pr0_link_message_handler = MessageHandler(pr0_link_filter, _pr0_link_)

    application.add_handler(pr0_link_message_handler)
    logger.debug('telegram bot handlers added')

    logger.debug('start polling')
    application.run_polling()
    logger.info('bot up and running')


async def _pr0_link_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)  # echoes

