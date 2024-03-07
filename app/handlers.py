from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb
from app.database.requests import get_product


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    """/start handler"""
    await message.answer('🤖 Welcome to phones catalog!', reply_markup=kb.main)


@router.message(F.text == 'Catalog')
async def catalog(message: Message):
    """Catalog handler"""
    await message.answer('📋 Choose from category', reply_markup=await kb.categories())


@router.message(F.text == 'Contacts')
async def catalog(message: Message):
    """Contacts handler"""
    await message.answer(
        '<b>Our contacts </b>👇\n\n☎️ Phone number: +380999999999\n✈️ Telegram: @anonimian\n📧'
        ' Email: rostyamudrik@proton.me\n⛽ GitHub: https://github.com/rostya-codes\n📷 https://www.instagram.com/rostya_bots/'
    )


@router.callback_query(F.data.startswith('category_'))
async def category_selected(callback: CallbackQuery):
    """category_id handler"""
    category_id = callback.data.split('_')[1]
    await callback.message.answer(f'📱 Products in selected category:', reply_markup=await kb.products(category_id))
    await callback.answer('')


@router.callback_query(F.data.startswith('product_'))
async def product_selected(callback: CallbackQuery):
    """product_id handler"""
    product_id = callback.data.split('_')[1]
    product = await get_product(product_id=product_id)
    await callback.message.answer(f'📲 Your product: <b>{product.name}</b>\n\n{product.description}\n\nPrice: ${product.price}')
    await callback.answer(f'You selected: {product.name}')
