## Introduction ##
This Bot was build to enable a group chat to consume content from a specific website.<br />
The Website this bot is grabbing from blocks a lot of content for invited users.<br />
As some of our group didn't had accounts, we needed a way to share it with them and it also enables everyone to consume the content without visiting the website itself.


## Installation ##
Right now I dont provide much Documentation about how to set up the bot. But here are the basics:

### Get your telegram token ###
You will need an API Token for Telegram. You will have to find @BotFather on Telegram and do the following:
* press ``start``
* click ``new bot``
* enter a name
* enter a username (shown to others, ending in \`bot\`)
* copy and paste your token into a file called telegramtoken in your project folder
* if you want to use the bot in a group use ``/setprivacy`` (disabled) and ``/setjoingroups`` before adding it

### Get your pr0 token ###
You will need a normal user account on the platform for this. I dont have a bot account myself (yet).
* enter your username in the first line of a file called "pr0token"
* enter your password in the second line of the same file
* start the bot with an connected CLI or in an IDE
* When you first try to download a picture (send it as PN to the bot) you will need to fill in a captach
* the CLI will prompt for the context of your new captcha.png file
* If you enter the right captcha it will generate a cookie.json for further usage

### Running it with systemd ###
Once you have your cookie, you might want to run it with the provided service. You will need to make adjustments to it. 


## Be aware! ##
I provide this code and documentation without any warranty.
If you face any sort of negative effects for using this bot (like being blocked or worse) it's your fault.<br />
You may want to adjust the flags for the image_grabber to provide an unsafer environment.


## Licences of used Libraries ##
https://github.com/python-telegram-bot/python-telegram-bot/blob/master/LICENSE <br />
https://github.com/itssme/pypr0/blob/master/LICENSE <br />