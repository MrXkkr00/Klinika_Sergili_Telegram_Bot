from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏷 Narxlar"),
            KeyboardButton(text="📂 Natijalarim")
        ],
        [
            KeyboardButton(text="📲 Qo'ng'iroq buyurtma qilish"),
            KeyboardButton(text="🔬 Ko'chib yuruvchi labaratoriya")
        ],
        [
            KeyboardButton(text="☎️ Biz bilan aloqa"),
            KeyboardButton(text="📍 Bizni topish")
        ],
        [
            KeyboardButton(text="🔄 Tilni o'zgartirish"),
            KeyboardButton(text="🖊 Taklif va shikoyatlar"),

        ],
    ],resize_keyboard=True
)

menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏷 Цены"),
            KeyboardButton(text="📂 Мои результаты")
        ],
        [
            KeyboardButton(text="📲 Заказать звонок"),
            KeyboardButton(text="🔬 Передвижная лаборатория")
        ],
        [
            KeyboardButton(text="☎️ Связаться с нами"),
            KeyboardButton(text="📍 Найти нас")
        ],
        [
            KeyboardButton(text="🔄 Изменить язык"),
            KeyboardButton(text="🖊 Предложения и жалобы"),

        ],
    ],resize_keyboard=True
)


keyboard_contact = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [
                                               KeyboardButton(text="📱Raqamingiz",
                                                              request_contact=True)
                                           ]
                                       ])

keyboard_contact_ru = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [
                                               KeyboardButton(text="📱Твой номер",
                                                              request_contact=True)
                                           ]
                                       ])

til =  ReplyKeyboardMarkup(resize_keyboard=True,
                           keyboard=[
                               [
                                   KeyboardButton(text="🇺🇿O'zbekcha"),
                                   KeyboardButton(text="🇷🇺Русский"),
                               ]
                           ])