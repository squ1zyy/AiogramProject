from aiogram import Router, F, html, Bot, Dispatcher
from aiogram.filters import Command, StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from answers import (ct_choice_answer, ct_choice_gender, ct_choice_cloth, 
                     ct_choice_brand, 
                     ct_yes, ct_no, X)
from keyboards import *
import constants

from loguru import logger

import os
import logging
import asyncio
import sys

router = Router()
dp = Dispatcher()

sneakers = [{'id': '1', 'brand': 'Off-White', 'size': 38, 'price': '2000$', 'description': 'Something', 
             'photo': 'https://cdn-images.farfetch-contents.com/off-white-out-of-office-ooo-sneakers_16863794_42669593_1000.jpg'},
            {'id': '2', 'brand': 'Nike', 'size': 38, 'price': '1500$', 'description': 'Something', 
             'photo': 'https://deltasport.ua/upload/iblock/471/CN8490_100_c.jpg'},
            {'id': '3', 'brand': 'Balenciaga', 'size': 38, 'price': '3200$', 'description': 'Something', 
             'photo': 'https://img.ssensemedia.com/images/231342M237019_1/balenciaga-black-track-led-sneakers.jpg'},]

inv = []


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

async def buy(message: Message):
    for i in range(len(inv)):
        inv.pop(i)
    print(inv)

@router.message(F.text == 'Inventory')
async def inventor(message: Message) -> None:
    if not inv:
        await message.reply(text='Inventory is empty.')
    for i in inv:
        # x = f"Brand: {i['brand']}\n{'-'*15}\nSize: {i['size']}\n{'-'*15}\nPrice: {i['price']}"
        y = f'| Brand: {i['brand']}\n| Size: {i['size']}\n| Price: {i['price']}'
        await message.reply(text=f'Inventory:\n\n{y}', reply_markup=inventory())

    print(inv)

@router.message(F.text == '✅Yes')
async def category_yes(message: Message) -> None:
    await ct_yes(message)

@router.message(F.text == '❌No')
async def category_no(message: Message, state: FSMContext) -> None:
    await ct_no(message)

@router.message(F.text == '↩️Return')
async def ct_return(message: Message) -> None:
    await message.reply('↩️Return', reply_markup=category())

@router.message(F.text == '💰Buy')
async def ct_return(message: Message) -> None:
    await buy(message)
    await message.reply('Successful✅')

async def buy(message: Message):
    for i in range(len(inv)):
        inv.pop(i)
    print(inv)

@router.message(X.x1)
async def ct_choice(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    answ = message.text.casefold()
    print(answ)
    for i in sneakers:
        if i['id'] == answ:
            inv.append(i)
    print(inv)
    await ct_yes(message)

@router.message(F.text == 'Off White')
async def off_white(message: Message, state: FSMContext) -> None:
    for i in sneakers:
        await asyncio.sleep(0.3)
        await message.answer_photo(f'{i["photo"]}')
        await message.reply(f'{i["id"]}\nBrand: {i["brand"]}\nSize: {i["size"]}\nPrice: {i["price"]}\nDescription: {i["description"]}\n')
    await state.set_state(X.x1)
    await message.answer(f'What is your choice?', reply_markup=choice())  

@router.message()
async def text_handler(message: Message, state: FSMContext) -> None:
    if message.text == '↩️Return':
        try:
            await message.answer("↩️Return")
        except Exception as e:
            logger.error(e)
    elif message.text == '🔃Cancel':
        try:
            await message.asnwer('🔃Canceled')
        except Exception as e:
            logger.error(e)

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