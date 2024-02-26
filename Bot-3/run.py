from aiogram import Router, F, html, Bot, Dispatcher
from aiogram.filters import Command, StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from loguru import logger

import logging
import asyncio
import sys

TOKEN = '6656625653:AAGECEK8f4S50wmAu7YRl5M9jdz7Vmz-QV4'

router = Router()
dp = Dispatcher()

class CategoryStates(StatesGroup):
    choosing_category = State()
    choosing_return = State()

def Category():
    builder = ReplyKeyboardBuilder()
    builder.button(text='✨Categories')
    builder.adjust(2,1)
    
    return builder.as_markup()

def Category_choice():
    builder = ReplyKeyboardBuilder()
    builder.button(text='🚹Man')
    builder.button(text='🚺Woman')
    builder.button(text='🔃Return')
    builder.adjust(2,1)
    return builder.as_markup()

def Man_category():
    builder = ReplyKeyboardBuilder()
    builder.button(text='👕Shirt')
    builder.button(text='🩳Pants')
    builder.button(text='🧥Jacket')
    builder.button(text='🔃Return')
    builder.adjust(1,4)
    return builder.as_markup()

def Woman_category():
    builder = ReplyKeyboardBuilder()
    builder.button(text='🎓Cap')
    builder.button(text='👗Skirt')
    builder.button(text='👖Pants')
    builder.button(text='🔃Return')
    builder.adjust(1,4)
    builder.row(4, 100)
    return builder.as_markup()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer_photo(photo='https://i.pinimg.com/originals/75/a1/be/75a1beb1cd6533c17aec7c665333b099.jpg')
    await message.reply(f'Welcome to our H&M Shop! Feel free to explore our features. To browse our shop, use /shop command.')
    
@router.message(Command('shop'))
async def command_keyboard_handler(message: Message, state: FSMContext) -> None:
    await message.reply(f'Use the button..', reply_markup=Category())
    await state.set_state(CategoryStates.choosing_category)

@router.message(CategoryStates.choosing_category)
async def text_handler(message: Message, state: FSMContext) -> None:
    try:
        if message.text == '✨Categories':
            await message.reply(f'✨Categories', reply_markup=Category_choice())
        elif message.text == '🚹Man':
            await message.reply(f'🚹Man', reply_markup=Man_category())
        elif message.text == '👕Shirt':
            await message.reply(f'👕Shirt')
        elif message.text == '🩳Pants':
            await message.reply(f'🩳Pants')
        elif message.text == '🧥Jacket':
            await message.reply(f'🧥Jacket')
        elif message.text == '🚺Woman':
            await message.reply(f'🚺Woman', reply_markup=Woman_category())
        elif message.text == '🎓Cap':
            await message.reply(f'🎓Cap')
        elif message.text == '👗Skirt':
            await message.reply(f'👗Skirt')
        elif message.text == '🚺👖Pants':
            await message.reply(f'🚺👖Pants')
        elif message.text == '↩️Return':
            await message.reply("↩️Return")
        
        await state.clear()
    except TypeError:
        await message.answer("Nice try!")

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp.include_router(router=router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.error(f'KeyBoard Interrupt')