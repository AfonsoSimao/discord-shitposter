# discord-shitposter
An experimental implementation of a discord bot using discord.py.

# Configuration
The following files should be added to the Configs folder:

1. MyCreds.py with DiscordAdamToken = <your_bot_token>. For MAL functionality also add MALUser = <your_mal_username> and MALPassword = <your_mal_password>

2. Constants.py with ADMIN_NAME = <your_discord_username>. Note that this should be your actual username and not your server nickname.

3. ImageFolders.py with the following:

- REACTION_FOLDER = '_media/Images/<reaction_folder_name>'
- NO_FOLDER = '_media/Images/<no_folder_name>'
- SLEEP_FOLDER = '_media/Images/<sleep_folder_name>'
- SORRY_FOLDER = '_media/Images/<sorry_folder_name>'
- SMUG_FOLDER = '_media/Images/<smug_folder_name>'
- POLL_FOLDER = '_media/Images/<poll_folder_name>'

The above mentioned paths should contain the images for the Greentext and Polls modules and the permission check responses to use.
