import logging

# ## preparations ##
# # load configs
# credentials
import telegram_handler

telegram_bot_token = open('telegramtoken', 'r').readline()
with open('pr0token', 'r') as file:
    pr0gramm_user_name = file.readline()
    pr0gramm_password = file.readline()
pr0gramm_flags = 15  # all flag

# # start logging
logging.basicConfig(filename='sh1t.log', filemode='w', encoding='utf-8', level=logging.DEBUG)  # TODO: Read from Config
# # prepare telegram bot
logging.debug('starting bot')
telegram_handler.start_bot(telegramtoken=telegram_bot_token)
logging.info('bot started')
# # check pr0 connection

# ## start ##
# # start telegram bot (listen)

