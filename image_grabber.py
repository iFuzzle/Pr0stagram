from pr0gramm import *
import json


def pr0_image_link_grabber(ident: int) -> str:
    with open("./pr0token") as token:
        username, password = token.readlines()
    api = Api(username=username, password=password)

    flag = api.calculate_flag(sfw=True, nsfp=False, nsfw=False, nsfl=False)

    try:
        my_json = json.loads(api.get_items(item=(ident + 1), flag=flag))
        if my_json["items"][0]["fullsize"] != "":
            print("Da drückste +")
            return f'{my_json["items"][0]["fullsize"]}'
        return f'{my_json["items"][0]["image"]}'

    except ConnectionResetError:
        print("ConnectionResetError...")
        return ""
