from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.reply import main_menu, contact_menu
from utils.db.queries import add_user, get_user
from utils.loggers import logger


router=Router()

class Register(StatesGroup):
    name=State()
    phone=State()

@router.message(F.text=="👤Profil")
async def start_register(message:Message, state:FSMContext):
    user= await get_user(message.from_user.id)

    if user:
        await message.answer(
            f"👤<b>Profilingiz:</b>\n\n" 
            f"Ism: {user.full_name}\n" 
            f"Telefon: {user.phone}\n"
            f"Ro'yxatdan o'tgan: {user.created_at}",
            parse_mode="HTML" 
        )
    else:
        await message.answer("Ismingizni kiriting")
        await state.set_state(Register.name)

@router.message(Register.name)
async def get_name(message:Message, state:FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
        "Telefon raqamingizni ulashmoqchimsiz?👇",
    reply_markup=contact_menu
    )
    await state.set_state(Register.phone)

@router.message(Register.phone, F.contact)
async def get_phone(message:Message , state:FSMContext):
    data=await state.get_data()
    name=data["name"]
    phone=message.contact.phone_number
    
    await add_user(
         
         tg_id=message.from_user.id,
         full_name=name,
         phone=phone
    )
    logger.info(f"Ro'yxatdan o'tish muvaffaqiyatli yakunlandi| id={message.from_user.id}")
    
    await message.answer(

        f"✅Sizning ma'lumotlaringiz saqlandi\n"
        f"Ismingiz:{name}\n"
        f"Telefon:{phone}",
        reply_markup=main_menu
    )

    await state.clear()

@router.message(Register.phone, F.text=="❌Bekor qilish")
async def cancel_register(message:Message, state:FSMContext):
        logger.info(f"Ro'yxatdan o'tish bekor qilindi| id={message.from_user.id}")
        await state.clear()
        await message.answer("Bekor qilindi.", reply_markup=main_menu)