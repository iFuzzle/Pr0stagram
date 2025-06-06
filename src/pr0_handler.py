import pr0gramm
import config_handler
import json


def login() -> None:
    config = config_handler.get_config()
    _pr0_username = config['pr0gramm']['username']
    _pr0_password = config['pr0gramm']['password']
    api = pr0gramm.Api(_pr0_username, _pr0_password)
    
    # NOTE: the pypr0 login function is annoying! best to just copy your cookie for now
    # HINT just make a <username>.json with {"me":"<COPIED FROM BROWSER COOKIE>"}

    # if cookie exists in current working directory (cwd), login function automatically uses it
    # FIXME currently only working with existing cookie.json
    if api.login():
        # TODO LOG: Debug: logged in
        return
    else:
        # get a Captcha
        # prompt Captcha to Admin User ID on Telegram
        # login with captcha and token
        # pr0gramm.Api.get_captcha(api, tmp_path='./')
        return

def get_content_url(post_id:int = -1) -> str:
    config = config_handler.get_config()
    username = config['pr0gramm']['username']
    password = config['pr0gramm']['password']
    api = pr0gramm.Api(username, password)
    print("get_content_url called")
    if post_id == -1:
        # TODO log / errorhandling
        print('issue when calling get_content, content_id was not set!')
    else:
        try:
            my_json = json.loads(api.get_items(item=(post_id + 1), flag=calc_flags()))
            if my_json['items'][0]['id'] != post_id:
                # for some reason, most likely flags or deleted, post was not found
                # api just gives back next best item, which we won't show
                return "not allowed"
            # FIXME pr0 api hands out fullsize under full.pr0... ending in .png but current code does only support .jpg
            #if my_json["items"][0]["fullsize"] != "":
            #    print('Da drückste +')
            #    print(f'myjson +: {my_json["items"][0]["fullsize"]}')
            #    return f'{my_json["items"][0]["fullsize"]}'
            #print(f'myjson: {my_json["items"][0]["image"]}')
            return f'{my_json["items"][0]["image"]}'
        except ConnectionResetError:
            #logger.error('ConnectionResetError...')
            print('error ConnectionReset')
            return ""
    return ""

def needs_spoiler(post_id:int = -1) -> bool:
    config = config_handler.get_config()
    username = config['pr0gramm']['username']
    password = config['pr0gramm']['password']
    api = pr0gramm.Api(username, password)
    if post_id == -1:
        # TODO log / errorhandling
        print('issue when calling get_content, content_id was not set!')
    else:
        try:
            my_json = json.loads(api.get_items(item=(post_id + 1), flag=calc_flags()))
            if my_json["items"][0]["flags"] not in (2,4):
                # if not in nsfw/nsfl, good to show!
                return False
        except ConnectionResetError:
            #logger.error('ConnectionResetError...')
            print('error ConnectionReset')
    return True

def calc_flags() -> int:
    config = config_handler.get_config()
    sfw  = config['pr0gramm']['flags']['sfw']
    nsfp = config['pr0gramm']['flags']['nsfp']
    nsfw = config['pr0gramm']['flags']['nsfw']
    nsfl = config['pr0gramm']['flags']['nsfl']
    pol  = config['pr0gramm']['flags']['pol']

    return pr0gramm.Api.calculate_flag(sfw=sfw,nsfp=nsfp, nsfw=nsfw, nsfl=nsfl, pol=pol)