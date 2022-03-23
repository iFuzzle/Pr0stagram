import logging
import urllib.request
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler
import image_grabber


logger = logging.getLogger("Sh1tlogger")
log_format = '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s'
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    filename="Sh1t.log")
logger.info("Started logging")


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


def status(update: Update, context: CallbackContext) -> None:
    if update.effective_user == 59554881:    # set your personal Telgram ID here
        group_ids = ", ".join(str(gid) for gid in context.bot_data.setdefault("group_ids", set()))
        channel_ids = ", ".join(str(cid) for cid in context.bot_data.setdefault("channel_ids", set()))
        response = f"@{context.bot.username} ist Mitglied in {len(group_ids)} Gruppen:\n{group_ids}" \
                   f"\n\naußerdem Admin hier:\n{channel_ids}"
        logger.log(f"Gruppen:\n{group_ids}")
        logger.log(f"Davon Admin:\n{channel_ids}")
    else:
        response = "For security reasons this Info is limited to the bot Owner."
        logger.warn(f"Zugriffsversuch auf Statusmeldung durch ID {update.effective_user}")
    update.effective_message.reply_text(response)


if __name__ == '__main__':
    bottoken = open("./telegramtoken").readline()
    updater = Updater(token=bottoken)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, pr0p0st))
    dispatcher.add_handler(CommandHandler("status", status))

    logger.info("Bot started successfully")

    updater.start_polling()
    updater.idle()


