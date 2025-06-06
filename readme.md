## Introduction ##
This Bot was build to enable a group chat to consume content from pr0gramm.  
It started to allow members from a telegram group chat to view the content without having to access the site.  
Due to a lot of x.com content being posted recently and my dislike of the site, I've added an automation to upgrade links to the superior xcancel.com

Use this at your own risk, the code base is hold together with hot glue and hope.  
the functionality uses your personal pr0gramm account so if the bot instance you're running is doing something that gets you banned, it's your fault.

## Installation ##
This is best a best effort attempt to allow someone with a bit of tech background to get this up and running

### Get your telegram token ###
You will need an API Token for Telegram. You will have to find @BotFather on Telegram and do the following:
* press ``start``
* click ``new bot``
* enter a name
* enter a username (shown to others, ending in \`bot\`)
* copy the `settings.yaml.example` as `settings.yaml`and past your tokens in there.
* if you want to use the bot in a group use ``/setprivacy`` (disabled) and ``/setjoingroups`` before adding it

### Get your pr0 token ###
You will need a normal user account on pr0gramm for this. I dont have a bot account myself (yet).  
* fill in your username and password into the `settings.yaml` created above  
NOTE: as of PyPr0 version 0.2.8 it's not possible for me to move the captcha process to telegram chat messages as planned. It seems a rewrite of PyPr0s `api.login()` function would be required.

##### 'borrow' a cookie #####
You can try and run the bot via CLI to generate the cookie via the bot, but it's a bit annoying.  
Alternatively you can login via any browser you like, open the dev Tools (F12 in most cases), head to the Application tab and check your storage for Cookies.  
You need the full URL encoded string as 'me' and find the key 'pp' in the decoded string (there should be a checkbox to decode it right there).  
Create a ` <username>.json` and paste the contents there like `{"me": "<URL-encoded String full>", "pp": "<decoded pp string>"}`

#### Running via docker compose ####
create and fill in your `settings.yaml` before running docker compose.  
!! currently only login via existing cookie is working, so provide one !!

place your `<username>.json` cookie in the src directory. It will be copied during build and used.  
I suggest this command to build and run your container. It will automatically show you the logs so you can see your bot in action:  
``docker compose up --build -d && docker compose logs -f``


#### as a systemd service (depricated) ###
you have to write the service yourself if you want to run it this way again but I suggest you learn to love docker.

## Settings ##
telegram: you will get your bot token from @botfather (official telegram bot) and you can get your user_id from @userinfobot on telegram (not an official telegram bot, by https://github.com/nadam)  
pr0gramm: your username and password you use for login  
  flags: you can allow (TRUE) or deny (FALSE) your bot any flags on pr0gramm. I suggest not allowing anything but sfw but the bot will put a spoiler over nsfw/nsfl content automatically.  
loglevel: I suggest to leave it on INFO (evne if it's currently not implemented correctly)

## Be aware! ##
I provide this code and documentation without any warranty.  
If you face any sort of negative effects for using this bot (like being banned or worse) it's your fault! You've been warned

## Licences of used Libraries ##
https://github.com/python-telegram-bot/python-telegram-bot/blob/master/LICENSE <br />
https://github.com/itssme/pypr0/blob/master/LICENSE <br />
