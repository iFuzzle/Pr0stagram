## Introduction ##
This bot was created for a small group of friends to share media from "the pr0" to a telegram group chat.<br>
Accessing media from Telegram directly requires additional actions and some content is locked behind an account.<br>
This bot simply scans for links to that website, grabs the content and posts it as an answer in the group chat.<br>
It's also possible to do this per PN to the bot and share the media from there.<br>

Legal discl

## Installation ##
This bot is supposed to only be run for PRIVATE USAGE! This is mainly to provde myself access to my own code.<br> 
But if you want to run your own version or just don't trust me (and you shouldn't), you can run your own instance.<br>
From experience I can tell you, that this process is subject to change and provided more as a guideline for myself.

### Get your telegram token ###
You will need an API Token for Telegram. You will have to find @BotFather on Telegram and do the following:
* press ``start``
* click ``new bot``
* enter a name
* enter a username (shown to others, ending in 'bot')
* copy and paste your token into a file called telegramtoken in your project folder
* if you want to use the bot in a group use ``/setprivacy`` (disabled) and ``/setjoingroups`` before adding it

### Get your pr0 token ###
You only need a normal user account on pr0 for this. I don't have a bot account myself (yet).<br>

%TODO Subject to change
    - new API version to be used
    - access without pr0 account? (sfp only?)
    - ask for bot access
    - rewrite readme for new API version

### Running it as a background service on your server with systemd ###
Once you have your cookie, you might want to run it with the provided service. You will need to make adjustments to it.
Quick guide (**errors are to be expected at every step**):
* useradd shitt0lk_bot
* <ftp> %yourmachine%/Pr0stagram/* /home/shitt0lk_bot/
* mv Shitt0lk.service /etc/systemd/system/
* chmod 700 /etc/systemd/system/Shitt0lk.service
* chmod 700 /home/shitt0lk_bot/Shitt0lk.py
* chown root:root /etc/systemd/system/Shitt0lk.service
* su shitt0lk_bot
* cd /home/shitt0lk_bot
* python3 -m venv /home/shitt0lk_bot/venv/
* source /home/shitt0lk_bot/venv/bin/activate
* pip install -r requirements.txt
* chmod 700 /home/shitt0lk_bot/Shitt0lk.py
* python3 /home/shitt0lk_bot/Shitt0lk.py
* send a pr0gramm.com link to your bot via PM
* <ftp get> /home/shitt0lk_botcaptcha.png
* type the captcha in the comand line
* Ctrl+C
* Ctrl+D
* systemctl daemon-relaod
* systemctl enable Shitt0lk.service
* systemctl start Shitt0lk.service
done

%TODO: Docker

## Be aware! ##
TLDR: it's your fault if you run this.<br>

I provide this code and documentation without any warranty and advice you NOT to run it or use my bot.<br>
If you face any sort of consequences for running or using this bot, you are accountable for yourslef.<br>
This is meant for private use! Don't make money with this and don't share copyrighted material!!<br>



## Licences of used Libraries ##
https://github.com/python-telegram-bot/python-telegram-bot/blob/master/LICENSE <br>
https://github.com/itssme/pypr0/blob/master/LICENSE <br>