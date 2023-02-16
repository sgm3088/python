import telebot
from telebot import types
import random

TOKEN = "5131762117:AAGewOGGWuis8QSYWKN8nmJiAvUtjMMlonI"
bot = telebot.TeleBot(TOKEN)

answer = ['птичка', 'кошка', 'собака', 'мясо', 'бутерброд', 'пулемет', 'человек', 'телефон', 'монета', 'котлета', 'геморой', 'ДА', 'НЕТ']
question = ['Вопрос1', 'Вопрос2', 'Вопрос3', 'Вопрос4', 'Вопрос5']
true_answer = {'Вопрос1': 'собака', 'Вопрос2': 'человек', 'Вопрос3': 'геморой', 'Вопрос4': 'котлета', 'Вопрос5': 'пулемет'}
answer_ok = 0
answer_not = 0
namb_ques = 0
test_or = False
real_message = ''

@bot.message_handler(commands=['start', 'help'])
def wellcame(message):
    test_or = False
    if not test_or:
        bot.reply_to(message, "Здравствуйте!!!")
    menu = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Если хотите пройти тест введите команду \n /test", reply_markup=menu)


@bot.message_handler(func=lambda w: True)
def start_bot(message):
    global test_or
    if message.text == "Hi":
        bot.reply_to(message, "Hi")
    elif message.text == "Привет":
        bot.reply_to(message, "Привет дорогой гость!")
    # elif message.from_user.id == 5073943531:
    #     bot.send_message(message.from_user.id, "Привет создатель")
    elif message.text == "/test":
        global  namb_ques
        change = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot_n = types.KeyboardButton("Да")
        bot_y = types.KeyboardButton("Нет")
        change.add(bot_y, bot_n)
        bot.send_message(message.from_user.id, "Хотите пройти тест", reply_markup=change)
    elif message.text == "Да":
        test_or = True
        message.text = "ДА"
        on_question(message)
    elif message.text == "Нет":
        message.text = 'help'
        wellcame(message)

    else:
        message.text = 'start'
        wellcame(message)

def on_question(message):
    print(message.text)
    global answer, namb_ques, test_or, answer_not, answer_ok

    if namb_ques == (len(question)-1):
        bot.send_message(message.from_user.id, f"Вы прошли тест -  правильных ответов {answer_ok} \nнеправильных ответов {answer_not}")
        test_or = False
        bot.register_next_step_handler(message, set_answer1)

    if message.text in answer and test_or:
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        for i in range(0, 5):
            set_bat = random.choice(answer)
            bat = types.KeyboardButton(set_bat)
            mark.add(bat)
        send_mes = f"Вот  вопрос {question[namb_ques]}?"
        bot.send_message(message.from_user.id, send_mes, parse_mode='html', reply_markup=mark)
        bot.register_next_step_handler(message, set_answer1)
    bot.send_message(message.from_user.id, "Выбирите ответ из меню...")


def set_answer1(message):
    change = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bot_n = types.KeyboardButton("Да")
    bot_y = types.KeyboardButton("Нет")
    change.add(bot_y, bot_n)
    bot.send_message(message.from_user.id, "Подтвердите ваш ответ....", reply_markup=change)
    bot.register_next_step_handler(message, call_send_answer1)

def call_send_answer1(message):
    global true_answer, namb_ques, question, answer_ok, answer_not
    if message.text == "Да":
        if true_answer[question[namb_ques]] == message.text:
            answer_ok += 1
        else:
            answer_not += 1
        message.text = "ДА"
        namb_ques += 1 if namb_ques < len(question)-1 else 0
        print(namb_ques)
        #bot.register_next_step_handler(call.message, question_one)
    elif message.text == "Нет":
        message.text = "НЕТ"
    on_question(message)







bot.polling(none_stop=True)