from requests import get
import json
import telebot
from telebot import types
from bs4 import BeautifulSoup
import time
bot=telebot.TeleBot("6962793166:AAHBBfDTPwxDvgNdpjm1qqFvADL7XItHJYc")
a=get("https://www.tp86.ru/press-centr/news/")
postTitless=[]
linkss=[]
r = get('https://www.tp86.ru/press-centr/news/')
@bot.message_handler(commands=["start"])
def welcome(message):
    mess=f"Приветсвую,{message.from_user.first_name}"
    bot.send_message(message.chat.id,mess,reply_markup = markup,parse_mode="html")


btn1 = types.KeyboardButton("Мероприятия Парка")
btn2 = types.KeyboardButton("Услуги Парка")
btn8 = types.KeyboardButton("Конкурсы")
btn3 = types.KeyboardButton("Как стать резидентом Технопарка Югры")

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

markup.add(btn1,btn2,btn3,btn8)



@bot.message_handler(content_types=['text'])
def victim(message):
    markup = types.InlineKeyboardMarkup()
    if message.text=="Мероприятия Парка":
        soup = BeautifulSoup(r.content, "html.parser")
        postTitles = soup.find_all("p", class_="news-element_text-prew")
        links=soup.find_all("a", class_="news-element news__list_item")
        for title in postTitles:
            if len(postTitless)==5:
                break
            else:
                postTitless.append(title.text.strip())
        for link in links:
            if len(linkss)==5:
                break
            else:
                linkss.append(str("https://www.tp86.ru"+link.get('href')))
        for i in range(5):
           
            markup = types.InlineKeyboardMarkup()
            button10 = types.InlineKeyboardButton("тык!", url=linkss[i-1])
            markup.add(button10)
            bot.send_message(message.chat.id,postTitless[i-1].format(message.from_user),reply_markup=markup)
    
    elif message.text=="Конкурсы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Конкурс «Акселератор технологических стартапов»")
        btn2 = types.KeyboardButton("Конкурс «УМНИК»")
        btn3 = types.KeyboardButton("Конкурс «Молодой изобретатель Югры»")
        back=types.KeyboardButton("Назад")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(back)
        bot.send_message(message.chat.id, 'Вы першли во вкладку "Конкурсы"', reply_markup=markup)
        time.sleep(0.5)
        bot.send_message(message.chat.id, 'Какой конкурс вам интересен?')
    elif message.text=="Конкурс «Акселератор технологических стартапов»":
        markup = types.InlineKeyboardMarkup()
        button4 = types.InlineKeyboardButton("тык!", url='https://www.tp86.ru/molodoy-izobretatel-yugry/index.php')
        markup.add(button4)
        bot.send_message(message.chat.id,"Информация о конкурсе «Акселератор технологических стартапов»".format(message.from_user),reply_markup=markup) 
    elif message.text=="Конкурс «УМНИК»":
        markup = types.InlineKeyboardMarkup()
        button5 = types.InlineKeyboardButton("тык!", url='https://www.tp86.ru/press-centr/news/39528/?ysclid=lp88jrsf2w967306183')
        markup.add(button5)
        bot.send_message(message.chat.id,"Информация о конкурсе «УМНИК»".format(message.from_user),reply_markup=markup) 
    elif message.text=="Конкурс «Молодой изобретатель Югры»":
        markup = types.InlineKeyboardMarkup()
        button6 = types.InlineKeyboardButton("тык!", url='https://www.tp86.ru/press-centr/news/39533/?ysclid=lp88eblj74476182406')
        markup.add(button6)
        bot.send_message(message.chat.id,"Информация о конкурсе «Молодой изобретатель Югры»".format(message.from_user),reply_markup=markup)
    elif message.text=="Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Мероприятия Парка")
        btn2 = types.KeyboardButton("Услуги Парка")
        btn8 = types.KeyboardButton("Конкурсы")
        btn3 = types.KeyboardButton("Как стать резидентом Технопарка Югры")
        markup.add(btn1,btn2,btn3,btn8)
        bot.send_message(message.chat.id," Вы вернулись к начальному меню".format(message.from_user),reply_markup=markup)




        
    elif message.text=="Услуги Парка":
        markup = types.InlineKeyboardMarkup()
        button2 = types.InlineKeyboardButton("тык!", url='https://www.tp86.ru/services/services/')
        markup.add(button2)
        bot.send_message(message.chat.id,"Гос.услуги Технопарка".format(message.from_user),reply_markup=markup)
        
    elif message.text=="Как стать резидентом Технопарка Югры":
        markup = types.InlineKeyboardMarkup()
        button3 = types.InlineKeyboardButton("тык!", url='https://www.tp86.ru/residents/add/')
        markup.add(button3)
        bot.send_message(message.chat.id," Как стать резидентом Технопарка Югры".format(message.from_user),reply_markup=markup)
        
          
        
    



bot.polling(non_stop=True)         




