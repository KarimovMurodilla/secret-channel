from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, mail, db
from states.ask import Ask
from keyboards.inline import inline_buttons
from utils.misc.yookassa_payment import payment


@dp.callback_query_handler(text_contains = 'pay', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    await c.answer()
    payment_details = payment.payment(10, 'Купить товар1')
    payment_url = payment_details['confirmation']['confirmation_url']
    await c.message.answer("Оплатите, затем мы примем ваш запрос на вступление на канал", reply_markup=inline_buttons.show_links(payment_url))
    
    if await payment.check_payment(payment_details['id']):
        db.update_status(c.from_user.id)


@dp.callback_query_handler(text_contains = 'question', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    await c.answer()
    await c.message.answer("Напишите вопрос, а я передам его главному. Он сам свяжется с вами")
    await Ask.step1.set()


@dp.message_handler(state=Ask.step1)
async def cancel_handler(message: types.Message, state: FSMContext):
    user_info = db.get_user(message.from_user.id)
    mail.send_mail(
        subject = "New question", 
        text_part = f"[{user_info.contact}]: {message.text}"
    )
    
    await message.answer("Отправлен ✅")
    await state.finish()