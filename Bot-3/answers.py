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

async def ct_no(message: Message) -> None:
    await message.reply(text=f'🔃Return', reply_markup=man_category())

async def ct_yes(message: Message) -> None:
    await message.reply(text=f'Item now is in inventory', reply_markup=category_choice())