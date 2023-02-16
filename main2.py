
from telebot import types
import telebot
TOKEN = "5131762117:AAGewOGGWuis8QSYWKN8nmJiAvUtjMMlonI"
bot = telebot.TeleBot(TOKEN, parse_mode=None)
seton = False
setonBD = False
dataBD = ('ФИО преподавателя', 'Наименование программы','Время занятий')
fio_prep = ['Русков Герман Юрьевич', 'Михайлов Сергей Геннадьевич']
name_prog = ['']
kvant_set = ('Биоквантум', 'IT - квантум', 'Наноквантум','Энерджиквантум', 'VR/AR – квантум', 'Хайтек квантум»', 'Математика»', 'Английский язык', 'Шахматы')
name_set = ''
day_set = ''
times_set = ''
group = {'Углубленная','Базовая'}
weekdays = {'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'}
times = ['8:30-9:15', '9:30-10:15', '15:00-15:45', '16:00-16:45', '17:00-18:45', '17:00-19:45']
key_set = {'ON', 'OFF'}
admin = ['5073943531', 'Сергей']



@bot.callback_query_handler(func=lambda c:True)
def cbinline(c):
	global seton, setonBD
	if c.data == "us_yes":
		markup = types.InlineKeyboardMarkup()

		send_mess = f"<b>Далее</b>!\n Выбери квантум в меню"

		menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		for f in kvant_set:
			menu.add(types.KeyboardButton(f))
		bot.send_message(c.message.chat.id, send_mess,
						 parse_mode='html', reply_markup=menu)

	elif c.data == "us_no":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Посетить группу Вк", url="https://vk.com/prog_life"))
		bot.send_message(c.message.chat.id, "Нажмите на кнопку ниже и погрузитесь в мир IT прямо сейчас",
						 parse_mode='html', reply_markup=markup)

	elif c.data == "bd_no":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		for f in dataBD:
			markup.add(types.KeyboardButton(f))
		send_mess = f"<b>Выбирите </b>!\n Какие данные вы хотите поменять?"
		bot.send_message(c.message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

	elif c.data == "bd_yes":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		for f in dataBD:
			markup.add(types.KeyboardButton(f))
		send_mess = f"<b>Выбирите </b>!\n Какие данные вы хотите поменять?"
		bot.send_message(c.message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

	else:
		send_mess = f"<b>Привет</b>!\n Что вы хотели?"
		bot.send_message(c.message.chat.id, send_mess, parse_mode='html')
		key = types.InlineKeyboardMarkup(row_width=3)
		but_1 = types.InlineKeyboardButton(text="/start", callback_data='No')
		but_2 = types.InlineKeyboardButton(text="/stop", callback_data='hj')
		key.add(but_1, but_2)
		bot.send_message(c.message.chat.id, "Вы выбрали.\n<b>Что-то:</b>",
						 parse_mode='html', reply_markup=key)

		bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id,
									  reply_markup=key)
		#bot.answer_callback_query(c.id)

@bot.message_handler(commands=['setdata'])
def set_datainb(message):
	global name_set, seton
	if str(message.from_user.id) in admin and seton:
		markup = types.InlineKeyboardMarkup(row_width=2)
		markup.add(types.InlineKeyboardButton("Yes", callback_data="bd_yes"),
				   types.InlineKeyboardButton("No", callback_data="bd_no"))
		send_mess = f"<b>Выбирите </b>!\n Вы хотите внести изменения в  BD?"
		bot.send_message(message.chat.id, send_mess,
						 parse_mode='html', reply_markup=markup)


def cler_menu():
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add(types.KeyboardButton("Выйти"))


@bot.message_handler(commands=['admin'])
def open_admin(message):
	global name_set, seton
	if str(message.from_user.id) in admin and message.from_user.first_name in admin:
		bot.send_message(message.from_user.id, 'Привет, великий!')
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

		for f in fio_prep:
			markup.add(types.KeyboardButton(f))
		send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\n Выбери ФИО Преподавателя"
		bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
		name_set = markup
		seton = True
	else:
		bot.send_message(message.from_user.id, 'Пшел вон! незванный')
		cler_menu()

@bot.message_handler(commands=['vk'])
def vk(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Посетить группу Вк", url="https://vk.com/prog_life"))
	bot.send_message(message.chat.id, "Нажмите на кнопку ниже и погрузитесь в мир IT прямо сейчас", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
	markup = types.InlineKeyboardMarkup(row_width=2)
	markup.add(types.InlineKeyboardButton("Хотите посмотреть квантумы", callback_data="kv"))
	markup.add(types.InlineKeyboardButton("Yes", callback_data="us_yes"),
			   types.InlineKeyboardButton("No", callback_data="us_no"))
	bot.send_message(message.chat.id,
					 "Отличный выбор, нажмите на кнопку ниже и начинайте изучения курсов прямо сейчас",
					 parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
	global name_set, seton
	get_message_bot = message.text
	print(get_message_bot)

	if get_message_bot in fio_prep and seton:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		for f in weekdays:
			markup.add(types.KeyboardButton(f))
		send_mess = f"<b>Далее</b>!\n Выбери день недели"
		bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
		day_set = markup

	elif get_message_bot in weekdays and seton:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		for f in times:
			markup.add(types.KeyboardButton(f))
		send_mess = f"<b>Далее</b>!\n Выбери время занятия"
		bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
		times_set = markup

	elif get_message_bot in times and seton:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		for f in group:
			markup.add(types.KeyboardButton(f))
		send_mess = f"<b>Далее</b>!\n Выбери группу"
		bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

	elif get_message_bot in group and seton:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		for f in key_set:
			markup.add(types.KeyboardButton(f))
		send_mess = f"<b>Далее</b>!\n Установите значение"
		bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

	elif get_message_bot == "ON" or get_message_bot == "OFF" and seton:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
		#markup.add(types.KeyboardButton('', callback_data='N'))
		bot.send_message(message.chat.id, '', parse_mode='html', reply_markup=markup)
		seton = False

	else:
		send_mess = f"<b>Привет</b>!\nЧто вы хотели?"
		bot.send_message(message.chat.id, send_mess, parse_mode='html')
		key = types.InlineKeyboardMarkup(row_width=3)
		but_1 = types.InlineKeyboardButton(text="/start", callback_data='N')
		but_2 = types.InlineKeyboardButton(text="/stop", callback_data='S')
		key.add(but_1, but_2)
		bot.send_message(message.chat.id, "",
						 parse_mode='html', reply_markup=key)



bot.polling(none_stop=True)

#bot.infinity_polling()

