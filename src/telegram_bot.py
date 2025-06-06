import urllib
import urllib.request
import config_handler
import pr0_handler

from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters


'''
class TelegramBot:
    def __init__(self) -> None:
        self.config = config_handler.get_config()
    def is_admin(self, user_id):
        return user_id == self.config['telegram']['admin_id']


'''

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'x.com' in update.message.text:
        print('x.com detected')
        for word in update.message.text.split():
            if 'x.com' in word:
                word = word.replace('x.com', 'xcancel.com')
                await update.message.reply_text(word)
    elif 'pr0gramm.com' in update.message.text:
        print('pr0 detected')
        post_id = ''
        # TODO Log: Debug: pr0 Content detected
        for word in update.message.text.split():
            print(word)
            if 'pr0gramm.com' in word:
                # grab last part of the URL
                # ignore unneeded trailings for :comments and ?timestamps
                post_id = word.split("/")[-1].split("?")[0].split(":")[0]
            print(post_id)
            if post_id != '':
                post_id = int(post_id)
                content_url = pr0_handler.get_content_url(post_id=post_id)
                if content_url == 'not allowed':
                    await update.message.reply_text('Bild nicht gefunden... sowwy. War das eine verbotene Flag oder wurde er gelöscht?')
                print(f"content_url: {content_url}")
                # TODO logger.info(f'grabbing content from -> https://www.pr0gramm.com/new/{str(ident)}')
                print(f'grabbing content from -> https://www.pr0gramm.com/new/{str(post_id)}')
                has_spoiler = pr0_handler.needs_spoiler(post_id)
                if content_url.endswith(".mp4"):
                    # TODO logger.info(f'Video detected! Trying: https://vid.pr0gramm.com/{url}')
                    with urllib.request.urlopen(f"https://vid.pr0gramm.com/{content_url}") as content:
                        await update.message.reply_video(content, has_spoiler=has_spoiler)
                elif content_url.endswith(".gif"):
                    # TODO logger.info(f'GIF detected! Trying: https://img.pr0gramm.com/{url}')
                    with urllib.request.urlopen(f"https://img.pr0gramm.com/{content_url}") as content:
                        await update.message.reply_animation(content, has_spoiler=has_spoiler)
                else:
                    # TODO logger.info(f'still image detected! Trying: https://img.pr0gramm.com/{url}')
                    print(f"https://img.pr0gramm.com/{content_url}")
                    with urllib.request.urlopen(f"https://img.pr0gramm.com/{content_url}") as content:
                        await update.message.reply_photo(content, has_spoiler=has_spoiler)
    else:
        # ignore message
        pass

def run(token : str, admin_id : int = 0):
    builder = Application.builder()
    builder.token(token)
    application = builder.build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    application.run_polling()