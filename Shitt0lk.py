import urllib.request
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import image_grabber


def pr0p0st(update: Update, context: CallbackContext) -> None:
    if 'pr0gramm.com' in update.message.text:
        ident = 0
        for word in update.message.text.split():
            if 'pr0gramm.com' in word:
                # letzten Teil vom Link bekommen Kommentare : und Zeitstempel ? wegschmeißen
                word = word.split("/")[-1].split("?")[0].split(":")[0]
                ident = int(word)
        if ident != 0:
            url = image_grabber.pr0_image_link_grabber(ident=ident)

            print(f"grabbing content from -> https://www.pr0gramm.com/new/{str(ident)}")
            if url.endswith(".mp4"):
                with urllib.request.urlopen(f"https://vid.pr0gramm.com/{url}") as f:
                    update.message.reply_video(f)
            if url.endswith(".gif"):
                with urllib.request.urlopen(f"https://img.pr0gramm.com/{url}") as f:
                    update.message.reply_animation(f)
            else:
                with urllib.request.urlopen(f"https://img.pr0gramm.com/{url}") as f:
                    update.message.reply_photo(f)

        else:
            print("Error: Some miss structured link was given.")
            update.message.reply_text("I cant read your link. The post number should be the last thing. Try again.")


bottoken = open("./telegramtoken").readline()
updater = Updater(token=bottoken)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, pr0p0st))

print("I am running")

updater.start_polling()
updater.idle()
