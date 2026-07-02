from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.reply import main_menu, contact_menu


router=Router()

class Register(StatesGroup):
    name=State()
    phone=State()

@router.message(F.text=="👤Profil")
async def start_register(message:Message, state:FSMContext):
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
    name=data("name")
    phone=message.contact.phone_number

    await message.answer(

        f"Sizning ma'lumotlaringiz\n"
        f"Ismingiz:{name}\n"
        f"Telefon:{phone}",
        reply_markup=main_menu
    )

    await state.clear()

    @router.message(Register.phone, F.text=="Bekor qilish")
    async def cencel_register(message:Message, state:FSMContext):
        await state.clear()
        await message.answer("Bekor qilindi.", reply_markup=main_menu)