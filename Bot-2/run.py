from aiogram import Router, Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold

from loguru import logger

import logging
import asyncio
import sys

TOKEN = '6656625653:AAGECEK8f4S50wmAu7YRl5M9jdz7Vmz-QV4'

router = Router()

class Calc(StatesGroup):
    vow_1 = State()

@router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await message.answer("Hi! I'm calc bot. To use me: /calc")

@router.message(Command('calc'))
async def calc(message: Message, state: FSMContext) -> None:
    try:
        await message.answer('Write in the chat some equation: ')
        await state.set_state(Calc.vow_1)

    except Exception:
        logger.error('Error --> /calc')

@router.message(Calc.vow_1)
async def calc_handler(message: Message, state: FSMContext) -> None:
    equation = message.text.casefold()
    ev = eval(equation)
    await message.answer(f'{ev}')
    state.clear()

async def main() -> None:
    dp = Dispatcher()
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp.include_router(router=router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.error(f'KeyBoard Interrupt')

"""
/calc
Input:
2+2
"""
