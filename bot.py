import telebot
from telebot import types

bot = telebot.TeleBot('TG-Bot-API-here')


@bot.message_handler(commands=['start'])
def start(message):
        mainmenu = types.InlineKeyboardMarkup(row_width=2)
        key1 = types.InlineKeyboardButton(text='USDT Ethereum', callback_data='USDT_E')
        key2 = types.InlineKeyboardButton(text='MATIC Polygon', callback_data='MATIC_P')
        key3 = types.InlineKeyboardButton(text='Contact us', url='tg-link')


        mainmenu.add(key1, key2, key3)
        bot.send_message(message.from_user.id, 'Welcome Message, blockchain choice', reply_markup=mainmenu)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    if call.data == "mainmenu":
        mainmenu = types.InlineKeyboardMarkup(row_width=2)
        key1 = types.InlineKeyboardButton(text='USDT Ethereum', callback_data='USDT_E')
        key2 = types.InlineKeyboardButton(text='MATIC Polygon', callback_data='MATIC_P')
        key3 = types.InlineKeyboardButton(text='Contact us', url='tg-link')

        mainmenu.add(key1, key2, key3)
        bot.edit_message_text('Blockchain choice back-menu message', call.message.chat.id, call.message.message_id,
                              reply_markup=mainmenu)

# ------------- ETHEREUM menu --------------

    elif call.data == "USDT_E":
        next_menu = types.InlineKeyboardMarkup(row_width=1)
        esch = types.InlineKeyboardButton(text='Department 1', callback_data='esc')
        edev = types.InlineKeyboardButton(text='Department 2', callback_data='edev')
        econs = types.InlineKeyboardButton(text='PromoService', callback_data='econs')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        next_menu.add(esch, edev, econs, back)
        bot.edit_message_text('Department choice message', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu)
                              
# ----------------- DEPARTMENT 1 -------------------
    elif call.data == "esc":
        next_menu3 = types.InlineKeyboardMarkup(row_width=2)
        elvl1 = types.InlineKeyboardButton(text='Service 1', callback_data='elvl1')
        elvl2 = types.InlineKeyboardButton(text='Service 2', callback_data='elvl2')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        next_menu3.add(elvl1, elvl2, back)
        bot.edit_message_text('Service choice message', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu3)
# Ethereum payment Service 1
    elif call.data == 'elvl1':
        pay_menu1 = types.InlineKeyboardMarkup(row_width=2)
        payelvl1 = types.InlineKeyboardButton(text='Payment', url='https://metamask.app.link/send/0x000')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        key3 = types.InlineKeyboardButton(text='Contact us', url='tg-link')
        pay_menu1.add(payelvl1, back, key3)
        bot.edit_message_text('Payment Confirmation Message', call.message.chat.id, call.message.message_id,
                              reply_markup=pay_menu1)

# Ethereum payment Service 2
    elif call.data == 'elvl2':
        pay_menu2 = types.InlineKeyboardMarkup(row_width=2)
        payelvl2 = types.InlineKeyboardButton(text='Payment', url='https://metamask.app.link/send/0x000')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        key3 = types.InlineKeyboardButton(text='Contact us', url='tg-link')
        pay_menu2.add(payelvl2, back, key3)
        bot.edit_message_text('Payment Confirmation Message', call.message.chat.id, call.message.message_id,
                              reply_markup=pay_menu2)

# Ethereum payment PromoService
    elif call.data == 'econs':
        pay_menu3 = types.InlineKeyboardMarkup(row_width=2)
        payecons = types.InlineKeyboardButton(text='Payment', url='https://metamask.app.link/send/0x000')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        key3 = types.InlineKeyboardButton(text='Contact us', url='tg-link')
        pay_menu3.add(payecons, back, key3)
        bot.edit_message_text('Payment Confirmation Message', call.message.chat.id, call.message.message_id,
                              reply_markup=pay_menu3)

# ----------------- DEPARTMENT 2 -------------------
    elif call.data == "edev":
        next_menu4 = types.InlineKeyboardMarkup(row_width=1)
        eft = types.InlineKeyboardButton(text='Service 3', callback_data='eft')
        enft = types.InlineKeyboardButton(text='Service 4', callback_data='enft')
        key3 = types.InlineKeyboardButton(text='Contact us', url='tg-link')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        next_menu4.add(eft, enft, key3, back)
        bot.edit_message_text('Service choice message', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu4)

# Ethereum payment Service 3
    elif call.data == 'eft':
        pay_menu4 = types.InlineKeyboardMarkup(row_width=2)
        payeft = types.InlineKeyboardButton(text='Payment', url='https://metamask.app.link/send/0x000')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        key3 = types.InlineKeyboardButton(text='Contact us', url='tg-link')
        pay_menu4.add(payeft, back, key3)
        bot.edit_message_text('Payment Confirmation Message', call.message.chat.id, call.message.message_id,
                              reply_markup=pay_menu4)

# Ethereum payment Service 4
    elif call.data == 'enft':
        pay_menu5 = types.InlineKeyboardMarkup(row_width=2)
        payenft = types.InlineKeyboardButton(text='Payment', url='https://metamask.app.link/send/0x000')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        key3 = types.InlineKeyboardButton(text='Contact us', url='tg-link')
        pay_menu5.add(payenft, back, key3)
        bot.edit_message_text('Payment Confirmation Message', call.message.chat.id, call.message.message_id,
                              reply_markup=pay_menu5)



# ------------- MATIC menu --------------

    elif call.data == "MATIC_P":
        matic_menu = types.InlineKeyboardMarkup(row_width=1)
        msch = types.InlineKeyboardButton(text='Department 1', callback_data='mschool')
        mdev = types.InlineKeyboardButton(text='Department 2', callback_data='mdev')
        mcons = types.InlineKeyboardButton(text='PromoService', callback_data='mcons')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        matic_menu.add(msch, mdev, mcons, back)
        bot.edit_message_text('Department choice message', call.message.chat.id, call.message.message_id,
                              reply_markup=matic_menu)
                              
# ----------------- DEPARTMENT 1 -------------------
    elif call.data == "mschool":
        matic_menu3 = types.InlineKeyboardMarkup(row_width=2)
        mlvl1 = types.InlineKeyboardButton(text='Service 1', callback_data='mlvl1')
        mlvl2 = types.InlineKeyboardButton(text='Service 2', callback_data='mlvl2')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        matic_menu3.add(mlvl1, mlvl2, back)
        bot.edit_message_text('Service choice message', call.message.chat.id, call.message.message_id,
                              reply_markup=matic_menu3)
# MATIC payment Service 1
    elif call.data == 'mlvl1':
        pay_menu1m = types.InlineKeyboardMarkup(row_width=2)
        payelvl1m = types.InlineKeyboardButton(text='Payment', url='https://metamask.app.link/send/0x000')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        key3 = types.InlineKeyboardButton(text='Contact us', url='tg-link')
        pay_menu1m.add(payelvl1m, back, key3)
        bot.edit_message_text('Payment Confirmation Message', call.message.chat.id, call.message.message_id,
                      reply_markup=pay_menu1m)

# MATIC payment Service 2
    elif call.data == 'mlvl2':
        pay_menu2m = types.InlineKeyboardMarkup(row_width=2)
        payelvl2m = types.InlineKeyboardButton(text='Payment', url='https://metamask.app.link/send/0x000')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        key3 = types.InlineKeyboardButton(text='Contact us', url='tg-link')
        pay_menu2m.add(payelvl2m, back, key3)
        bot.edit_message_text('Payment Confirmation Message', call.message.chat.id, call.message.message_id,
                      reply_markup=pay_menu2m)

# MATIC payment PromoService
    elif call.data == 'mcons':
        pay_menu3m = types.InlineKeyboardMarkup(row_width=2)
        payeconsm = types.InlineKeyboardButton(text='Payment', url='https://metamask.app.link/send/0x000')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        key3 = types.InlineKeyboardButton(text='Contact us', url='tg-link')
        pay_menu3m.add(payeconsm, back, key3)
        bot.edit_message_text('Payment Confirmation Message', call.message.chat.id, call.message.message_id,
                      reply_markup=pay_menu3m)

# ----------------- DEPARTMENT 2 -------------------
    elif call.data == "mdev":
        matic_menu4 = types.InlineKeyboardMarkup(row_width=1)
        mft = types.InlineKeyboardButton(text='Service 3', callback_data='mft')
        mnft = types.InlineKeyboardButton(text='Service 4', callback_data='mnft')
        key3 = types.InlineKeyboardButton(text='Contact us', url='tg-link')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        matic_menu4.add(mft, mnft, key3, back)
        bot.edit_message_text('Service choice message', call.message.chat.id, call.message.message_id,
                              reply_markup=matic_menu4)

# MATIC payment Service 3
    elif call.data == 'mft':
        pay_menu4m = types.InlineKeyboardMarkup(row_width=2)
        paymft = types.InlineKeyboardButton(text='Payment', url='https://metamask.app.link/send/0x000')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        key3 = types.InlineKeyboardButton(text='Contact us', url='tg-link')
        pay_menu4m.add(paymft, back, key3)
        bot.edit_message_text('Payment Confirmation Message', call.message.chat.id, call.message.message_id,
                      reply_markup=pay_menu4m)

# MATIC payment Service 4
    elif call.data == 'mnft':
        pay_menu5m = types.InlineKeyboardMarkup(row_width=2)
        paymnft = types.InlineKeyboardButton(text='Payment', url='https://metamask.app.link/send/0x000')
        back = types.InlineKeyboardButton(text='Back', callback_data='mainmenu')
        key3 = types.InlineKeyboardButton(text='Contact us', url='tg-link')
        pay_menu5m.add(paymnft, back, key3)
        bot.edit_message_text('Payment Confirmation Message', call.message.chat.id, call.message.message_id,
                      reply_markup=pay_menu5m)



bot.polling(none_stop=True, interval=0)