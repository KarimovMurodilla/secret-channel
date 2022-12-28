from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline import inline_buttons
from loader import dp


@dp.callback_query_handler(text_contains = 'pay', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    await c.answer()
    await c.message.answer("Оплатите, затем мы примем ваш запрос на вступление на канал", reply_markup=inline_buttons.show_links())


@dp.callback_query_handler(text_contains = 'question', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    await c.answer()
    await c.message.answer("Напишите вопрос, а я передам его главному. Он сам свяжется с вами")