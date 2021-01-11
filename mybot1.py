import discord
from discord.ext import commands


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):

        if message.author.id == self.user.id:
            return

        if message.content.startswith('Something'):
            await message.reply('Something ', mention_author = True)


        if message.content.startswith('Something'):
            await message.reply('Something')

        if message.content.startswith('Something'):
            await message.reply('Something')

client = MyClient()
client.run('TOKEN')