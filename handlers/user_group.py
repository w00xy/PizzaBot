from aiogram import Router, F, types, Bot
from aiogram.filters import Command

from common.restricted_words import restricted_words
from filters.chat_types import ChatTypeFilter
from common.services import clean_text

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))
user_group_router.edited_message.filter(ChatTypeFilter(['group', 'supergroup']))


@user_group_router.message(Command('admin'))
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)
    # print(admins_list)
    admins_list = [member.user.id for member in admins_list
                   if member.status == 'creator' or member.status == 'administrator']
    bot.my_admins_list = admins_list

    if message.from_user.id in admins_list:
        await message.delete()


@user_group_router.message()
@user_group_router.edited_message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.delete()
        await message.answer(f'{message.from_user.username}, соблюдайте порядок!')