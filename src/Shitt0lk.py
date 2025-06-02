import base64
import logging
import urllib.request
import requests
import yaml
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler, ConversationHandler

import image_grabber

logger = logging.getLogger("Sh1tlogger")
log_format = '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s'
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    filename="Sh1t.log")
logger.info("Started logging")

CAPTCHA, HELPER = range(2)
helper_token = ""


def pr0p0st(update: Update, context: CallbackContext) -> None:
    logger.debug(f'msg received: {update.message.text}')
    if 'pr0gramm.com' in update.message.text:
        ident = 0
        logger.debug(f'pr0 in Nachricht entdeckt')
        for word in update.message.text.split():
            if 'pr0gramm.com' in word:
                logger.debug(f'word mit pr0: {word}')
                # letzten Teil vom Link bekommen Kommentare : und Zeitstempel ? wegschmeißen
                word = word.split("/")[-1].split("?")[0].split(":")[0]
                ident = int(word)
                logger.debug(f'erkannte Endung: {ident}')
        if ident != 0:
            url = image_grabber.pr0_image_link_grabber(ident=ident)

            logger.info(f'grabbing content from -> https://www.pr0gramm.com/new/{str(ident)}')
            if url.endswith(".mp4"):
                logger.info(f'Video detected! Trying: https://vid.pr0gramm.com/{url}')
                with urllib.request.urlopen(f"https://vid.pr0gramm.com/{url}") as f:
                    update.message.reply_video(f)
            elif url.endswith(".gif"):
                logger.info(f'GIF detected! Trying: https://img.pr0gramm.com/{url}')
                with urllib.request.urlopen(f"https://img.pr0gramm.com/{url}") as f:
                    update.message.reply_animation(f)
            else:
                logger.info(f'still image detected! Trying: https://img.pr0gramm.com/{url}')
                with urllib.request.urlopen(f"https://img.pr0gramm.com/{url}") as f:
                    update.message.reply_photo(f)

        else:
            logger.error('Error: Some miss structured link was given.')
            update.message.reply_text("I cant read your link. The post number should be the last thing. Try again.")


def login(update: Update, context: CallbackContext) -> int:
    logger.info("login attempt")
    if update.effective_user.id == 59554881:  # set your personal Telgram ID here
        logger.info(f"Login triggered by owner")
        captcha_req = requests.get("https://pr0gramm.com/api/user/captcha")
        helper_token = captcha_req.json()["token"]
        image = captcha_req.json()["captcha"].split("base64,")[-1]
        image = base64.decodebytes(bytes(image, "utf-8"))
        update.effective_message.reply_photo(image)
        return CAPTCHA
    else:
        update.effective_message.reply_text("not allowed")
        return ConversationHandler.END


def captcha(update: Update, context: CallbackContext) -> int:
    captcha_text = update.message.text[1:]  # Es muss ein / davor stehen, das muss wieder weg...
    update.effective_message.reply_text(f"Captcha ist: {captcha_text}")
    logger.warning(f"captcha Eingabe: {captcha_text}")
    image_grabber.login(captcha=captcha_text, token=helper_token)
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(f"User {user.id} canceled the conversation.")
    update.message.reply_text("Prozess abgebrochen")
    return ConversationHandler.END


if __name__ == '__main__':
    # read settings from settings.yaml
    with open("settings.yaml", "r") as settings_file:
        settings = yaml.load(settings_file, Loader=yaml.FullLoader)

    bottoken = settings['telegram']['token']
    updater = Updater(token=bottoken)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, pr0p0st))

    conv_handler = ConversationHandler(
        per_user=True,
        per_chat=True,
        per_message=False,
        entry_points=[CommandHandler('login', login)],
        states={
            CAPTCHA: [
                MessageHandler(Filters.text, captcha)
            ]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    logger.info("Bot started successfully")

    updater.start_polling()
    updater.idle()
