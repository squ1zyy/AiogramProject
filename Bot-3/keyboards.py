from aiogram.utils.keyboard import ReplyKeyboardBuilder



def category():
    builder = ReplyKeyboardBuilder()
    builder.button(text='✨Categories')
    builder.button(text='Inventory')
    builder.adjust(1,1)
    return builder.as_markup()

def category_choice():
    builder = ReplyKeyboardBuilder()
    builder.button(text='🚹Man')
    builder.button(text='↩️Return')
    builder.adjust(1,1)
    return builder.as_markup()

def man_category():
    builder = ReplyKeyboardBuilder()
    builder.button(text='👞Shoes')
    builder.button(text='↩️Return')
    builder.adjust(1,1)
    return builder.as_markup()


def size_category():
    builder = ReplyKeyboardBuilder()
    builder.button(text='38')
    builder.button(text='39')
    builder.button(text='40')
    builder.button(text='↩️Return')
    return builder.as_markup()

def brand_choose():
    builder = ReplyKeyboardBuilder()
    builder.button(text='Off White')
    builder.button(text='Nike')
    builder.button(text='Balenciaga')
    builder.button(text='↩️Return')
    return builder.as_markup()

def agreement():
    builder = ReplyKeyboardBuilder()
    builder.button(text='✅Yes')
    builder.button(text='❌No')
    builder.button(text='↩️Return')
    return builder.as_markup()

def choice():
    builder = ReplyKeyboardBuilder()
    builder.button(text='1')
    builder.button(text='2')
    builder.button(text='3')
    builder.button(text='↩️Return')
    return builder.as_markup()

def inventory():
    builder = ReplyKeyboardBuilder()
    builder.button(text='💰Buy')
    builder.button(text='🔃Cancel')
    builder.button(text='↩️Return')
    return builder.as_markup()