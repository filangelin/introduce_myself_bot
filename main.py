from telebot import TeleBot, types

bot = TeleBot(token="")

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row(
    types.KeyboardButton(text='Мои фото'),
    types.KeyboardButton(text='Мои болталки'),
)
keyboard.row(
    types.KeyboardButton(text='Моё главное увлечение'),
)


@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=message.from_user.first_name + ', привет! А меня зовут Ангелина, здесь ты сможешь получше меня узнать☺️\n'
                                            'P.S. посмотреть на внутрянку бота - /hack',
        reply_markup=keyboard
    )


@bot.message_handler(commands=['hack'])
def start_command_handler(message: types.Message):
    git = "https://github.com/filangelin/introduce_myself_bot"
    bot.send_message(

        chat_id=message.chat.id,
        text=f'Лови ссылку на исходники: <code>{git}</code>',
        reply_markup=keyboard
    )


@bot.message_handler()
def message_handler(message: types.Message):
    if message.text == 'Мои фото':
        bot.send_message(
            chat_id=message.chat.id,
            text=f'Фото с периода лета между 10 и 11 классом')
        bot.send_photo(chat_id=message.chat.id, photo=open('img/sch.png', 'rb'))
        bot.send_message(
            chat_id=message.chat.id,
            text=f'Последнее селфи')
        bot.send_photo(chat_id=message.chat.id, photo=open('img/photo.jpg', 'rb'))
    elif message.text == 'Мои болталки':
        bot.send_message(
            chat_id=message.chat.id,
            text=f'Что такое gpt "для бабушки:"')
        bot.send_audio(chat_id=message.chat.id, audio=open('audio/gpt.ogg', 'rb'))
        bot.send_message(
            chat_id=message.chat.id,
            text=f'Разница между SQL и NoSQL:')
        bot.send_audio(chat_id=message.chat.id, audio=open('audio/sql_nosql.ogg', 'rb'))
        bot.send_message(
            chat_id=message.chat.id,
            text=f'Первая влюбленность❤️')
        bot.send_audio(chat_id=message.chat.id, audio=open('audio/first_l.ogg', 'rb'))
    elif message.text == 'Моё главное увлечение':
        bot.send_message(
            chat_id=message.chat.id,
            text=f'Моё главное увлечение - цикл романов в жанре фэнтези "Меч истины". Это цикл из 24 книг, представляешь? '
                 f'Моя любовь к этой вселенной начлась еще со времен школы и продолжается до сих пор:) Кроме увлекательнейшего '
                 f'сюжета, боатого мира с интересными персонажами очень много философии и моральных уроков. Я не просто читаю '
                 f'эти книги, я ими зачитываюсь."'
        )


bot.polling()
