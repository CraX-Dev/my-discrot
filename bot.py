# Imports
import discord
from discord.ext import commands

# CredentialsCredentials
TOKEN = 'ODgzMjY0OTkxNTczMTg0NTY1.YTHaoA.mHR-ldp3pvEizA8UXZJ3JXKViiI'

# Create bot
client = commands.Bot(command_prefix='!')

# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

# Command
@client.command()
async def helloworld(ctx):
    await ctx.send('Hello World!')
print(TOKEN)
client.run(TOKEN)
