## Server information bot
This bot provides server information for your Discord server. Users can use a command to get detailed information about the server, including the number of members, roles, channels, and more. The bot sends an embedded message with the server details when the command is triggered.

## Features
- Server details: Fetches and displays various server statistics such as member count, owner, and more.
- Channel count: Displays counts for different types of channels (text, voice, stage, forum, etc.).
- Boosts and roles: Shows the number of server boosts and roles.
- Active threads: Lists the number of active threads in the server.
- Media channels: Displays the number of media channels (news channels).

![P2xXF1JLAf](https://github.com/user-attachments/assets/330153ab-38b7-4b5a-b353-710bfdab28ef)

## Requirements
- Programming Language: Python
- Required Libraries: disnake (for interacting with Discord's API)
Install the required libraries using pip:
```
pip3 install disnake
```

## Setup
1. Create a bot on Discord:
- Go to the [Discord Developer Portal](https://discord.com/developers).
- Create a new application, then create a bot and obtain the bot token.
- Replace the placeholder `INSERT-TOKEN` in the code with your bot token.
2. Configure the bot:
- No specific configuration is required for this bot as it fetches data dynamically from the server.
3. Install Dependencies:
- On your machine, ensure Python 3.8+ is installed. You can check this by running:
```
python3 --version
```
- Install pip if it's not installed:
```
sudo apt install python3-pip
```
- Install the required libraries with pip:
```
pip3 install disnake
```
4. Run the bot:
- You can run the bot using the following command:
```
python3 app.py
```
Make sure you are in the same directory as the `app.py` file or provide the full path to it.

## How to Use
- Deploy: Clone the repository and configure your bot with the bot token.
- Run: Launch the bot on your server.
- Interaction: Users can invoke the `/server` command to get information about the server.

## Links
[Boosty developer](https://boosty.to/mao-mao)

[GitHub](https://github.com/rinnyuwu)

[Donation Alerts](https://www.donationalerts.com/r/rinnyuwu)
