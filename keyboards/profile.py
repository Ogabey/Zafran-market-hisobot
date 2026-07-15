from aiogram import Router, F
from aiogram.types import Message

from utils.db.queries import get_user
from utils.loggers import logger

router = Router()

@router.message(F.text == "👤 Profil")
async def show_profile(message: Message):
    user = await get_user(message.from_user.id)

    if not user:
        await message.answer(
            "Siz hali ro'yxatdan o'tmagansiz.\n"
            "Iltimos, avval botni qayta ishga tushiring: /start"
        )
        return

    await message.answer(
        f"👤 <b>Profilingiz ma'lumotlari:</b>\n\n"
        f"🆔 Telegram ID: <code>{user.tg_id}</code>\n"
        f"✍️ Ism: {user.full_name}\n"
        f"📞 Telefon: {user.phone}\n"
        f"📅 Ro'yxatdan o'tgan sana: {user.create_at.strftime('%d.%m.%Y')}\n\n"
        f"🚀 <i>Zafran Market tahlil botidan foydalanayotganingiz uchun rahmat!</i>",
        parse_mode="HTML"
    )
    logger.info(f"Profil ko'rildi | id={message.from_user.id}")