import discord
import random
guh = ["images/guh1.jpg",
       "images/guh2.jpg",
       "images/guh3.jpg",
       "images/guh4.jpg",
       "images/guh5.jpg",]

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content.lower() == 'guh':
            print('guh')
            await message.channel.send(file=discord.File(random.choice(guh)))


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('DISCORD_TOKEN')
