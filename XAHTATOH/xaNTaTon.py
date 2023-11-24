import aiogram
from requests import get
import json
from bs4 import BeautifulSoup
import time
from os import getenv
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.command import Command
dp = Dispatcher()
TOKEN = "6962793166:AAHBBfDTPwxDvgNdpjm1qqFvADL7XItHJYc"
bot=Bot(token=TOKEN)

last=[""]
postlast=['l']
postTitless=[]
linkss=[]
residents=[]
r = get('https://www.tp86.ru/press-centr/news/')
r1= get('https://www.tp86.ru/residents/add/')

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    btn1 = KeyboardButton(text="Новости Технопарка")
    btn2 = KeyboardButton(text="Услуги Технопарка")
    btn8 = KeyboardButton(text="Конкурсы")
    btn3 = KeyboardButton(text="Как стать резидентом Технопарка Югры")
    kb = [[btn1], [btn2], [btn3], [btn8]]
    markup=ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Приветсвую", reply_markup=markup)
    #await message.answer("-1002096049831","Приветсвую", parse_mode='plain text')
@dp.message(F.text)    
async def cmd_test1(message: types.Message):
    if message.text=="Новости Технопарка":
        soup = BeautifulSoup(r.content, "html.parser")
        postTitles = soup.find_all("p", class_="news-element_text-prew")[:5]
        links=soup.find_all("a", class_="news-element news__list_item")[:5]
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
        kb = []

        for link, title in zip(linkss,postTitles):
            builder = InlineKeyboardBuilder()
            builder.add(types.InlineKeyboardButton(text='Читать дальше...', url=link))
            await message.answer(str(title.text).strip(), reply_markup=builder.as_markup())

    elif message.text=="Как стать резидентом Технопарка Югры":
        r1= get('https://www.tp86.ru/residents/add/')
        soup = BeautifulSoup(r1.content, "html.parser")
        resident=soup.find_all("p", class_="two-column__item")
        for res in resident:
            if len(postTitless)==6:
                break
            else:
                residents.append(res.text.strip())
        message.answer("Условия,при которых можно стать резидентом Техопарка следующие:")      
        for i in range(6):
            await message.answer(residents[i-1])
            time.sleep(1)
    elif message.text=="Услуги Технопарка":
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(text='Переход на сайт', url="https://www.tp86.ru/services/services/"))
        await message.answer("Услуги,предоставляемые Технопарком",reply_markup=builder.as_markup())

    elif message.text=="Конкурсы":
        btn1 = KeyboardButton(text="Конкурс «Акселератор технологических стартапов»")
        btn2 = KeyboardButton(text="Конкурс «УМНИК»")
        btn3 = KeyboardButton(text="Конкурс «Молодой изобретатель Югры»")
        btn8 = KeyboardButton(text="Назад")
        kb = [[btn1], [btn2], [btn3], [btn8]]
        markup=ReplyKeyboardMarkup(keyboard=kb)
        await message.answer("Вы першли в меню «Конкурсы»", reply_markup=markup)   

    elif message.text=="Услуги Технопарка":
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(text='Переход на сайт', url="https://www.tp86.ru/services/services/"))
        await message.answer("Услуги,предоставляемые Технопарком",reply_markup=builder.as_markup())

    elif message.text=="Конкурсы":
        btn1 = KeyboardButton(text="Конкурс «Акселератор технологических стартапов»")
        btn2 = KeyboardButton(text="Конкурс «УМНИК»")
        btn3 = KeyboardButton(text="Конкурс «Молодой изобретатель Югры»")
        btn8 = KeyboardButton(text="Назад")
        kb = [[btn1], [btn2], [btn3], [btn8]]
        markup=ReplyKeyboardMarkup(keyboard=kb)
        await message.answer("Вы першли в меню «Конкурсы»", reply_markup=markup)  

    elif message.text=="Конкурс «Акселератор технологических стартапов»":
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(text='Переход к описанию', url="https://www.tp86.ru/molodoy-izobretatel-yugry/index.php"))
        await message.answer("О конкурсе «Акселератор технологических стартапов»",reply_markup=builder.as_markup())

    elif message.text=="Конкурс «УМНИК»":
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(text='Переход к описанию', url="https://www.tp86.ru/press-centr/news/39528/?ysclid=lp88jrsf2w967306183"))
        await message.answer("О конкурсе «УМНИК»",reply_markup=builder.as_markup())  

    elif message.text=="Конкурс «Молодой изобретатель Югры»":
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(text='Переход к описанию', url="https://www.tp86.ru/press-centr/news/39533/?ysclid=lp88eblj74476182406"))
        await message.answer("О конкурсе «Молодой изобретатель Югры»",reply_markup=builder.as_markup())

    elif message.text=="Назад":
        btn1 = KeyboardButton(text="Новости Технопарка")
        btn2 = KeyboardButton(text="Услуги Технопарка")
        btn8 = KeyboardButton(text="Конкурсы")
        btn3 = KeyboardButton(text="Как стать резидентом Технопарка Югры")
        kb = [[btn1], [btn2], [btn3], [btn8]]
        markup=ReplyKeyboardMarkup(keyboard=kb)
        await message.answer("Вы вернудись в начальное меню", reply_markup=markup)     

async def propagate():      
    soup = BeautifulSoup(r.content, "html.parser")
    last_news = {}
    
    while True:
        posstTitles = soup.find_all("p", class_="news-element_text-prew")[:5]
        linkks= soup.find_all("a", class_="news-element news__list_item")[:5]
        dict_news = {str(title.text).strip(): link.get('href') for title, link in zip(posstTitles, linkks)}           
        diff = [item for item in dict_news.items() if not item in last_news.items()]
        for title, link in diff:
            builder = InlineKeyboardBuilder()
            builder.add(types.InlineKeyboardButton(text='Читать далее...', url="https://www.tp86.ru"+link))
            await bot.send_message("-1002096049831",title, reply_markup=builder.as_markup())
            break
        await asyncio.sleep(10)  
        last_news = dict_news.copy()

async def main():
    loop = asyncio.get_event_loop()    
    task1 = asyncio.create_task(dp.start_polling(bot))
    task2 = asyncio.create_task(propagate())

    await task1
    await task2
    loop.run_forever()

if __name__ == "__main__":
    asyncio.run(main())   










