import logging
from pr0gramm import *
import json

logger = logging.getLogger("Sh1tlogger")
log_format = '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s'
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    filename="Sh1t.log")


def pr0_image_link_grabber(ident: int) -> str:
    with open("./pr0token") as token:
        username, password = token.readlines()
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
