import telebot

class ReplyMarkup:


    menu_button = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_button.row("Redactor")
    menu_button.row("Button 2", "Button 2")

    effects_button = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    effects_button.row("Gray", "RGB", "Effect 3")
