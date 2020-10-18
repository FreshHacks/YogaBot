import telebot # telegram api

bot = telebot.TeleBot("1272739117:AAF0yvdDTqPuaog3G25M4zCLYRYy8LuVMu0") # bot connect token

# "/start" command
@bot.message_handler(commands=['start', 'help']) # decorator command start with help alias
def start(message):
	bot.send_message(message.chat.id, """
		<b>Найчастіші запитання</b>
		<b>1</b> - Які види йоги викладаються/практикуються?
		<b>2</b> - Де знаходиться студія?
		<b>3</b> - Хто інструктор?
		<b>4</b> - Як із Вами зв'язатись?
		<b>5</b> - Який розклад занять?
		<b>6</b> - Чи потрібно записуватись заздалегідь і як це зробити?
		<b>7</b> - Що потрібно взяти із собою?
		<b>8</b> - Скільки коштує разове заняття?
		<b>9</b> - Якщо я початківець, в який час мені краще приходити? Чи є групи для початківців?
		<b>10</b> - Чи є обмеження за віком/статтю?
		<b>11</b> - У мене є хронічні захворювання, чи можна мені займатись?
	""", parse_mode='html') # Send message, disabling markdown mode, enabling html parse_mode


@bot.message_handler(content_types=['text'])
def msg_handle(message):
	if message.text == "1": # If code of question is 1
		bot.reply_to(message, "Відповідь на запитання <b>1</b>: \nХатха-йога, аштанга-йога.", parse_mode = "HTML")

	elif message.text == "2": # If code of question is 2
		bot.reply_to(message, "Відповідь на запитання <b>2</b>: \nТетріс (колишній Інфракон), вулиця Київська, 16, 5й поверх, кімната 517.", parse_mode = "HTML")

	elif message.text == "3": # If code of question is 3
		bot.reply_to(message, 'Відповідь на запитання <b>3</b>: \nЮрій Чепелюк, стаж роботи - з 2011 року, <a href = "https://facebook.com/samvar2/">FB</a>', parse_mode = "HTML")

	elif message.text == "4": # If code of question is 4
		bot.reply_to(message, "Відповідь на запитання <b>4</b>: \nТелефон (вайбер) інструктора: +38 093 993 2170. Телефон (вайбер) адміністратора: +38 68 308 0299.", parse_mode = "HTML")

	elif message.text == "5": # If code of question is 5
		bot.reply_to(message, """
			Відповідь на запитання <b>5</b>: 
			Понеділок: 9:30 - 10:30; 18:00 - 18:55; 19:00 - 20:30. 
			Вівторок:  7:00 - 8:55;  9:00 -  10:00; 18:00 - 18:55; 19:00 - 20:30. 
			Середа:    9:30 - 10:30; 18:00 - 18:55; 19:00 - 20:30. 
			Четвер:    7:00 - 8:55;  9:00 -  10:00; 18:00 - 18:55; 19:00 - 20:30. 
			П'ятниця:  9:30 - 10:30; 18:00 - 18:55; 19:00 - 20:30. 
			Субота:    9:00 - 11:00.
			Неділя:    9:00 - 11:00.
			""", parse_mode = "HTML")

	elif message.text == "6": # If code of question is 6
		bot.reply_to(message, "Відповідь на запитання <b>6</b>: \nТак, бажано записуватись заздалегідь, - так ми можемо контролювати кількість відвідувачів (відповідно до карантинних вимог). Записатись можна, надіславши повідомлення (вайбер,смс) на номери +38 093 993 2170 (інструктор), +38 68 308 0299 (адміністратор).", parse_mode = "HTML")

	elif message.text == "7": # If code of question is 7
		bot.reply_to(message, "Відповідь на запитання <b>7</b>: \nЗручний одяг (футболка, що не падатиме на голову при нахилах; штани, що не тиснутимуть в талії; шкарпетки, хоча краще босоніж :) ). Якщо маєте власний килимок - беріть його також. Хоча, за потреби, у нас завжди знайдеться вільний килимок :). Вода - за бажанням.", parse_mode = "HTML")

	elif message.text == "8": # If code of question is 8
		bot.reply_to(message, "Відповідь на запитання <b>8</b>: \nВартість разового відвідування - 70,00 гривень.", parse_mode = "HTML")

	elif message.text == "9": # If code of question is 9
		bot.reply_to(message, "Відповідь на запитання <b>9</b>: \nЧи є групи для початківців? Окремих занять для початківців немає - можна приєднатись до будь-якої з груп, інструктор під час заняття буде коригувати Ваше навантаження. Заняття на 09:00, 09:30 та на 18:00 мають тривалість 55 хвилин, відповідно, навантаження в цих групах дещо менше.", parse_mode = "HTML")

	elif message.text == "10": # If code of question is 10
		bot.reply_to(message, 'Відповідь на запитання <b>10</b>: \nНі, немає обмежень за віком, на заняттях успішно займаються поруч і ті, кому за 60 років, і підлітки. Також немає обмежень за статтю: групи мішані, чоловіки/хлопці та жінки/дівчата разом. Окремих "дівчачих" або "чоловічих" груп немає.', parse_mode = "HTML")

	elif message.text == "11": # If code of question is 11
		bot.reply_to(message, "Відповідь на запитання <b>11</b>: \nУ кожному конкретному випадку рішення про доцільність заняття йогою інструктор приймає під час особистої розмови із відвідувачем. Наберіть інструктора для отримання детальної інформації +38 093 993 2170.", parse_mode = "HTML")

	else: # If answer is unknown
		bot.reply_to(message, "Неправильне запитання. Список: /help")


# Bot start
if __name__ == '__main__': # If file starting as main
     bot.polling(none_stop=True) # Bot polling