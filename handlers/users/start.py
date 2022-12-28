from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from states.reg import Reg
from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    user = db.get_user(message.from_user.id)

    if not user:
        await message.answer("Привет! Введите своё имя")
        await Reg.step1.set()
    
    else:
        await message.answer(f"Привет {user.name}!")


@dp.message_handler(state=Reg.step1)
async def get_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.answer("Здорово! Теперь свой ник в запрещённой сети инстаграм 😉")
    await Reg.next()


@dp.message_handler(state=Reg.step2)
async def get_insta(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['insta'] = message.text

    await message.answer("Ваш номер телефона", reply_markup=keyboard_buttons.send_contact())
    await Reg.next()


@dp.message_handler(content_types='contact',state=Reg.step3)
async def get_contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        name = data['name']
        insta = data['insta']
        contact = message.contact.phone_number
        user_id = message.from_user.id
        username = message.from_user.username

    db.reg_user(user_id, username, name, insta, contact)

    await message.answer(
        "Зарегистрировал!\n"
        "Прежде чем купить подписку на канал, рекомендую ознакомиться с правилами и безопасностью :)",
            reply_markup=types.ReplyKeyboardRemove()
    )

    await message.answer(
        "Ознакомьтесь с правилами безопасности и нахождения в группе:\n"
        "1.  Я никому не пишу первый и не прошу перевести деньги на разного рода счета.\n"
        "2.  У меня нет помощников или партнеров.\n"
        "3. Я не предлагаю доверительное управление или участие в посторонних проектах.\n"
        "4. Любой график или торговая идея носит только информативный характер и является отображением моих знаний и опыта.\n"
        "5. Все Ваши прибыли и потери являются результатом Ваших принятых решений. Любая торговая идея, сценарий, сетап или фундаментальный анализ не призывает Вас открытию сделки. Поэтому ответственность за потери или прибыли полностью на Вас самих.\n"
        "6. В канале разрешено комментировать торговые идеи и видео! Будьте максимально вежливыми. Исключение из чата может быть по причине недружественного или оскорбительного поведения.\n"
        '7. Не только Вы выбираете чьими услугами пользоваться, но и я выбираю кому их оказывать. Поэтому я оставляю за собой право в любое время по любой причине выдать участнику "mute", исключить его из чата/канала без возврата средств.\n'
        "7. Оплачивая подписку, Вы соглашаетесь со всеми вышеперечисленными условиями. "
    )

    await message.answer("Не забудьте подписаться на основной канал: https://t.me/SharkSail")
    await message.answer("Теперь можно перейти к оплате или задать вопрос", reply_markup=inline_buttons.pay_and_question())

    await state.finish()