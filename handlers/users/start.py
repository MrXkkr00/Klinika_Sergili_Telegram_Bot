from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.bosh_menu import menu, keyboard_contact, til
from loader import dp, bot


class NatijalarState(StatesGroup):
    ism = State()
    contact = State()




@dp.message_handler(CommandStart())
@dp.message_handler(text="🇺🇿O'zbekcha")
async def bo232t_start(message: types.Message):
    await message.answer(f"Assalomu Alekum, {message.from_user.full_name}!",reply_markup=menu)







@dp.message_handler(text="📂 Natijalarim")
async def b23ot_start(message: types.Message):
    await message.answer(f"To'liq Ism Familyangizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await NatijalarState.ism.set()


@dp.message_handler(state=NatijalarState.ism)
async def bo3t_start(message: types.Message,  state: FSMContext):
    ism = message.text
    await state.update_data(
        {"ism": ism}
    )
    await message.answer(f"Aloqa uchun cantact yubiring",reply_markup=keyboard_contact)
    await NatijalarState.next()


@dp.message_handler(content_types='contact', state=NatijalarState.contact)
async def bot_3start(message: types.Message,  state: FSMContext):
    contakt = message.contact.phone_number
    data = await state.get_data()
    ism = data.get("ism")
    await message.answer(f"Sizning natijalaringiz sizga tez orada tashlanadi",reply_markup=menu)
    await message.answer(f"Ваши результаты будут отправлены вам в ближайшее время")
    msg = "Quyidagi ma'lumotlar qabul qilindi:\n\n"
    msg += f"👨🏻‍💼Mijoz - {ism}\n\n"
    msg += f"Username - @{message.from_user.username}\n\n"
    msg += f"📱Contact - {contakt}\n\n"
    await bot.send_message(chat_id=984568970,text=f"{msg}")
    await state.finish()


class Statecontact(StatesGroup):
    contact = State()

@dp.message_handler(text="📲 Qo'ng'iroq buyurtma qilish")
async def bot_s3tart1(message: types.Message):
    await message.answer(f"Qaayta qo'ng'iroq qilishimiz uchun o'zingizning ishlab turgan telefon \nraqamingizni yuboring.\n\nTelefon raqamni qo'lda kiriting +998XXYYYZZZZ yoki quyidagi\n tugmadan foydalanib yuborishingiz mumkin.",reply_markup=keyboard_contact)
    await Statecontact.contact.set()
@dp.message_handler(content_types='contact', state=Statecontact.contact)
async def bot_3start2(message: types.Message,  state: FSMContext):
    contakt = message.contact.phone_number
    await message.answer(f"Sizning natijalaringiz sizga tez orada tashlanadi",reply_markup=menu)
    await message.answer(f"Ваши результаты будут отправлены вам в ближайшее время")
    msg = "📲 Qo'ng'iroq buyurtma qilish\n\n"
    msg += f"Username - @{message.from_user.username}\n\n"
    msg += f"📱Contact - {contakt}\n\n"
    await bot.send_message(chat_id=984568970,text=f"{msg}")
    await state.finish()


@dp.message_handler(text="🔬 Ko'chib yuruvchi labaratoriya")
async def bot_star3t(message: types.Message):
    await message.answer(f"☎️Biz bilan bog’lanish uchun quyidagi raqamlarga murojat qiling\n\n+998951449955\n+998951455005")


@dp.message_handler(text="☎️ Biz bilan aloqa")
async def bot_start1(message: types.Message):
    await message.answer(f"☎️Biz bilan bog’lanish uchun quyidagi raqamlarga murojat qiling\n\n+998951449955\n+998951455005")


@dp.message_handler(text="📍 Bizni topish")
async def bot_start2(message: types.Message):
    await bot.send_location(message.chat.id, 41.215308, 69.214523, reply_markup=menu)
    await message.answer(f"🏥Orientir: Sergeli 4-metro bekati Ⓜ️ yonidagi Olam klinikasi")

class TaklifState(StatesGroup):
    taklif = State()


@dp.message_handler(text="🖊 Taklif va shikoyatlar")
async def bot_start3(message: types.Message):
    await message.answer(f"Taklif va shikoyatlaringizni yozib qoldiring ", reply_markup=ReplyKeyboardRemove())
    await TaklifState.taklif.set()


@dp.message_handler(state=TaklifState.taklif)
async def bot_taklik(message: types.Message, state: FSMContext):
    msg = message.text
    await bot.send_message(984568970,f"🖊Taklif\n🙋🏻‍♂️Mijoz : @{message.from_user.username}\n{msg}",reply_markup=menu)
    await state.finish()


@dp.message_handler(text="🔄 Tilni o'zgartirish")
async def bot_start(message: types.Message):
    await message.answer(f"Tilni tanlang :\nВыберите язык :",reply_markup=til)