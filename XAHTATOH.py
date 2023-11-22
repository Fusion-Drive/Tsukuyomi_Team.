import telebot
import time
from telebot import types
bot=telebot.TeleBot("6962793166:AAHBBfDTPwxDvgNdpjm1qqFvADL7XItHJYc")

@bot.message_handler(commands=["start"])
def welcome(message):
    mess=f"Приветсвую,{message.from_user.first_name}"
    bot.send_message(message.chat.id,mess,reply_markup = markup,parse_mode="html")


btn1 = types.KeyboardButton("Мероприятия Парка")
btn2 = types.KeyboardButton("Услуги Парка")
btn8 = types.KeyboardButton("Конкурсы")
btn3 = types.KeyboardButton("Как стать резидентом Технопарка Югры")

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

markup.add(btn1,btn2,btn3)

markup.add(btn8)



@bot.message_handler(content_types=['text'])
def victim(message):
    if message.text=="Мероприятия Парка":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(" тык!", url='https://www.tp86.ru/press-centr/news/')
        markup.add(button1)
        bot.send_message(message.chat.id," Все ближайшие мероприятия".format(message.from_user),reply_markup=markup)
    elif message.text=="Конкурсы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Конкурс «Акселератор технологических стартапов»")
        btn2 = types.KeyboardButton("Конкурс УМНИК")
        btn3 = types.KeyboardButton("Конкурс Молодой изобретатель Югры")
        back=types.KeyboardButton("Назад")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(back)
        bot.send_message(message.chat.id, 'Вы першли во вкладку "Конкурсы"', reply_markup=markup)
        bot.send_message(message.chat.id, 'Какой конкурс вам интересен?', reply_markup=markup)
        if message.text=="Конкурс «Акселератор технологических стартапов»":
            markup = types.InlineKeyboardMarkup()
            button4 = types.InlineKeyboardButton("тык!", url='https://www.tp86.ru/molodoy-izobretatel-yugry/index.php')
            markup.add(button4)
        elif message.text=="Конкурс УМНИК":
            markup = types.InlineKeyboardMarkup()
            button5 = types.InlineKeyboardButton("тык!", url='https://www.tp86.ru/press-centr/news/39528/?ysclid=lp88jrsf2w967306183')
            markup.add(button5)
            bot.send_message(message.chat.id,"Информация о конкурсе «УМНИК»".format(message.from_user),reply_markup=markup) 
        elif message.text=="Конкурс Молодой изобретатель Югры":
            markup = types.InlineKeyboardMarkup()
            button6 = types.InlineKeyboardButton("тык!", url='https://www.tp86.ru/press-centr/news/39533/?ysclid=lp88eblj74476182406')
            markup.add(button6)
            bot.send_message(message.chat.id,"«Информация о конкурсе «Молодой изобретатель Югры".format(message.from_user),reply_markup=markup)
        elif message.text=="Назад":
            btn1 = types.KeyboardButton("Мероприятия Парка")
            btn2 = types.KeyboardButton("Услуги Парка")
            btn8 = types.KeyboardButton("Конкурсы")
            btn3 = types.KeyboardButton("Как стать резидентом Технопарка Югры")



        
    elif message.text=="Услуги Парка":
        markup = types.InlineKeyboardMarkup()
        button2 = types.InlineKeyboardButton("тык!", url='https://www.tp86.ru/services/services/')
        markup.add(button2)
        bot.send_message(message.chat.id," Государственные услуги".format(message.from_user),reply_markup=markup)
        
    elif message.text=="Как стать резидентом Технопарка Югры":
        markup = types.InlineKeyboardMarkup()
        button3 = types.InlineKeyboardButton("тык!", url='https://www.tp86.ru/residents/add/')
        markup.add(button3)
        bot.send_message(message.chat.id," Как стать резидентом Технопарка Югры".format(message.from_user),reply_markup=markup)
        
          
        
    



bot.polling(non_stop=True)         




