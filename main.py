import pip

pip.main(['install', 'pytelegrambotapi'])
import telebot
from telebot import types

bot = telebot.TeleBot('7061982998:AAGos3UYUuhtGFDCyEsezTuGTwtGRSAZ4cE')
@bot.message_handler()
def main(message):
    
    if message.text.lower() == '!форточка':
      okno= open('okno.gif', 'rb')
      if message.reply_to_message is not None:
         bot.send_animation(message.chat.id, okno, reply_to_message_id=message.reply_to_message.message_id)
      else: 
         bot.send_animation(message.chat.id, okno)
      okno.close()
    elif message.text.lower() == '!палка':
      plk= open('plk.gif', 'rb')
      if message.reply_to_message is not None:
         bot.send_animation(message.chat.id, plk, reply_to_message_id=message.reply_to_message.message_id)
      else: 
         bot.send_animation(message.chat.id, plk)
    elif message.text.lower() == '!пук':
      puk= open('puk.gif', 'rb')
      if message.reply_to_message is not None:
        bot.send_animation(message.chat.id, puk, reply_to_message_id=message.reply_to_message.message_id)
      else: 
        bot.send_animation(message.chat.id, puk)
      puk.close()
    elif message.text.lower() == '!омегапалка':
      omp= open('omp.gif', 'rb')
      if message.reply_to_message is not None:
        bot.send_animation(message.chat.id, omp, reply_to_message_id=message.reply_to_message.message_id)
      else: 
        bot.send_animation(message.chat.id, omp)
      omp.close()
    elif message.text.lower() == '!обнимашки':
      hugs= open('hgs.gif', 'rb')
      if message.reply_to_message is not None:
        bot.send_animation(message.chat.id, hugs, reply_to_message_id=message.reply_to_message.message_id)
      else: 
        bot.send_animation(message.chat.id, hugs)
      hugs.close()
    elif message.text.lower() == '!брид':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Тык!', url='https://t.me/gattomaniya/12'))
        bot.reply_to(message, 'Ссылка на гайд по бриду:', reply_markup=markup)

    elif message.text.lower() == '!обмен':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Тык!', url='https://clck.ru/39ouU4'))
        bot.reply_to(message, 'Таблица со всеми питомцами:', reply_markup=markup)

    elif message.text.lower() == '!команды':
        text= ''' 
    <b>Список команд:</b>
    !Палка- <i>БАМ!</i>
    !Форточка- <i>Она самая!</i>
    !Пук- <i>Пук</i>
    !Обмен- <i>Таблица для обмена питомцами</i>
    !Обнимашки- <i>Просто обнимашки</i>
    !Омегапалка- <i>Пробудить демона</i>
    !Уровень- <i>Таблица опыта для прокачки питомца</i>        
    !Бан- <i> Отправить ЖАБобу</i>
    !Брид- <i>Гайд по бриду</i>
    !Душнила- <i>Вызов главного душнилы</i>
    !Инфо-<i>О боте</i>
    !Статы- <i>Рекомендация для прокачки петов</i>
   
    '''
        bot.send_message(message.chat.id, text, parse_mode='HTML')

    elif message.text.lower() == '!инфо':
        info='''
        
<b>Данный бот является пользовательской инициативой.</b>

Ничего к официальной группе разработчиков общего не имеет. 

Список команд: !команды'''
        bot.send_message(message.chat.id, info, parse_mode='HTML')

    elif message.text.lower() == '!статы':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Тык!', url='https://t.me/gattomaniya/42'))
        bot.reply_to(message, 'Ссылка на гайд по статам:', reply_markup=markup)

    #elif message.text.lower() == '!ивенты':
       # markup = types.InlineKeyboardMarkup()
        #markup.add(types.InlineKeyboardButton('Тык!', url='https://t.me/gattomaniya/42'))
       # bot.reply_to(message, 'Ссылка на гайд по статам:', reply_markup=markup)

    elif message.text.lower() == '!душнила':
        bot.send_message(message.chat.id, '@Ragnarkkr')

    elif message.text.lower() == '!бан':
        bot.send_message(message.chat.id, 'Ваша ЖАБоба на пользователя принята!')
    elif message.text.lower() == '!уровень':
      xp= open('xp.jpeg', 'rb')
      bot.send_photo(message.chat.id, xp)
      xp.close()


bot.polling(none_stop=True)