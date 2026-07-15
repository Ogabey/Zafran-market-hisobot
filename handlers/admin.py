from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import ADMIN_ID

from filters.admin_filter import IsAdmin


from keyboards.admin_kb import admin_menu, cancel_kb, back_to_admin_kb
from utils.db.queries import count_users, count_users_today, get_all_users
from utils.loggers import logger



router = Router()
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())




class Broadcast(StatesGroup):
    message = State()


@router.message(Command("admin"))
async def cmd_admin(message: Message): 
    
    await message.answer("🔧 <b>Admin panel</b>", 
                         reply_markup=admin_menu,
                         parse_mode="HTML")

@router.callback_query(F.data == "admin_back")  
async def admin_back(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer("🔧 <b>Admin panel</b>",
                                  reply_markup=admin_menu,
                                  parse_mode="HTML")
    await callback.answer() 


@router.callback_query(F.data == "admin_cancel")
async def admin_cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear() 
    await callback.message.answer("Bekor qilindi.",
                                  reply_markup=admin_menu) 
    await callback.answer()

@router.callback_query(F.data == "admin_stats")
async def show_stats(callback: CallbackQuery):
    
    total = await count_users() 
    today = await count_users_today() 

    await callback.message.answer(
        f"📊 <b>Statistika:</b>\n\n"
        f"👥 Jami foydalanuvchilar: <b>{total}</b>\n"
        f"🆕 Bugun qo'shilganlar: <b>{today}</b>\n\n"
        f"🚀 <i>Zafran Market tahlil tizimi faoliyat yuritmoqda.</i>",
        reply_markup=back_to_admin_kb,
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "admin_users")
async def show_users(callback: CallbackQuery):
   
    users = await get_all_users()

    if not users:
        await callback.message.answer("Hali hech kim ro'yxatdan o'tmagan.", reply_markup=back_to_admin_kb)
        await callback.answer()
        return

    text = "👥 <b>Foydalanuvchilar ro'yxati:</b>\n\n"
    for i, user in enumerate(users, start=1):
        text += (
            f"{i}. {user.full_name}\n"
            f"   📞 {user.phone}\n"
            f"   🆔 <code>{user.tg_id}</code>\n"
            f"   📅 {user.create_at.strftime('%d.%m.%Y')}\n\n"
        )

    await callback.message.answer(text, reply_markup=back_to_admin_kb, parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data == "admin_broadcast") 
async def start_broadcast(callback: CallbackQuery, state: FSMContext):

    await callback.message.answer("📢 Yubormoqchi bo'lgan xabaringizni yozing:",
                                  reply_markup=cancel_kb)
    await state.set_state(Broadcast.message)
    await callback.answer()

@router.message(Broadcast.message)
async def send_broadcast(message: Message, state: FSMContext):
    
    users   = await get_all_users()
    success = 0
    failed  = 0

    for user in users:
        try:
            await message.bot.send_message(user.tg_id, message.text)
            success += 1
        except Exception as e:
            failed += 1
            logger.error(f"Broadcast xatosi | id={user.tg_id} | {e}")

    await state.clear()
    await message.answer(
        f"✅ Broadcast yakunlandi!\n\n"
        f"Yuborildi: {success}\n"
        f"Xato: {failed}",
        reply_markup=admin_menu
    )
    logger.info(f"Broadcast | muvaffaqiyatli={success} | xato={failed}")