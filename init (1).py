import telebot
import config
import fireb
from telebot import types
from models import Choreographer, Schedule


choreographers = [
    Choreographer(name='Daenny', image='static_data\Daenny.jpg', description='Дэни подходит каждому по особенному ', instagram='https://instagram.com/daenny___?igshid=YmMyMTA2M2Y=',
                  schedules=[
                      Schedule(name='ALL STYLES', time='ПН-СР-ПТ 19:00-20:00', place='PLUSLIMIT, Лебедева 2',
                               cost='16000'),
                      Schedule(name='K-POP femine', time='ВТ-ЧТ-СБ 17:00-18:00', place='USKO, Назарбаева 273',
                               cost='16000'),
                      Schedule(name='K-POP', time='СБ-ВС 15:30-17:00', place='USKO, Назарбаева 273',
                               cost='13000'),
                    ]),
    Choreographer(name='Maya', image='static_data\Maya.jpg', description='Майя все делает с любовью', instagram='https://instagram.com/maybemayabee?igshid=YmMyMTA2M2Y=',
                  schedules=[
                      Schedule(name='GIRLY', time='ПН-СР-ПТ 17:00-18:00', place='Skillz dance,7й мкр,13Б',
                               cost='20000'),
                      Schedule(name='GIRLY', time='ПН-СР-ПТ 18:00-19:00', place='Skillz dance,7й мкр,13Б',
                               cost='20000'),
                      Schedule(name='PRO GROUP', time='ВТ-ЧТ-СБ 18:00-19:00',place='SK boxing sport club, Каирбекова 35А',
                               cost='30000'),
                  ]),
    Choreographer(name='Rozanna', image='static_data\Rozanna.jpg', description='Розанна очень круто обьясняет', instagram='https://instagram.com/rozannaaaaaaaaa?igshid=YmMyMTA2M2Y=',
                  schedules=[
                      Schedule(name='K-POP', time='СБ-ВС 15:00-16:00', place='USKO, Назарбаева 273',
                               cost='12000'),
                      Schedule(name='Girly hip-hop', time='СБ-ВС 16:00-17:00', place='USKO, Назарбаева 273',
                               cost='12000'),
                  ]),
]

REF = fireb.db.reference('py/')
USERS_REF = REF.child('users')
# bot = telebot.TeleBot(config.TOKEN)
TOKEN = '5649971399:AAHb9wPPI-qrm40iG64Vrc4h3PVcFWRXM0A'
bot = telebot.TeleBot(TOKEN)


OWNER_ID = "907917436"

KASPI_ACCOUNT = '0000 1212 3434 4545'

# dance time
#Dances = ['Утренние классы', 'Вечерние классы']

#Morning_dances = [['Q-POP ПН-СР-ПТ 11:00', 12000],
#                 ['K-POP ВТ-ЧТ-СБ 12:00', 13000]]


#Evening_dances = [['Q-POP ВТ-ЧТ-СБ 16:00', 12000], ['K-POP ПН-СР-ПТ 17:00', 13000],
#                  ['HIP-HOP СР-ПТ-ВС 18:00', 15000], ['GIRL CRUSH ВТ-ЧТ-ВС  19:00', 15000], ['ALL STYLES ВТ-ЧТ-СБ 20:00', 17000]]

#Dances_style = [['Q-POP ПН-СР-ПТ 11:00', 12000], ['K-POP ВТ-ЧТ-СБ 12:00', 13000], ['Q-POP ВТ-ЧТ-СБ 16:00', 12000], ['K-POP ПН-СР-ПТ 17:00',
#                                                                                                                    13000], ['HIP-HOP СР-ПТ-ВС 18:00', 15000], ['GIRL CRUSH ВТ-ЧТ-ВС  19:00', 15000], ['ALL STYLES ВТ-ЧТ-СБ 20:00', 17000]]

Choreographers = [['static_data\Maya.jpg', 'Maya-Майя'], ['static_data\Daenny.jpg', 'Daenny-Гульдана'],
                  ['static_data\Rozanna.jpg', 'Rozanna-Аяна'], ['static_data\Tokie.jpg', 'Tokie-Толкын']]



Selected_dances = []


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.InlineKeyboardButton("Мастерклассы")
    item2 = types.InlineKeyboardButton("Хореографы")
    item3 = types.InlineKeyboardButton("Мои записи")
    item4 = types.InlineKeyboardButton("Оплата")
    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ бот по имени - {1.first_name}!\nВ разделе хореографы представлены наши преподаватели,с которым мы сотрудничаем!\nИх графики,направление и местоположение каждого класса и также в разделе мастерклассы, вы можете увидеть предстоящие мероприятия хореограф.\n "
                     .format(message.from_user, bot.get_me()), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == "private":
        if message.text == "Мастерклассы":
            markup = types.InlineKeyboardMarkup()
            #for i in Dances:
            #    item = types.InlineKeyboardButton(i, callback_data=i)
            #    markup.add(item)
            bot.send_message(message.chat.id, "пока нет информации насчет мастерклассов",
                             reply_markup=markup)

        elif message.text == "Хореографы":
            markup = types.InlineKeyboardMarkup()
            for i in range(len(choreographers)):
                # choreographers = [Choreographers, Choreographers, Choreographers, Choreographers]
                item = types.InlineKeyboardButton(
                    choreographers[i].name, callback_data=str(i))
                markup.add(item)
            bot.send_message(
                message.chat.id, "Наши хореографы", reply_markup=markup)

        elif message.text == "Мои записи":
            bot.send_message(message.chat.id, Collection_user_data_record())
            #bot.send_chat_action(message.chat.id, 'upload_photo')
            # for i in Studio_photo:
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
        return "стоимость всех танцев которых вы выбрали: " + str(Calculate_price()) + "\nтанцы на которые вы записались: " + Selected_dances_names_collestion() + '\nнаш счет Kaspi банка - ' + KASPI_ACCOUNT


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
                selected_dances_names += '\n' + i[0]
        except Exception as e:
            print(repr(e))

    return selected_dances_names


def register(call):
    print("asdasdasdasd")
    bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="ваша заявка записана")
    # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
    #                           text="ваша заявка записана")

    # bot.send_message(call.message.chat.id, "Вы записались на танец")

    # bot.send_message(chat_id=OWNER_ID, text="зарегистрирован пользователь id - {0.message.chat.id}\nтанец - {0.data}"
    #                  .format(call))


def Set_data_in_Firebase(id, choreographers_name):
    print('Chore', id, choreographers_name)
    with open('data.txt', 'a') as file:
        file.write(f'{id}: {choreographers_name} \n')
    file.close()
    USERS_REF.set({
        id: {
            'choreographer': choreographers_name,
            'dance': Selected_dances_names_collestion(),
            'price': str(Calculate_price())
        }
    })


def data_collection(name, price):
    Selected_dances.append([name, price])


def Send_info_about_choreographer(call):
    button_index = int(call.data)
    chosen_choreographer = choreographers[button_index]
    markup = types.InlineKeyboardMarkup(row_width=1)
    for schedule in chosen_choreographer.schedules:
        item = types.InlineKeyboardButton(
            f'{schedule.name}: {schedule.time}', callback_data=schedule.name)
        markup.add(item)
    caption = f'{chosen_choreographer.name}\n{chosen_choreographer.description}'
    # img = open(Choreographers[int(call.data)][0], 'rb')
    # bot.send_photo(call.message.chat.id,
    # img,
    #    caption=caption, reply_markup=markup)
    bot.send_message(call.message.chat.id,
                     #    img,
                     caption, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print('calback inline outside')
    try:
        print('calback inline in try')
        if call.message:
            # if call.data == Dances[0]:
            #     markup = types.InlineKeyboardMarkup()
            #     for i in Morning_dances:
            #         item = types.InlineKeyboardButton(
            #             i[0] + " " + str(i[1]), callback_data=i[0])
            #         markup.add(item)
            #     bot.send_message(
            #         call.message.chat.id, "Утренние классы\nвыберите танец", reply_markup=markup)

            # elif call.data == Dances[1]:
            #     markup = types.InlineKeyboardMarkup()
            #     for i in Evening_dances:
            #         item = types.InlineKeyboardButton(
            #             i[0] + " " + str(i[1]), callback_data=i[0])
            #         markup.add(item)
            #     bot.send_message(
            #         call.message.chat.id, "Вечерние классы\nвыберите танец", reply_markup=markup)

            # for i in Morning_dances:
            #     if call.data == i[0]:
            #         register(call)
            #         data_collection(call.data, i[1])
            #         # default_name_choreographer)
            #         Set_data_in_Firebase(call.message.chat.id, call.data)
            #         break
            # for i in Evening_dances:
            #     if call.data == i[0]:
            #         register(call)
            #         data_collection(call.data, i[1])
            #         # default_name_choreographer)
            #         Set_data_in_Firebase(call.message.chat.id, call.data)
            #         break
            for chor in choreographers:
                for sch in chor.schedules:
                    if call.data == sch.name:
                        Set_data_in_Firebase(call.message.chat.id, call.data)
                        data_collection(call.data, 12000)
                        break

            for i in range(len(Choreographers)):
                if call.data == str(i):
                    Send_info_about_choreographer(call)
                    break
            
            for i in range(len(Choreographers)):
                if call.data == Choreographers[i][1]: # TODO: WHY ERROR PRO GROUP !== Choreographers[i][1]
                    register(call.data)
                    data_collection(call.data, 1800)  # default_dance, default_price)
                    Set_data_in_Firebase(call.message.chat.id, call.data)
                    break
    except Exception as e:
        print('error')
        print(repr(e))


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print('error',e)
