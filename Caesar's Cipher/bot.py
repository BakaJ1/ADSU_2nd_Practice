import telebot
import config
import Caesar
from telebot import types


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('caesar_p.PNG', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Расшифровать")
    item2 = types.KeyboardButton("Зашифровать")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\n"
                                      "Имя мне - <b>{1.first_name}</b>.\n"
                                      "Интересуешься моим шифром? Тогда ты пришел по адресу!\n"
                                      "Вот новенький циркуляр Б-65 с моими командами:\n"
                                      "<b><I><u>Зашифровать</u></I></b> - с помощью моего АБСОЛЮТНО надежного алгоритма я зашифрую твое послание так, что его никто не разберет. <S>Я так думаю...</S>\n"
                                      "<b><I><u>Расшифровать</u></I></b> - ЧТО!? Кто-то зашифровал послание моим алгоритмом? Возмутительно! Давай восстановим оригинальное послание и накажем наглого подражателя!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)



user_data = {}

@bot.message_handler(func=lambda message: message.chat.type == 'private' and message.text in ['Расшифровать', 'Зашифровать'])
def handle_initial_message(message):
    chat_id = message.chat.id
    if message.text == 'Расшифровать':
        user_data[chat_id] = {'action': 'decrypt'}
        bot.send_message(chat_id, "📝Записываю... Введите текст для расшифровки и следом за ним коэффициент смещения:")
    elif message.text == 'Зашифровать':
        user_data[chat_id] = {'action': 'encrypt'}
        bot.send_message(chat_id, "📝Записываю... Введите текст для шифрованияи следом за ним коэффициент смещения:")


@bot.message_handler(func=lambda message: message.chat.id in user_data and 'action' in user_data[message.chat.id])
def handle_text_message(message):
    chat_id = message.chat.id
    user_input_raw = message.text.split(' ')
    user_input = ['', '']
    for i in range(len(user_input_raw)):
        try:
            temp = int(user_input_raw[i])
            user_input[1] = str(temp)
        except:
            user_input[0] += user_input_raw[i] + ' '
    if len(user_input) < 2:
        user_input.append('8')
    if user_input[1] == '':
        user_input[1] = '8'

    action = user_data[chat_id]['action']

    if action == 'decrypt':
        answer = Caesar.caesar_alg(text=user_input[0], caesar_coefficient=int(user_input[1]))
        decrypted_text = answer.DEcrypt()
        bot.send_message(chat_id, decrypted_text)
    elif action == 'encrypt':
        answer = Caesar.caesar_alg(text=user_input[0], caesar_coefficient=int(user_input[1]))
        encrypted_text = answer.ENcrypt()
        bot.send_message(chat_id, encrypted_text)

    del user_data[chat_id]


bot.polling(none_stop=True)


#t.me/ADSU_Caesar_bot