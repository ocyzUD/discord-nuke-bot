import discord
from discord.ext import commands
import asyncio

TOKEN = 'YOUR_TOKEN_HERE'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def spam_channels(guild, number, message):
    for i in range(number):

        channel = await guild.create_text_channel(f"NIGGER-{i+1}")
        await channel.send(message)
        print (f"Channel created: spam-channel-{i+1}, Message sent: {message}")
         
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord')

    print("Welcome to ocyz' nuke bot for discord!")

    server_id = input("Server ID: ")
    number_of_channels = int(input("Number of channels to create: "))
    message_to_send = input("Message to send to each channel: ")

    guild = bot.get_guild(int(server_id))
    if guild is None:
       print("Could not find the server with the provided ID.")
       await bot.close()
       return

    await spam_channels(guild, number_of_channels, message_to_send)
    await bot.close()

bot.run(TOKEN)
