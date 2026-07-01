from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Standart'),
        KeyboardButton(text='Premium')],
        [KeyboardButton(text='hafta bepul foydalanish'),
         KeyboardButton(text='Yuriqnoma')],
         [KeyboardButton(text='Ortga qaytish')]
    ],
    resize_keyboard=True

)       