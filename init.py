import telebot
import config
import fireb
from telebot import types



REF = fireb.db.reference('py/')
USERS_REF = REF.child('users')
bot = telebot.TeleBot(config.TOKEN)


OWNER_ID = "907917436"

KASPI_ACCOUNT = '0000 1212 3434 4545'

# dance time
Dances = ['Утренние классы', 'Вечерние классы']

Morning_dances = [['Q-POP ПН-СР-ПТ 11:00', 12000], ['K-POP ВТ-ЧТ-СБ 12:00', 13000]]


Evening_dances = [['Q-POP ВТ-ЧТ-СБ 16:00', 12000], ['K-POP ПН-СР-ПТ 17:00', 13000], ['HIP-HOP СР-ПТ-ВС 18:00', 15000], ['GIRL CRUSH ВТ-ЧТ-ВС  19:00', 15000],['ALL STYLES ВТ-ЧТ-СБ 20:00', 17000]]

Dances_style = [['Q-POP ПН-СР-ПТ 11:00', 12000], ['K-POP ВТ-ЧТ-СБ 12:00', 13000],['Q-POP ВТ-ЧТ-СБ 16:00', 12000], ['K-POP ПН-СР-ПТ 17:00', 13000], ['HIP-HOP СР-ПТ-ВС 18:00', 15000], ['GIRL CRUSH ВТ-ЧТ-ВС  19:00', 15000],['ALL STYLES ВТ-ЧТ-СБ 20:00', 17000]]

Choreographers = [['static_data\Maya.jpg', 'Maya-Майя'], ['static_data\Daenny.jpg', 'Daenny-Гульдана'], ['static_data\Rozanna.jpg', 'Rozanna-Аяна'], ['static_data\Tokie.jpg', 'Tokie-Толкын']]


Studio_photo = ['static_data\studio_1.jpeg', 'static_data\studio_2.jpg']

Selected_dances = []


#default_name_choreographer1 = 'Daenny-Гульдана'
#default_name_choreographer2 = 'Maya-Майя'
#default_name_choreographer3 = 'Rozanna-Аяна'
#default_name_choreographer4 = 'Tokie-Толкын'
#default_dance1 = 'Q-POP ПН-СР-ПТ 11:00'
#default_dance2 = 'K-POP ВТ-ЧТ-СБ 12:00'
#default_dance3 = 'HIP-HOP СР-ПТ-ВС 18:00'
#default_dance4 = 'Q-POP ВТ-ЧТ-СБ 16:00'
#default_dance5 = 'K-POP ПН-СР-ПТ 17:00'
#default_dance6 = 'GIRL CRUSH ВТ-ЧТ-ВС  19:00'
#default_dance7 = 'ALL STYLES ВТ-ЧТ-СБ 20:00'
#default_price1 = 12000
#default_price2 = 13000
#default_price3 = 15000
#default_price4 = 17000


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.InlineKeyboardButton("Танцы")
    item2 = types.InlineKeyboardButton("Хореографы")
    item3 = types.InlineKeyboardButton("Мои записи")
    item4 = types.InlineKeyboardButton("Оплата")
    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ бот по имени - {1.first_name}, здесь вы научитесь танцам!\nЧтобы зарегистрироваться нажмите в меню на танцы или же на хореографы!"
    .format(message.from_user, bot.get_me()), reply_markup = markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == "private":
        if message.text == "Танцы":
            markup = types.InlineKeyboardMarkup()
            for i in Dances:
                item = types.InlineKeyboardButton(i, callback_data=i)
                markup.add(item)
            bot.send_message(message.chat.id, "выберите время" ,reply_markup=markup)

        elif message.text == "Хореографы":
            markup = types.InlineKeyboardMarkup()
            for i in range(len(Choreographers)):
                item = types.InlineKeyboardButton(Choreographers[i][1], callback_data=str(i))
                markup.add(item)
            bot.send_message(message.chat.id, "Наши хореографы" ,reply_markup=markup)
        
        elif message.text == "Мои записи":
            bot.send_message(message.chat.id,Collection_user_data_record())
            #bot.send_chat_action(message.chat.id, 'upload_photo')
            #for i in Studio_photo:
               # img = open(i, 'rb')
                #bot.send_photo(message.chat.id, img)

        elif message.text == "Оплата":
            bot.send_message(message.chat.id, Collection_user_data())

def Collection_user_data_record():
    if Selected_dances == []:
        return "Вы не записались ни на один танец"
    else:
        return "Вы записались на: " + Selected_dances_names_collestion() 


def Collection_user_data():
    if Selected_dances == []:
        return "вы не записались ни на один танец"
    else:
        return "стоимость всех танцев которых вы выбрали: " + str(Calculate_price()) + "\nтанцы на которые вы записались: " + Selected_dances_names_collestion()  + '\nнаш счет Kaspi банка - ' + KASPI_ACCOUNT
    



def Calculate_price():
    price_of_all_dances = 0
    if Selected_dances != []:
        try:
            for i in Selected_dances:
                price_of_all_dances += i[1]
        except Exception as e:
            print(repr(e))

    return price_of_all_dances


def Selected_dances_names_collestion():
    selected_dances_names = ''
    if Selected_dances != []:
        try:
            for i in Selected_dances:
                selected_dances_names +='\n' + i[0]
        except Exception as e:
            print(repr(e))

    return selected_dances_names

def register(call):
    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ваша заявка записана")

    bot.send_message(call.message.chat.id, "Вы записались на танец" )


    bot.send_message(chat_id = OWNER_ID, text="зарегистрирован пользователь id - {0.message.chat.id}\nтанец - {0.data}"
            .format(call))

def Set_data_in_Firebase(id, choreographers_name):
    with open('data.txt', 'a') as file:
        file.write(f'{id}: {choreographers_name} \n')
    USERS_REF.set({
        id :{
            'choreographer' : choreographers_name,
            'dance' : Selected_dances_names_collestion(),
            'price' : str(Calculate_price())
        }
    })

def data_collection(name, price):
    Selected_dances.append([name, price])


def Send_info_about_choreographer(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Q-POP ПН-СР-ПТ 11:00",callback_data= Choreographers[int(call.data)][1])
    item2 = types.InlineKeyboardButton("K-POP ВТ-ЧТ-СБ 12:00",callback_data= Choreographers[int(call.data)][1])
    item3 = types.InlineKeyboardButton("Q-POP ВТ-ЧТ-СБ 16:00",callback_data= Choreographers[int(call.data)][1])
    item4 = types.InlineKeyboardButton("K-POP ПН-СР-ПТ 17:00",callback_data= Choreographers[int(call.data)][1])
    item5 = types.InlineKeyboardButton("HIP-HOP СР-ПТ-ВС 18:00",callback_data= Choreographers[int(call.data)][1])
    item6 = types.InlineKeyboardButton("GIRL CRUSH ВТ-ЧТ-ВС  19:00",callback_data= Choreographers[int(call.data)][1])
    item7 = types.InlineKeyboardButton("ALL STYLES ВТ-ЧТ-СБ 20:00",callback_data= Choreographers[int(call.data)][1])
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    img = open(Choreographers[int(call.data)][0], 'rb')
    bot.send_photo(call.message.chat.id, img, caption=Choreographers[int(call.data)][1] + " C легкостью находит подход к каждой из своих учениц и расскрывает потенциал девочек Если вы хотите присоединиться, делайте это прямо сейчас!Нажав на нужное вам направление танцев", reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == Dances[0]:
                markup = types.InlineKeyboardMarkup()
                for i in Morning_dances:
                    item = types.InlineKeyboardButton(i[0] +" "+ str(i[1]), callback_data=i[0])
                    markup.add(item)
                bot.send_message(call.message.chat.id, "Утренние классы\nвыберите танец" ,reply_markup=markup)

            elif call.data == Dances[1]:
                markup = types.InlineKeyboardMarkup()
                for i in Evening_dances:
                    item = types.InlineKeyboardButton(i[0] +" "+ str(i[1]), callback_data=i[0])
                    markup.add(item)
                bot.send_message(call.message.chat.id, "Вечерние классы\nвыберите танец" ,reply_markup=markup)


            for i in Morning_dances:
                if call.data == i[0]:
                    register(call)
                    data_collection(call.data, i[1])
                    Set_data_in_Firebase(call.message.chat.id, call.data) #default_name_choreographer)
                    break
            for i in Evening_dances:
                if call.data == i[0]:
                    register(call)
                    data_collection(call.data, i[1])
                    Set_data_in_Firebase(call.message.chat.id, call.data) #default_name_choreographer)
                    break

            for i in range(len(Choreographers)):
                if call.data == str(i):
                    Send_info_about_choreographer(call)
                    break

            for i in range(len(Choreographers)):
                if call.data == Choreographers[i][1]:
                    register(call)
                    data_collection()#default_dance, default_price)      
                    Set_data_in_Firebase(call.message.chat.id, call.data)         
                    break     
            
            #for i in range(len(Choreographers)):
            #   if call.data == Choreographers[i][['static_data\Maya.jpg', 'Maya-Майя']]:
            #       register(call)
            #        data_collection()#default_dance, default_price)      
            #        Set_data_in_Firebase(call.message.chat.id, call.data)         
            #        break    
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)