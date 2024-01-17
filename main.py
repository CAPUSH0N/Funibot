import telebot
from tok import key
from telebot import types
import webbrowser
from random import choice
bot=telebot.TeleBot(key)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я пародийный бот, нажми меню и давай повеселимся!')
@bot.message_handler(commands=['menu'])
def menu(message):
    mark=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn=types.KeyboardButton('игра с вугаром')
    btn2=types.KeyboardButton('как мы провели зимние каникулы')
    btn3=types.KeyboardButton('комплимент себе')
    btn4=types.KeyboardButton('замечание самому себе')
    mark.add(btn, btn2, btn3, btn4)
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
        btn3=types.KeyboardButton('комплимент себе')
        btn4=types.KeyboardButton('замечание самому себе')
        mark.add(btn, btn2, btn3, btn4)
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
        btn3=types.KeyboardButton('комплимент себе')
        btn4=types.KeyboardButton('замечание самому себе')
        mark.add(btn, btn2, btn3, btn4)
    if message.text == 'комплимент себе':
       like_vugar=[ 'Вугар, ты очень терпеливый человек',
 'Твоя улыбка всегда разносит серость дня',
 'Вугар, у тебя невероятно сложный характер',
 'Очень остроумный человек - это про тебя, Вугар'
 'Ты всегда готов помочь другим, Вугар',
 "Ты очень умный и аналитический человек, Вугар",
 'У тебя замечательный вкус в музыке, Вугар',
 'Ты всегда находишь положительные стороны во всем, Вугар',
 'Вугар, ты всегда заводишь интересные и продуктивные разговоры',
 'Вугар, не забывай улыбаться, это делает твой день лучше',
 "Усы - это отличный аксессуар, но сбритые усы выглядят стильно, Вугар",
 'Твоя дружба всегда надежна и искренна, Вугар',
 'Ты всегда стараешься найти решение любой проблемы, Вугар',
 'Вугар, ты отлично справляешься с управлением временем',
'Время с тобой всегда пролетает незаметно, Вугар',
 'Тебя всегда можно попросить о совете, Вугар',
 'Твоя целеустремленность и настойчивость великолепны, Вугар',
 'Вугар, ты никогда не боишься брать на себя ответственность',
 'Ты всегда готов поддержать и вдохновить других, Вугар',
 'Вугар, с тобой всегда интересно проводить время',
' Ты способен вдохновить людей на большие свершения, Вугар',
 'Вугар, твоя целеустремленность вдохновляет других',
 'Ты очень ответственный и надежный, Вугар',
 'Ты проявляешь высокую самодисциплину и самоконтроль, Вугар']
       n=choice(like_vugar)
       bot.send_message(message.chat.id, n)
        
    elif message.text == 'замечание самому себе':
        unlike_vugar=[' Вугар, ты никогда не должен был сбривать усы. У тебя был стильный и запоминающийся вид!',
                       'Вугар, я заметил, что ты постоянно забываешь свои очки дома. Поставь себе напоминание на телефон, чтобы больше не забывать их.', 
                       'Вугар, почему твои шутки всегда такие нелепые?',
 'Вугар, ты всегда опаздываешь, начни быть более пунктуальным',
 'Вугар, почему ты так легко раздражаешься?',
 'Вугар, ты должен быть более ответственным и надежным',
 'Вугар, старайся быть более внимательным к деталям',
 'Вугар, тебе нужно проявлять больше терпения',
 'Вугар, старайся быть более дипломатичным в своих высказываниях',
 'Вугар, не забывай быть благодарным и выражай свою признательность',
 'Вугар, тебе нужно быть более активным в выполнении своих обязанностей',
 'Вугар, почему ты всегда таким загадочным? Показывай эмоции!',
 'Вугар, попробуй прислушиваться к чужим мнениям и не быть столь упрямым',
 'Вугар, старайся быть более организованным, это поможет тебе в повседневной жизни',
 'Вугар, не забывай про здоровый образ жизни и физическую активность',
 'Вугар, ты должен быть более сдержанным в своих эмоциях',
 'Вугар, попробуй быть более открытым к новым идеям и опыту',
 'Вугар, почему ты всегда такой критичный к окружающим?',
 'Вугар, развивай свои коммуникативные навыки - это поможет в общении с людьми',
 'Вугар, старайся быть более осторожным, чтобы избежать непредвиденных ситуаций',
 'Вугар, не забывай про самоанализ и работу над своими недостатками',
 'Вугар, старайся быть более уверенным в себе и своих возможностях',
 'Вугар, не забывай, что ты ответственен за свои поступки и слова',
 'Вугар, почему ты всегда таким закрытым? Будь более общительным']
        n=choice(unlike_vugar)
        bot.send_message(message.chat.id, n)

    

        
    
            




   
    





     
        

            

    
																																					




bot.polling()
