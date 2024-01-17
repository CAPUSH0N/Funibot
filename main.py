import telebot
from tok import key
from telebot import types
import webbrowser
bot=telebot.TeleBot(key)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я пародийный бот, нажми меню и давай повеселимся!')
@bot.message_handler(commands=['menu'])
def menu(message):
    mark=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn=types.KeyboardButton('игра с вугаром')
    btn2=types.KeyboardButton('как мы провели зимние каникулы')
    mark.add(btn, btn2)
    bot.send_message(message.chat.id, 'выберите категорию', reply_markup=mark)
@bot.message_handler(content_types='text')
def holidays_button(message):
    if message.text == 'как мы провели зимние каникулы':
        mark=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn=types.KeyboardButton('Вугар')
        btn2=types.KeyboardButton('Алмаз')
        btn3=types.KeyboardButton('Алексей')
        btn4=types.KeyboardButton('Валера')
        btn5=types.KeyboardButton('Никита')
        btn6=types.KeyboardButton('Вернуться в меню')
        mark.add(btn, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, 'кто вас интересует?', reply_markup=mark)
    elif message.text == 'Вугар':
        file=open('Много работы. Джим Керри. Брюс Всемогущий.mp4', 'br')
        bot.send_message(message.chat.id, 'держи')
        bot.send_video(message.chat.id, file)
    elif message.text == 'Алмаз':
          bot.send_message(message.chat.id, 'держи')
          webbrowser.open('https://rt.pornhub.com/video/search?search=60+plus+milf')
    elif message.text == 'Алексей':
        file2=open('Пока на расслабоне, на чиле.mp4', 'br')
        bot.send_message(message.chat.id, 'держи')
        bot.send_video(message.chat.id, file2)
    elif message.text == 'Валера':
        file3=open('а хуй его знает.mp4', 'br')
        bot.send_message(message.chat.id, 'держи')
        bot.send_video(message.chat.id, file3)
    elif message.text == 'Никита':
        file4=open('Yoru Fake.mp4', 'br')
        bot.send_message(message.chat.id, 'держи')
        bot.send_video(message.chat.id, file4)
    elif message.text == 'Вернуться в меню':
        mark=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn=types.KeyboardButton('игра с вугаром')
        btn2=types.KeyboardButton('как мы провели зимние каникулы')
        mark.add(btn, btn2)
        bot.send_message(message.chat.id, 'мы вернулись в главное меню', reply_markup=mark)
    
    if message.text=='игра с вугаром':
         mark=types.ReplyKeyboardMarkup(resize_keyboard=True)
         btn=types.KeyboardButton('камень ножницы бумага')
         mark.add(btn)
         bot.send_message(message.chat.id, 'во что сыграем?', reply_markup=mark)
    elif message.text =='камень ножницы бумага':
         mark=types.ReplyKeyboardMarkup(resize_keyboard=True)
         btn=types.KeyboardButton('камень')
         btn2=types.KeyboardButton('ножницы')
         btn3=types.KeyboardButton('бумага')
         btn4=types.KeyboardButton('Вернуться в меню')
         mark.add(btn, btn2, btn3, btn4)
         bot.send_message(message.chat.id, 'ОТЛИЧНО! давайте сыграем в камень ножницы бумага', reply_markup=mark)
    elif message.text == 'ножницы':
        bot.send_message(message.chat.id, 'камень')
        bot.send_message(message.chat.id, 'Я ВЫЙГРАЛ!')
    elif message.text == 'бумага':
        bot.send_message(message.chat.id, "ножницы")
        bot.send_message(message.chat.id, "Я ВЫЙГРАЛ!")
    elif message.text == 'камень':
        bot.send_message(message.chat.id, "бумага")
        bot.send_message(message.chat.id, "Я ВЫЙГРАЛ!")
    elif message.text == 'Вернуться в меню':
        mark=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn=types.KeyboardButton('игра с вугаром')
        btn2=types.KeyboardButton('как мы провели зимние каникулы')
        mark.add(btn, btn2)
        


    

        
    
            




   
    





     
        

            

    
																																					




bot.polling()
