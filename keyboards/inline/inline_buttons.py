from aiogram import types


def pay_and_question():
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Общая информация о канале и обо мне", callback_data="info")
    btn2 = types.InlineKeyboardButton(text="Вопрос", callback_data="question")
    menu.add(btn1, btn2)

    return menu