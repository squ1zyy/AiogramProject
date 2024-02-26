from aiogram import Router, F, html, Bot, Dispatcher
from aiogram.filters import Command, StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold

from loguru import logger

import logging
import asyncio
import sys


TOKEN = '6656625653:AAGECEK8f4S50wmAu7YRl5M9jdz7Vmz-QV4'

router = Router()

class Quiz(StatesGroup):
    asnw_1 = State()
    asnw_2 = State()
    asnw_3 = State()

@router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await message.answer("Hi! I'm quiz bot. To use me: /quiz")

@router.message(Command('quiz'))
async def quiz(message: Message, state: FSMContext) -> None:
    try:
        await message.answer('What is the national US animal?')
        await state.set_state(Quiz.asnw_1)

        await message.answer('')
    except Exception:
        logger.error('Error --> /quiz')

@router.message(Quiz.asnw_1)
async def process_answer_1(message: Message, state: FSMContext) -> None:
    if message.text.casefold() == 'eagle':
        await message.answer_photo(photo='https://www.treehugger.com/thmb/hABHkJldvMOC7FMjwJS493YoSZs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/cooper-s-hawk-profile-583855629-d89e191a88d1484db08800f067ba98e8.jpg')
        await message.reply("Correct! 🦅 Eagle is the national US animal.")
        await asyncio.sleep(1.5)
        await message.answer('Next question: What is the capital of France?')
        await state.clear()
        await state.set_state(Quiz.asnw_2)
    else:
        await message.reply("Incorrect. The correct answer is Eagle.")
        await state.clear()

@router.message(Quiz.asnw_2)
async def process_answer_2(message: Message, state: FSMContext) -> None:
    if message.text.casefold() == 'paris':
        await message.answer_photo(photo='https://res.klook.com/image/upload/Mobile/City/swox6wjsl5ndvkv5jvum.jpg')
        await message.reply("Correct! 🗼 Paris is the capital of France.")
        await asyncio.sleep(1.5)
        await message.answer('Next question: Who painted the Mona Lisa?')
        await state.clear()
        await state.set_state(Quiz.asnw_3)
    else:
        await message.reply("Incorrect. The correct answer is Paris.")
        await state.clear()

@router.message(Quiz.asnw_3)
async def process_answer_3(message: Message, state: FSMContext) -> None:
    if message.text.casefold() == 'leonardo da vinci':
        await message.answer_photo(photo='https://www.libr.dp.ua/uploads/posts/2021-02/1612943636_vinci.jpg')
        await message.reply("Correct! 🎨 Leonardo da Vinci painted the Mona Lisa.")
        await state.clear()
    else:
        await message.reply("Incorrect. The correct answer is Leonardo da Vinci.")
        await state.clear()
        
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