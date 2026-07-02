from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Standart'),
        KeyboardButton(text='Premium')],
        [KeyboardButton(text='hafta bepul foydalanish'),
         KeyboardButton(text='Yuriqnoma')],
         [KeyboardButton(text='Ortga qaytish'), KeyboardButton(text='👤Profil')]
    ],
    resize_keyboard=True

)       
contact_menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱Telifon raqam ulashish", request_contact=True)],
        [KeyboardButton(text="❌Bekor qilish")]
    ],
    resize_keyboard=True
)