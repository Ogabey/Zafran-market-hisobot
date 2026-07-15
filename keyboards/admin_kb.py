from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📊 Statistika",        callback_data="admin_stats")],
        [InlineKeyboardButton(text="👥 Foydalanuvchilar", callback_data="admin_users")],
        [InlineKeyboardButton(text="📢 Broadcast (Xabar)", callback_data="admin_broadcast")],
    ]
)

cancel_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="❌ Bekor qilish", callback_data="admin_cancel")]
    ]
)

back_to_admin_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="admin_back")]
    ]
)