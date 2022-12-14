![meteum](https://user-images.githubusercontent.com/11780431/202411607-6c5174a4-4e99-47d7-b5f9-1e6d797e5c2c.png)

# Meteum Telegram Bot [![Telegram](https://img.shields.io/badge/@MeteumBot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/MeteumBot)

This is a simple example of using the Meteum API to creating a Telegram chat bot.

If you are looking for a more in-depth guide and reference for the Meteum GraphQL API, please refer to [documentation](https://docs.meteum.ai).

## Getting started

Before launching this project, you should create a chatbot using @BotFather, following the [instructions](https://core.telegram.org/bots#how-do-i-create-a-bot).

Here are the next steps for bot quick launch:

1. Register and get free trial at [Meteum website](https://meteum.ai/b2b/console/home).
1. Install Python from the [official website](https://www.python.org/downloads/).
1. Install [Pipenv via pip](https://docs.pipenv.org/install/#installing-pipenv).
1. Clone or download this repository.

    ```bash
    git clone https://github.com/meteum-ai/meteum-telegram-bot.git
    ```

1. Prepare environment and install dependencies.

    ```bash
    # Meteum API token. Don't hesitate to use our free trial.
    echo API_TOKEN=... > .env  

    # The bot token that you received from BotFather.
    echo BOT_TOKEN=... >>.env
    ```

1. Run the bot.

    ```bash
    pipenv run python bot.py
    ```
