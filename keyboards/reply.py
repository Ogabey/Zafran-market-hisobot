from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📝Kunlik hisobot'),
        KeyboardButton(text='❌yoqolgan tovarlar'),
        KeyboardButton(text='Yordam')],
    ],
    resize_keyboard=True

)