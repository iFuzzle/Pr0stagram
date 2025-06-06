import logging
import config_handler, pr0_handler, telegram_bot


logger = logging.getLogger("Sh1tlogger")
log_format = '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s'
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    filename="Sh1t.log")
logger.info("Started logging")

if __name__ == '__main__':
    config = config_handler.get_config()
    # pr0 login
    # FIXME pass username and password as string from config
    pr0_handler.login()
    telegram_bot.run(admin_id = config['telegram']['admin_id'],
                         token = config['telegram']['token'])
    exit() # should not reach this, because bot will be running endless unless interrupt is sent
