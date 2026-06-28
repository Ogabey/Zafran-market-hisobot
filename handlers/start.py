from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message 
from keyboards.reply import main_menu

router=Router()

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer(
        f"Assalomu alaykum, {message.from_user.full_name}!!! \n Bizning botimizga xush kelibsiz:)",
        reply_markup=main_menu
    )

    @router.message(F.text=="Yordam")
    async def qayt_button(message: Message):
        await message.answer("Sizda qandaydir savol va takliflar bo'lsa @ogabeyqudratov ga yozing")