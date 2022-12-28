from aiogram import types


def pay_and_question():
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Оплатить", callback_data="pay")
    btn2 = types.InlineKeyboardButton(text="Вопрос", callback_data="question")
    menu.add(btn1, btn2)

    return menu


def show_links():
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Оплатить", url="https://yookassa.ru")
    btn2 = types.InlineKeyboardButton(text="Вступить на канал", url="https://t.me/+X-aBl_FfpS5mNTcy")
    menu.add(btn1, btn2)

    return menu