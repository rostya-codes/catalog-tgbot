from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    """/start handler"""
    await message.answer('Welcome!', reply_markup=kb.main)


@router.message(F.text == 'Catalog')
async def catalog(message: Message):
    """catalog handler"""
    await message.answer('Choose from category', reply_markup=await kb.categories())


@router.callback_query(F.text.startswith('category_'))
async def category_selected(message: Message):
    """category_id handler"""
    category_id = message.data.split('_')[1]
    await message.answer(f'You chose category: {category_id}')
