from aiogram import Router, F, html, Bot, Dispatcher
from aiogram.filters import Command, StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from keyboards import *

from loguru import logger

router = Router()
dp = Dispatcher()



def get_sneaker_details(sneakers, sneaker_id):
    for sneaker in sneakers:
        if sneaker['id'] == sneaker_id:
            return sneaker['brand'], sneaker['size'], sneaker['price'], sneaker['description'], sneaker['photo']


sneakers = [{'id': '1', 'brand': 'Off-White', 'size': 38, 'price': '2000$', 'description': 'Something', 
             'photo': 'https://cdn-images.farfetch-contents.com/off-white-out-of-office-ooo-sneakers_16863794_42669593_1000.jpg'},
            {'id': '2', 'brand': 'Nike', 'size': 38, 'price': '1500$', 'description': 'Something', 
             'photo': 'https://lishop.store/image/cache/products/9/6/6/nike-air-max-terrascape-plus-triple-black-1000x1000.jpg'},
            {'id': '3', 'brand': 'Balenciaga', 'size': 38, 'price': '3200$', 'description': 'Something', 
             'photo': 'https://img.ssensemedia.com/images/231342M237019_1/balenciaga-black-track-led-sneakers.jpg'},]

inv = []

class X(StatesGroup):
    x1 = State()
    x2 = State()

async def ct_choice_answer(message: Message) -> None:
    await message.reply(text=f'✨Cаtеgоriеs', reply_markup=category_choice())

async def ct_choice_gender(message: Message) -> None:
    await message.reply(f'🚹Man', reply_markup=man_category())

async def ct_choice_cloth(message: Message) -> None:
    await message.reply(f'👞Shoes', reply_markup=size_category())

async def ct_choice_brand(message: Message) -> None:
    await message.reply(f'🌿Brand', reply_markup=brand_choose())

async def white(message: Message, state: FSMContext) -> None:
    for i in sneakers:
        await message.answer_photo(f'{i['photo']}')
        await message.reply(f'{i['id']}\nBrand: {i['brand']}\nSize: {i['size']}\nPrice: {i['price']}\nDescription: {i['description']}\n')
    await message.answer(f'What is your choice?', reply_markup=agreement())
    # await state.set_state(X.x1)

@router.message(X.x1)
async def ct_choice(message: Message, state: FSMContext) -> None:
    answ = message.text.casefold()
    print(answ)
    for i in sneakers:
        if i['id'] == answ:
            inv.append(i)
    print(inv)


@router.message()
async def ct_yes(message: Message) -> None:
    await message.reply(text=f'Item now is in inventory', reply_markup=category_choice())


async def ct_no(message: Message) -> None:
    await message.reply(text=f'🔃Return', reply_markup=man_category())

async def buy(message: Message):
    for i in range(len(inv)):
        inv.pop(i)
    print(inv)

async def inven(message: Message) -> None:
    for i in inv:
        if inv is not None:
            x = f'Brand: {i['brand']}\n{'-'*15}\nSize: {i['size']}\n{'-'*15}\nprice: {i['price']}'
        else:
            await message.reply(text='Inventory is empty.')
        await message.reply(text=f'Inventory:\n\n{x}', reply_markup=inventory())
    print(inv)


@router.message()
async def text_handler(message: Message) -> None:
    if message.text == '↩️Return':
        try:
            await message.answer("↩️Return")
        except Exception as e:
            logger.error(e)