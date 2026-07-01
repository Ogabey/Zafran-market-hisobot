from aiogram import Router, F
from aiogram.types import CallbackQuery

router=Router()

@router.callback_query(F.data == "standart_activ")
async def callback_standart(callback: CallbackQuery):
    await callback.message.answer("🚀 Standart tarifni tanladingiz. Tizim faollashtirildi!")
    await callback.answer()

@router.callback_query(F.data == "premium_activate")
async def callback_premium(callback: CallbackQuery):
    await callback.message.answer("🔥 Premium tarif tanladingiz. Barcha imkoniyatlar yoqildi!")
    await callback.answer()

@router.callback_query(F.data == "start_free")
async def callback_free(callback: CallbackQuery):
    await callback.message.answer("🎁 Hafta bepul foydalanish muddati muvaffaqiyatli ishga tushdi!")
    await callback.answer()

@router.callback_query(F.data == "yuriq_read")
async def callback_yuriq(callback: CallbackQuery):
    await callback.message.answer("🔄 Iltimos, yuqoridagi rasm va yo'riqnoma matnini qaytadan diqqat bilan o'rganib chiqing.")
    await callback.answer()

@router.callback_query(F.data == "main_menu")
async def callback_main(callback: CallbackQuery):
    await callback.message.answer("🏠 Siz asosiy sahifaga qaytdingiz.")
    await callback.answer()
