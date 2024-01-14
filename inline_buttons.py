from telebot import types, telebot

class Inline_Markup:



    effects_inline = types.InlineKeyboardMarkup(row_width=3)
    gray_inline = types.InlineKeyboardButton(text="Gray", callback_data="gray_inline")
    rgb_inline = types.InlineKeyboardButton(text="Rgb", callback_data="rgb_inline")
    focus_inline = types.InlineKeyboardButton(text="Focus", callback_data="focus_inline")
    lab_inline = types.InlineKeyboardButton(text="Lab", callback_data="lab_inline")
    blur_inline = types.InlineKeyboardButton(text="Blur", callback_data="blur_inline")
    canny_inline = types.InlineKeyboardButton(text="Canny", callback_data="canny_inline")
    gradient_inline = types.InlineKeyboardButton(text="Gradient", callback_data="gradient_inline")
    effects_inline.add(gray_inline, rgb_inline, focus_inline, lab_inline, blur_inline, canny_inline)


    back_inline = types.InlineKeyboardButton(text="Back", callback_data="back_inline")


    canny_effects_inline = types.InlineKeyboardMarkup(row_width=3)
    canny_low_effect_inline = types.InlineKeyboardButton(text="Low", callback_data="canny_low_effect_inline")
    canny_medium_effect_inline = types.InlineKeyboardButton(text="Medium", callback_data="canny_medium_effect_inline")
    canny_high_effect_inline = types.InlineKeyboardButton(text="High", callback_data="canny_high_effect_inline")
    canny_effects_inline.add(canny_low_effect_inline, canny_medium_effect_inline, canny_high_effect_inline, back_inline)