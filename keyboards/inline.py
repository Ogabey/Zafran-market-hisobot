from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Standartni faollashtirish", callback_data="standart_activ")],
        
        [InlineKeyboardButton(text="🔥 Premiumga o'tish", callback_data="premium_activate")],
       
        [InlineKeyboardButton(text="🎁 Bepul sinovni boshlash", callback_data="start_free")],
     
        [InlineKeyboardButton(text="🔄 Yo'riqnomani qayta o'qish", callback_data="yuriq_read")],
        
        [InlineKeyboardButton(text="🏠 Bosh menyuga o'tish", callback_data="main_menu")]
    ]
)
