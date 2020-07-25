# discord-shitposter
An experimental implementation of a discord bot using discord.py.

#Installation
Python 3.5.3 or higher is required.

Download the repo, install the requirements...

```pip install -r requirements.txt```

...then run CommandsAdam.py.

# Configuration
The following files should be added to the Configs folder:

1. MyCreds.py with DiscordAdamToken = <your_bot_token>. For MAL functionality also add MALUser = <your_mal_username> and MALPassword = <your_mal_password>

2. Constants.py with ME = <your_discord_id>. Can be set to any int if you're the owner of the bot. If, for some reason, you're not the owner of the bot, setting this constant will allow your user to still pass isMaster() Checks

3. ImageFolders.py with the following:

```
REACTION_FOLDER = '_media/Images/<reaction_folder_name>'
NO_FOLDER = '_media/Images/<no_folder_name>'
SLEEP_FOLDER = '_media/Images/<sleep_folder_name>'
SORRY_FOLDER = '_media/Images/<sorry_folder_name>'
SMUG_FOLDER = '_media/Images/<smug_folder_name>'
POLL_FOLDER = '_media/Images/<poll_folder_name>'
```

The above mentioned paths should contain the images for the Greentext and Polls modules and the permission check responses to use.
