from telebot import types
import telebot
import requests
import json
import urllib
import os



TOKEN = "5131762117:AAGewOGGWuis8QSYWKN8nmJiAvUtjMMlonI"
bot = telebot.TeleBot(TOKEN, parse_mode=None)
local_path: str = r"C:\Users\User_PC\PycharmProjects"
obmen = {'in': '', 'out': ''}





@bot.message_handler(commands=['start'])
def command_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    k1 = types.KeyboardButton("Курс")
    k2 = types.KeyboardButton("График")
    k3 = types.KeyboardButton("Уведомления")
    k4 = types.KeyboardButton("Обмен")
    k5 = types.KeyboardButton("Кошелек")
    k6 = types.KeyboardButton("Биржа")

    markup.add(k1, k2, k3, k4, k5, k6)

    bot.send_message(message.chat.id, "Привет. Я КриптоБот. Используй клавиатуру ниже")
    bot.send_message(message.chat.id, "Готово ✓", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Курс":
        #j = requests.get(api)
        #data = json.loads(j.text)
        bot.send_message(message.chat.id, f"Курс биткоина на 20.12.22: <b>{data['USD']}$</b> ", parse_mode='html')

    elif message.text == "График":
        #urllib.request.urlretrieve(URL_PHOTO, local_path)
        #img = open(local_path, 'rb')
        bot.send_message(message.chat.id, "")
        #os.remove(local_path)


    elif message.text == "Обмен":
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Bitcoin", callback_data="Bitcoin")
        but_2 = types.InlineKeyboardButton(text="Litecoin", callback_data="Litecoin")
        but_3 = types.InlineKeyboardButton(text="Ethereum", callback_data="Ethereum")
        but_4 = types.InlineKeyboardButton(text="Tether USDT", callback_data="Tether USDT")
        but_5 = types.InlineKeyboardButton(text="Монобанк ГРН", callback_data="Приват 24 ГРН")
        but_6 = types.InlineKeyboardButton(text="Альфа-Банк ГРН", callback_data="Альфа-Банк ГРН")
        but_7 = types.InlineKeyboardButton(text="Альфа-Банк РУБ", callback_data="Альфа-Банк РУБ")
        but_8 = types.InlineKeyboardButton(text="YooMoney", callback_data="YooMoney")
        but_9 = types.InlineKeyboardButton(text="Qiwi", callback_data="Qiwi")


        key.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9)
        bot.send_message(message.chat.id, "Поиск выгодных обменников в реальном времени.\n<b>Что хотите  отдать:</b>",
                         parse_mode='html', reply_markup=key)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "Bitcoin":
            obmen['in'] = "Bitcoin"
            key = types.InlineKeyboardMarkup(row_width=2)
            but_1 = types.InlineKeyboardButton(text="Litecoin", callback_data="Litecoin")
            but_2 = types.InlineKeyboardButton(text="Ethereum", callback_data="Ethereum")
            but_3 = types.InlineKeyboardButton(text="СберБанк", callback_data="СберБанк")
            but_4 = types.InlineKeyboardButton(text="Tether USDT", callback_data="Tether USDT")
            but_5 = types.InlineKeyboardButton(text="Монобанк ГРН", callback_data="Монобанк ГРН")
            but_6 = types.InlineKeyboardButton(text="Альфа-Банк ГРН", callback_data="Альфа-Банк ГРН")
            but_7 = types.InlineKeyboardButton(text="Альфа-Банк РУБ", callback_data="Альфа-Банк РУБ")
            but_8 = types.InlineKeyboardButton(text="YooMoney", callback_data="YooMoney")
            but_9 = types.InlineKeyboardButton(text="Qiwi", callback_data="Qiwi")

            key.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9)
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          reply_markup=key)
            bot.answer_callback_query(call.id)


    if call.message:

        if call.data == "Bitcoin":
            bot.answer_callback_query(call.id)
            obmen['out'] = "Bitcoin"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"Обменники: [перейти {obmen['in']} > {obmen['out']}](https://www.bestchange.ru/{obmen['in'].lower()}-to-{obmen['out'].lower()})",
                                  parse_mode='Markdown', reply_markup=None)
            obmen['in'], obmen['out'] = '', ''

        elif call.data == "Litecoin":
            bot.answer_callback_query(call.id)
            obmen['out'] = "Litecoin"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"Обменники: [перейти {obmen['in']} > {obmen['out']}](https://www.bestchange.ru/{obmen['in'].lower()}-to-{obmen['out'].lower()})",
                                  parse_mode='Markdown', reply_markup=None)
            obmen['in'], obmen['out'] = '', ''


bot.polling(none_stop=True)