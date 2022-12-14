# Copyright Beyond ML and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import responses
import settings
import telebot


bot = telebot.TeleBot(settings.BOT_TOKEN, parse_mode="markdown")


@bot.message_handler(chat_types=["group", "private", "supergroup"], content_types=["location"])
def send_weather(message: telebot.types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    bot.reply_to(message, responses.get_weather(lat, lon), disable_web_page_preview=True)


def main():
    bot.infinity_polling()


if __name__ == "__main__":
    main()
