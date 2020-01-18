import requests
import re
from telebot import TeleBot, types


bot = TeleBot("631973776:AAExMI5_dAPqlaXHnWgJjKXixX7Y7ndp_Vg")


@bot.message_handler()
def define(message):
    definition = requests.get(
        f"http://api.urbandictionary.com/v0/define?term={message.text}"
    ).json()["list"]
    output = "\n\n".join([d["definition"] for d in definition])
    bot.reply_to(message, output)

    pattern = r"\[.*?\]"
    words = re.findall(pattern, output)

    markup = types.ReplyKeyboardMarkup(row_width=1)
    for word in words:
        markup.add(types.KeyboardButton(word.strip("[]")))
    bot.send_message(message.chat.id, "Look up for words in brackets:",
                     reply_markup=markup)


if __name__ == "__main__":
    bot.polling()