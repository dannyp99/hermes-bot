import traceback
import asyncio
from aiogram import Bot, Dispatcher, executor, types

file = open('.env', 'r')

API_TOKEN = file.readline().rstrip()

# - - - - - - - - - - - - - - - -
# Initialize bot and dispathcer
bot = Bot(token=API_TOKEN)
dp  = Dispatcher(bot)
# - - - - - - - - - - - - - - - -

@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
	await message.answer("Hello I am Hermes messenger of Gods and this Group Chat\n/start\n/help    see commands\n/zoom   see the meeting time and link")


@dp.message_handler(commands=['zoom'])
async def meet(message: types.Message):
	await message.answer('https://hofstra.zoom.us/j/94395519966')

async def reminder():
	print('Reminder reminding')
	try:
		await bot.send_message(chat_id=-476860228, text='I have an important message that we are meeting today!\nPlease join here:\nhttps://hofstra.zoom.us/j/94395519966')
	except Exception:
		traceback.print_exc()

loop = asyncio.get_event_loop()
loop.create_task(reminder())

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)