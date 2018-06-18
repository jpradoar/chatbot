from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('Atlas')

bot.set_tainer(ListTainer)

for _file in is.listdir('files'):
	chats = open('files/' + _file, 'r').readlines()

	bot.train(chats)

while True:
	request= input('You: ')
	response = bot.get_response(request)

	print('Atlas: ', response)
	 