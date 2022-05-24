#Import VKBottle
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, \
                        Text, OpenLink, Location, EMPTY_KEYBOARD, \
                        template_gen, TemplateElement
from vkbottle_types import BaseStateGroup
from vkbottle import CtxStorage, PhotoMessageUploader, DocMessagesUploader, VoiceMessageUploader
from vkbottle import VKAPIError
from vkbottle import Bot, load_blueprints_from_package

#Import token
from dotenv import load_dotenv

#Load token
load_dotenv()

#Set up Token
TOKEN = os.getenv("TOKEN")

#Initializing bot
bot = Bot(TOKEN)

#Load blueprints (commands)
for command in load_blueprints_from_package("commands"):
  command.load(bot) 
  

#Run Bot
bot.run_forever()