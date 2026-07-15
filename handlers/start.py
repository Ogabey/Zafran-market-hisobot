from aiogram import Router, F 
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext # FSM ni boshqarish uchun qo'shdik


from filters.registered_filter import IsRegistered


from keyboards.reply import main_menu 
from keyboards.inline import inline_menu 
from utils.db.queries import get_user 
from utils.loggers import logger

router = Router()




@router.message(CommandStart())
async def cmd_start(message: Message):
    user = await get_user(message.from_user.id)
    
    if user:
        await message.answer(
            f"Assalomu alaykum, {user.full_name}!!! \nBizning botimizga xush kelibsiz :)",
            reply_markup=main_menu
        )
        logger.info(f"Qaytgan user | id={message.from_user.id}") 
    else:
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!!! \nBizning botimizga xush kelibsiz :)",
            reply_markup=main_menu
        )
        logger.info(f"Yangi user | id={message.from_user.id}")

@router.message(F.text.contains("Profil"), IsRegistered()) 
async def show_profile(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    
    await message.answer(
            f"👤 <b>Sizning profilingiz:</b>\n\n"
            f"📝 Ism-sharif: <b>{user.full_name}</b>\n"
            f"📞 Telefon: <b>{user.phone}</b>\n"
            f"🆔 Telegram ID: <code>{user.tg_id}</code>\n"
            f"📅 Ro'yxatdan o'tgan sana: <b>{user.create_at.strftime('%d.%m.%Y')}</b>",
            parse_mode="HTML"
        )
   
    
@router.message(F.text == "Standart",IsRegistered())
async def show_standard(message: Message):  
    await message.answer("🚀 Standart tarif:", reply_markup=inline_menu)

@router.message(F.text == "Premium", IsRegistered())
async def show_premium(message: Message):
    await message.answer("🔥 Premium tarif:", reply_markup=inline_menu)

@router.message(F.text == "hafta bepul foydalanish",IsRegistered())
async def show_free(message: Message):
    await message.answer("🎁 Bepul sinov:", reply_markup=inline_menu)

@router.message(F.text == "Yuriqnoma", IsRegistered())
async def show_manual(message: Message):
    await message.answer("ℹ️ Bot qo'llanmasi:", reply_markup=inline_menu)

@router.message(F.text == "Ortga qaytish",IsRegistered())
async def show_back(message: Message):
    await message.answer("🏠 Bosh menyu:", reply_markup=inline_menu)

@router.message(F.text.contains("Profil"))
async def show_profile_blocked(message: Message):
    await message.answer("⚠️ Siz hali ro'yxatdan o'tmagansiz! Iltimos, ismingizni kiriting:")

@router.message(F.text.in_({"Standart", "Premium", "hafta bepul foydalanish", "Yuriqnoma"}))
async def show_menu_blocked(message: Message):
    await message.answer("⚠️ Bot xizmatlaridan foydalanish uchun, iltimos, oldin ro'yxatdan o'ting!")