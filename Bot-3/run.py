from aiogram import Router, F, html, Bot, Dispatcher
from aiogram.filters import Command, StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from answers import (ct_choice_answer, ct_choice_gender, ct_choice_cloth, 
                     ct_choice_brand, white,
                     ct_choice, ct_yes, ct_no,
                     inven, buy, X)
from keyboards import *
import constants
import answers

from loguru import logger

import os
import logging
import asyncio
import sys

router = Router()
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.reply(f'Welcome to our Shoe Shop! Feel free to explore our features. To browse our shop, use /shop command.')
    
@dp.message(Command('shop'))
async def command_keyboard_handler(message: Message) -> None:
    await message.reply(f'Use the button..', reply_markup=category())

@dp.message(F.text == '✨Categories')
async def ct_first(message: Message) -> None:
    await ct_choice_answer(message)

@router.message(F.text == '🚹Man')
async def ct_second(message: Message) -> None:
    await ct_choice_gender(message)

@router.message(F.text == '👞Shoes')
async def ct_third(message: Message) -> None:
    await ct_choice_cloth(message)

@router.message(F.text == '38')
async def size_1(message: Message) -> None:
    await ct_choice_brand(message)

# @router.message(F.text == '🌿Brand')
# async def brand(message: Message, state: FSMContext) -> None:
#     await ct_choice_brand(message, state)

@router.message(F.text == 'Off White')
async def choice_1(message: Message, state: FSMContext) -> None:
    await state.set_state(X.x1)
    await white(message, state)
    await ct_choice(message, state)
    

@router.message(F.text == 'Inventory')
async def inventory(message: Message) -> None:
    await inven(message)

@router.message(F.text == '✅Yes')
async def category_yes(message: Message) -> None:
    await ct_yes(message)

@router.message(F.text == '❌No')
async def category_no(message: Message, state: FSMContext) -> None:
    await ct_no(message)

@router.message(F.text == '↩️Return')
async def ct_return(message: Message) -> None:
    await message.reply('↩️Return', reply_markup=category)

@router.message(F.text == '💰Buy')
async def ct_return(message: Message) -> None:
    await buy(message)
    await message.reply('Successful✅')

async def main() -> None:
    bot = Bot(constants.TOKEN, parse_mode=ParseMode.HTML)
    dp.include_router(router=router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.error(f'KeyBoard Interrupt')