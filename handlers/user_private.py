from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_list, Bold
import reply_kbs.keyboards
from reply_kbs.keyboards import get_kb
from filters.chat_types import ChatTypeFilter
from emoji import emojize as _
user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(_('<B>Это бот пиццерии W :pizza:</b>'),
                         reply_markup=get_kb(
                             'Меню',
                             'О магазине',
                             'Варианты оплаты',
                             'Способы доставки',
                             placeholder='Что вы хотите сделать?',
                             sizes=(2,2 )
                            )
                        )

# @user_private_router.message(F.text.lower() == 'меню')
@user_private_router.message(or_f(Command('menu'), (F.text.lower().contains('меню'))))
async def menu_cmd(message: types.Message):
    await message.answer('Меню бота: ')


@user_private_router.message(F.text.lower().contains('о магазине'))
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer('О нас: ')


@user_private_router.message(F.text.lower().contains('варианты оплаты'))
@user_private_router.message(Command('prices'))
async def prices_cmd(message: types.Message):
    await message.answer('Расценки: ')


@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'способы доставки'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    # text = as_list(
    #     as_marked_list(
    #         Bold('Варианты доставки/заказа'),
    #         'Курьер',
    #         'Самовывоз',
    #         'Приеду покушать к вам',
    #         marker='📍'
    #     ),
    #     as_marked_list(
    #         Bold('Нельзя'),
    #         'Почта',
    #         'Голуби',
    #         marker='🚫'
    #     ),
    #     sep='\n------------------------------------------------\n'
    # )


    text = ('<b>Варианты доставки/заказа</b>\n'
            '📍 Курьер\n'
            '📍 Самовывоз\n'
            '📍 Приеду покушать к вам\n'
            '------------------------------------------------\n'
            '<b>Нельзя:</b>\n'
            '🚫 Почта\n'
            '🚫 Голуби\n')

    await message.answer(text)


@user_private_router.message(F.text == 'penis')
async def shipping_cmd(message: types.Message):
    await message.answer('tebe pizdy')
