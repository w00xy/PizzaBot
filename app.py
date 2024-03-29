import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from common.bot_cmds_list import private
from handlers.admin_private import admin_router
from handlers.user_group import user_group_router
from handlers.user_private import user_private_router
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
bot.my_admins_list = []

dp = Dispatcher()

allowed_updates = ['message, edited_message']


dp.include_routers(user_private_router)
dp.include_routers(user_group_router)
dp.include_routers(admin_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=allowed_updates)


asyncio.run(main())
