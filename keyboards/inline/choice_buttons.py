from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_DOMBRA, URL_KOBIZ, URL_GITARA, URL_SIBIZGI, URL_PIANINO

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Dombra", callback_data=buy_callback.new(item_name="Dombra", quantity=1))

choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Kobiz", callback_data="buy:Kobiz:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Gitara", callback_data="buy:Gitara:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Sibizgi", callback_data="buy:Sibizgi")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Pianino", callback_data="buy:Pianino:5")

choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")

choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="Visit", url=URL_GITARA)

    ]

])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_KOBIZ)

    ]

])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_DOMBRA)

    ]

])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_PIANINO)

    ]



])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_SIBIZGI)

    ]

])