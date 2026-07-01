from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message 
from keyboards.reply import main_menu
from keyboards.inline import inline_menu

router=Router()

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer(
        f"Assalomu alaykum, {message.from_user.full_name}!!! \n Bizning botimizga xush kelibsiz:)",
        reply_markup=main_menu
    )

@router.message(F.text == "Standart")
async def show_standard(message: Message):  
    await message.answer("🚀 Standart tarif:", reply_markup=inline_menu)

@router.message(F.text == "Premium")
async def show_premium(message: Message):
    await message.answer("🔥 Premium tarif:", reply_markup=inline_menu)

@router.message(F.text == "hafta bepul foydalanish")
async def show_free(message: Message):
    await message.answer("🎁 Bepul sinov:", reply_markup=inline_menu)

@router.message(F.text == "Yuriqnoma")
async def show_manual(message: Message):
    await message.answer("ℹ️ Bot qo'llanmasi:", reply_markup=inline_menu)

@router.message(F.text == "Ortga qaytish")
async def show_back(message: Message):
    await message.answer("🏠 Bosh menyu:", reply_markup=inline_menu)