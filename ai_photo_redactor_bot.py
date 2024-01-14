import telebot
import cv2
import sqlite3
from time import sleep
import datetime

import config

from buttons import ReplyMarkup
from inline_buttons import Inline_Markup

bot = telebot.TeleBot(config.TOKEN)

db = sqlite3.connect("ai_photo_redactor_bot.db", check_same_thread=False)
sql = db.cursor()

DateTime = datetime.datetime.now()

sql.execute('''CREATE TABLE IF NOT EXISTS user_data (ID INTEGER, USERNAME TEXT, FIRST_NAME TEXT, LAST_NAME TEXT, DATE_TIME TIMESWAP)''')
db.commit()




@bot.message_handler(commands=['start'])
def start (message):

    sql.execute(f'''SELECT ID FROM user_data WHERE ID = {message.chat.id}''')
    user_id = sql.fetchone()

    if user_id == None:

        sql.execute('''INSERT INTO user_data (ID, USERNAME, FIRST_NAME, LAST_NAME, DATE_TIME) VALUES (?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), DateTime))
        db.commit()

        bot.send_message(message.chat.id, f'<b> {message.from_user.full_name}'
                                          f'\n\nWelcome  👋 </b>', parse_mode='html')
        bot.send_message(message.chat.id, "<b> Send me a photo and I'll redact it for you ! </b>", parse_mode="html")

    else:

        bot.send_message(message.chat.id, "<b> Send me a photo and I'll redact it for you ! </b>", parse_mode="html")


@bot.message_handler(content_types=['text'])
def text(message):

    if message.text == "Redactor":
        redactor = bot.send_message(message.chat.id, "Ok, send me a photo:")
        bot.register_next_step_handler(redactor, select_effect)






@bot.message_handler(content_types=['photo'])
def select_effect(message):

    file_info = bot.get_file(message.photo[-1].file_id)
    file = bot.download_file(file_info.file_path)

    with open(f"photo/Original/{message.chat.id}.jpg", "wb") as new_file:
        new_file.write(file)
        new_file.close()
        with open(f"photo/Original/{message.chat.id}.jpg", "rb") as photo:
            bot.send_message(message.chat.id, "<b> Choose the effect: </b>", parse_mode="html",)
            bot.send_photo(message.chat.id, photo,  reply_markup=Inline_Markup.effects_inline)


def gray_effect(message):

    file_info = bot.get_file(message.photo[-1].file_id)
    file = bot.download_file(file_info.file_path)

    with open(f"photo/Gray/{message.chat.id}.jpg", "wb") as new_file:
        new_file.write(file)

        img = cv2.imread(f"photo/Gray/{message.chat.id}.jpg")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f"photo/Gray/{message.chat.id}.jpg", img)
        with open(f"photo/Gray/{message.chat.id}.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo, reply_markup=Inline_Markup.effects_inline)

def rgb_effect(message):

    file_info = bot.get_file(message.photo[-1].file_id)
    file = bot.download_file(file_info.file_path)

    with open(f"photo/Rgb/{message.chat.id}.jpg", "wb") as new_file:
        new_file.write(file)

        img = cv2.imread(f"photo/Rgb/{message.chat.id}.jpg")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imwrite(f"photo/Rgb/{message.chat.id}.jpg", img)
        bot.send_photo(message.chat.id, open(f"photo/Rgb/{message.chat.id}.jpg", "rb"), reply_markup=Inline_Markup.effects_inline)


def focus_effect(message):

    file_info = bot.get_file(message.photo[-1].file_id)
    file = bot.download_file(file_info.file_path)

    with open(f"photo/Focus/{message.chat.id}.jpg", "wb") as new_file:
        new_file.write(file)

        img = cv2.imread(f"photo/Focus/{message.chat.id}.jpg")
        img= cv2.fastNlMeansDenoisingColored(img, None, 10, 20, 20, 20)
        cv2.imwrite(f"photo/Focus/{message.chat.id}.jpg", img)
        bot.send_photo(message.chat.id, open(f"photo/Focus/{message.chat.id}.jpg", "rb"), reply_markup=Inline_Markup.effects_inline)


def lab_effect(message):

    file_info = bot.get_file(message.photo[-1].file_id)
    file = bot.download_file(file_info.file_path)

    with open(f"photo/Lab/{message.chat.id}.jpg", "wb") as new_file:
        new_file.write(file)

        img = cv2.imread(f"photo/Lab/{message.chat.id}.jpg")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        cv2.imwrite(f"photo/Lab/{message.chat.id}.jpg", img)
        bot.send_photo(message.chat.id, open(f"photo/Lab/{message.chat.id}.jpg", "rb"), reply_markup=Inline_Markup.effects_inline)


def blur_effect(message):

    file_info = bot.get_file(message.photo[-1].file_id)
    file = bot.download_file(file_info.file_path)

    with open(f"photo/Blur/{message.chat.id}.jpg", "wb") as new_file:
        new_file.write(file)

        img = cv2.imread(f"photo/Blur/{message.chat.id}.jpg")
        img = cv2.GaussianBlur(img, (7, 7), 0)
        cv2.imwrite(f"photo/Blur/{message.chat.id}.jpg", img)
        bot.send_photo(message.chat.id, open(f"photo/Blur/{message.chat.id}.jpg", "rb"), reply_markup=Inline_Markup.effects_inline)



#  CANNY EFFECT  #

def canny_low_effect(message):

    file_info = bot.get_file(message.photo[-1].file_id)
    file = bot.download_file(file_info.file_path)

    with open(f"photo/Canny/{message.chat.id}.jpg", "wb") as new_file:
        new_file.write(file)

        img = cv2.imread(f"photo/Canny/{message.chat.id}.jpg")
        img = cv2.Canny(img, 10, 20)
        cv2.imwrite(f"photo/Canny/{message.chat.id}.jpg", img)
        bot.send_photo(message.chat.id, open(f"photo/Canny/{message.chat.id}.jpg", "rb"), reply_markup=Inline_Markup.effects_inline)

def canny_medium_effect(message):

    file_info = bot.get_file(message.photo[-1].file_id)
    file = bot.download_file(file_info.file_path)

    with open(f"photo/Canny/{message.chat.id}.jpg", "wb") as new_file:
        new_file.write(file)

        img = cv2.imread(f"photo/Canny/{message.chat.id}.jpg")
        img = cv2.Canny(img, 50, 100)
        cv2.imwrite(f"photo/Canny/{message.chat.id}.jpg", img)
        bot.send_photo(message.chat.id, open(f"photo/Canny/{message.chat.id}.jpg", "rb"), reply_markup=Inline_Markup.effects_inline)

def canny_high_effect(message):

    file_info = bot.get_file(message.photo[-1].file_id)
    file = bot.download_file(file_info.file_path)

    with open(f"photo/Canny/{message.chat.id}.jpg", "wb") as new_file:
        new_file.write(file)

        img = cv2.imread(f"photo/Canny/{message.chat.id}.jpg")
        img = cv2.Canny(img, 100, 200)
        cv2.imwrite(f"photo/Canny/{message.chat.id}.jpg", img)
        bot.send_photo(message.chat.id, open(f"photo/Canny/{message.chat.id}.jpg", "rb"), reply_markup=Inline_Markup.effects_inline)





#  GRADIENT EFFECT  #

def gradient_effect(message):

    file_info = bot.get_file(message.photo[-1].file_id)
    file = bot.download_file(file_info.file_path)

    with open(f"photo/Canny/{message.chat.id}.jpg", "wb") as new_file:
        new_file.write(file)

        img = cv2.imread(f"photo/Canny/{message.chat.id}.jpg")
        img = cv2.MORPH_GRADIENT
        cv2.imwrite(f"photo/Canny/{message.chat.id}.jpg", img)
        bot.send_photo(message.chat.id, open(f"photo/Canny/{message.chat.id}.jpg", "rb"), reply_markup=Inline_Markup.effects_inline)




@bot.callback_query_handler(func=lambda call: True)
def inline(call):


    if call.data == "back_inline":
        with open(f"photo/Original/{call.message.chat.id}.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, '<b> Choose the effect: </b>', parse_mode="html", reply_markup=Inline_Markup.effects_inline)




    if call.data == "gray_inline":
        gray_effect(call.message)

    if call.data == "rgb_inline":
        rgb_effect(call.message)

    if call.data == "focus_inline":
        focus_effect(call.message)

    if call.data == "lab_inline":
        lab_effect(call.message)

    if call.data == "blur_inline":
        blur_effect(call.message)




    #  CANNY EFFECT  #

    if call.data == "canny_inline":
        with open(f"photo/Original/{call.message.chat.id}.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, '<b> Select the quantity of "Canny Effect": </b>', parse_mode="html", reply_markup=Inline_Markup.canny_effects_inline)

    if call.data == "canny_low_effect_inline":
        canny_low_effect(call.message)

    if call.data == "canny_medium_effect_inline":
        canny_medium_effect(call.message)

    if call.data == "canny_high_effect_inline":
        canny_high_effect(call.message)




    #  GRADIENT EFFECT  #

    if call.data == "gradient_inline":
        gradient_effect(call.message)













if __name__=='__main__':

    while True:

        try:

            bot.polling(non_stop=True, interval=0)

        except Exception as e:

            print(e)
            sleep(5)
            continue