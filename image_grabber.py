import logging
from pr0gramm import *
import json
import yaml

logger = logging.getLogger("Sh1tlogger")
log_format = '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s'
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    filename="Sh1t.log")

# read settings from settings.yaml
with open("settings.yaml", "r") as settings_file:
    settings = yaml.load(settings_file, Loader=yaml.FullLoader)
username = settings['pr0gramm']['username']
password = settings['pr0gramm']['password']

def pr0_image_link_grabber(ident: int) -> str:
    api = Api(username=username, password=password)

    flag = api.calculate_flag(sfw=True, nsfp=False, nsfw=False, nsfl=False)

    try:
        my_json = json.loads(api.get_items(item=(ident + 1), flag=flag))
        if my_json["items"][0]["fullsize"] != "":
            logger.debug('Da drückste +')
            return f'{my_json["items"][0]["fullsize"]}'
        logger.debug(f'{my_json["items"][0]["image"]}')
        return f'{my_json["items"][0]["image"]}'

    except ConnectionResetError:
        logger.error('ConnectionResetError...')
        return ""


def login(captcha, token) -> bool:
    logger.info(f"Login attempt")
    api = Api(username=username, password=password)
    api.login()
    pass
    logger.debug(f"Log in with captcha: {captcha} and token: {token}")
    r = post("https://pr0gramm.com/api/user/login/",
             data={'name': username, 'password': password,
                   'captcha': captcha, 'token': token})
    if not r.json()["success"]:
        logger.error("There was an error logging in: " + str(r.json()["error"]))
    else:
        logger.debug("stuff with cookies")
        try:
            with open("./cookie.json", 'w') as temp_file:
                temp_file.write(json.dumps(utils.dict_from_cookiejar(r.cookies)))
        except IOError:
            logger.error('Could not write cookie file %s', "./cookie.json")
