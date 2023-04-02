import logging
import telegram_handler


# ## preparations ##
# # start logging
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

'''logging.basicConfig(filename='sh1t.log',
                    filemode='a',
                    encoding='utf-8',
                    level=logging.DEBUG)'''

logger.debug('started')
# # load config
# credentials
telegram_bot_token = open('telegramtoken', 'r').readline()
with open('pr0token', 'r') as file:
    pr0gramm_user_name = file.readline()
    pr0gramm_password = file.readline()
# flags
sfw = 1
nsfw = 2
nsfl = 4
nsfp = 8
pr0gramm_flags = sfw + nsfp + nsfw + nsfl  # all flags
logger.critical(f'calculated flag(s): {pr0gramm_flags} | swf=1, nfsw=2, nsfl=4, nfsp=8')

if __name__ == '__main__':
    # # prepare telegram bot
    logger.debug('starting bot')
    telegram_handler.start_bot(telegramtoken=telegram_bot_token)
    logger.info('bot started')
    # # check pr0 connection

    # ## start ##
    # # start telegram bot (listen)

