# Discord Bot

A simple Discord bot that performs various tasks based on user commands.

## Features

- Responds to user commands
- Customizable thread IDs
- Supports multiple functionalities (add features as necessary)

## Getting Started

Follow these steps to set up the project on your local machine:
- To run this bot

### Prerequisites

- Python 3.x installed
- Pip (Python package installer)

### Clone the Repository

bash:
- git clone https://github.com/akshatggupta/Discord_bot.git
- cd Discord_bot

### Configure resources.py:

Open the resources.py file
- add your desired thread names
-  their corresponding Discord thread IDs in the resources dictionary. For example:
resources = {
    "AI": 1289527408709341286,
    "Web Development": 1289573446434422914,}
    - Add more threads as needed

### Create a .env file in the root directory of the project and add your Discord bot token:
- DISCORD_TOKEN=your_bot_token_here
- THREAD_ID=your_thread_id_here

### To start the bot, run:
python Elixir_bot.py

