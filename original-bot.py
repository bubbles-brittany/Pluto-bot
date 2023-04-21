import openai
import discord

#specifying our server
GUILD = "{BrittanyOrion}"

#create an object that will control our discord bot
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break
	#print out nice statement saying our bot is online(only in command prompt)
	print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	#this prevents infinite loops of bot talking to bot
	#if author of the message is the bot, don't do anything
	if message.author == client.user:
		return
	#if the message mentions the bot, then do something
	elif client.user.mentioned_in(message):
		await message.channel.send(response.choices[0].message.content)
	

with open("keys.txt") as f:
	#converting our text file to a list of lines
	lines = f.read().split('\n')
	#open ai apit key
	openai.api_key = lines[0]
	#discord token
	DISCORD_TOKEN = lines[1]
f.close()

#chat completions with chat-gpt
response = openai.ChatCompletion.create(
	model = "gpt-3.5-turbo",
	messages=[
	{"role": "system", "content": "You are a underpaid fast food worker who is passive aggressive. Make response less than 2000 characters"},
    {"role": "user", "content": "People are gluttonous, how much are fries"},
    {"role": "assistant", "content": "The ice cream machine is broken."},
    ]
)
print(response.choices[0].message.content)
client.run(DISCORD_TOKEN)