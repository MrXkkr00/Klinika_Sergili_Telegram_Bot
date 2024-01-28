from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.bosh_menu import menu, keyboard_contact, til, keyboard_contact_ru, menu_ru
from loader import dp, bot


class NatijalarruState(StatesGroup):
    ism = State()
    contact = State()




@dp.message_handler(text="🇷🇺Русский")
async def bo232t_start(message: types.Message):
    await message.answer(f"Ассаляму алейкум, {message.from_user.full_name}!",reply_markup=menu_ru)






#
# @dp.message_handler(text="📂 Natijalarim")
# async def b23ot_start(message: types.Message):
#     await message.answer(f"To'liq Ism Familyangizni qoldiring", reply_markup=ReplyKeyboardRemove())
#     await NatijalarState.ism.set()
#
#
# @dp.message_handler(state=NatijalarState.ism)
# async def bo3t_start(message: types.Message,  state: FSMContext):
#     ism = message.text
#     await state.update_data(
#         {"ism": ism}
#     )
#     await message.answer(f"Aloqa uchun cantact yubiring",reply_markup=keyboard_contact)
#     await NatijalarState.next()

@dp.message_handler(text="📂 Мои результаты")
async def b23ot_start(message: types.Message):
    await message.answer(f"Оставьте свое полное имя и фамилию", reply_markup=ReplyKeyboardRemove())
    await NatijalarruState.ism.set()


@dp.message_handler(state=NatijalarruState.ism)
async def bo3t_23start(message: types.Message,  state: FSMContext):
    ism = message.text
    await state.update_data(
        {"ism": ism}
    )
    await message.answer(f"Перейти в контакт для связи",reply_markup=keyboard_contact_ru)
    await NatijalarruState.next()


@dp.message_handler(content_types='contact', state=NatijalarruState.contact)
async def bot23_3start(message: types.Message,  state: FSMContext):
    contakt = message.contact.phone_number
    data = await state.get_data()
    ism = data.get("ism")
    await message.answer(f"Ваши результаты будут отправлены вам в ближайшее время",reply_markup=menu_ru)
    msg = "Quyidagi ma'lumotlar qabul qilindi:\n\n"
    msg += f"👨🏻‍💼Mijoz - {ism}\n\n"
    msg += f"Username - @{message.from_user.username}\n\n"
    msg += f"📱Contact - {contakt}\n\n"
    await bot.send_message(chat_id=984568970,text=f"{msg}")
    await state.finish()


class Statecontactru(StatesGroup):
    contact = State()

@dp.message_handler(text="📲 Заказать звонок")
async def bot_s3tart1(message: types.Message):
    await message.answer(f"Отправьте нам номер своего\nрабочего телефона, чтобы мы могли вам перезвонить.\n\nВведите номер телефона вручную +998XYYYYZZZZ или вы можете отправить его с помощью кнопки\n ниже.",reply_markup=keyboard_contact_ru)
    await Statecontactru.contact.set()
@dp.message_handler(content_types='contact', state=Statecontactru.contact)
async def bot_3start2(message: types.Message,  state: FSMContext):
    contakt = message.contact.phone_number
    await message.answer(f"Ваши результаты будут отправлены вам в ближайшее время",reply_markup=menu_ru)
    msg = "📲 Qo'ng'iroq buyurtma qilish\n\n"
    msg += f"Username - @{message.from_user.username}\n\n"
    msg += f"📱Contact - {contakt}\n\n"
    await bot.send_message(chat_id=984568970,text=f"{msg}")
    await state.finish()


@dp.message_handler(text="🔬 Передвижная лаборатория")
async def bot_star3t(message: types.Message):
    await message.answer(f"☎️Для связи с нами звоните по номерам\n\n+998951449955\n+998951455005")


@dp.message_handler(text="☎️ Связаться с нами")
async def bot_start1(message: types.Message):
    await message.answer(f"☎️Для связи с нами звоните по номерам\n\n+998951449955\n+998951455005")


@dp.message_handler(text="📍 Найти нас")
async def bot_start2(message: types.Message):
    await bot.send_location(message.chat.id, 41.215308, 69.214523, reply_markup=menu_ru)
    await message.answer(f"🏥Ориентир: клиника Олам возле 4-й станции метро Сергели Ⓜ")

class TaklifStateru(StatesGroup):
    taklif = State()


@dp.message_handler(text="🖊 Предложения и жалобы")
async def bot_starre3(message: types.Message):
    await message.answer(f"Пишите свои предложения и жалобы ", reply_markup=ReplyKeyboardRemove())
    await TaklifStateru.taklif.set()


@dp.message_handler(state=TaklifStateru.taklif)
async def bot_taklierk(message: types.Message, state: FSMContext):
    msg = message.text
    await bot.send_message(984568970,f"🖊Taklif\n🙋🏻‍♂️Mijoz : @{message.from_user.username}\n{msg}",reply_markup=menu_ru)
    await state.finish()


@dp.message_handler(text="🔄 Изменить язык")
async def bot_start(message: types.Message):
    await message.answer(f"Tilni tanlang :\nВыберите язык :",reply_markup=til)
#
# @dp.message_handler(text="📲 Заказать звонок")
# async def bot_s3tart(message: types.Message):
#
#
# @dp.message_handler(text="")
# async def bot_star3t(message: types.Message):
#     await message.answer(f".")
#
#
# @dp.message_handler(text="☎️ Связаться с нами")
# async def bot_start1(message: types.Message):
#     await message.answer(f".")
#
#
# @dp.message_handler(text="📍 Найти нас")
# async def bot_start2(message: types.Message):
#     await bot.send_location(message.chat.id, 41.215308, 69.214523, reply_markup=menu)
#
# class TaklifruState(StatesGroup):
#     taklif = State()
#
#
# @dp.message_handler(text="🖊 Предложения и жалобы")
# async def bot_start3(message: types.Message):
#     await message.answer(f"Пишите свои предложения и жалобы ")
#     await TaklifruState.taklif.set()
#
#
# @dp.message_handler(state=TaklifruState.taklif)
# async def bot_taklik(message: types.Message):
#     msg = message.text
#     await bot.send_message(984568970,f"🖊Taklif\n🙋🏻‍♂️Mijoz : @{message.from_user.username}\nmsg",reply_markup=menu)
#
#
# @dp.message_handler(text="🔄 Изменить язык")
# async def bot_start(message: types.Message):
#     await message.answer(f"Tilni tanlang :\nВыберите язык :",reply_markup=til)