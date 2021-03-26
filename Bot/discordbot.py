import discord
import os
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='.')
TOKEN = os.getenv('DISCORD_TOKEN')
#Events------------------------------------------------------------------------

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')
    
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

#Commands----------------------------------------------------------------------

@client.command()
async def shutdown(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        print(f"The bot has left {channel}")
        await voice.disconnect()
    await ctx.send("Shutting down bot...")
    quit()

@client.command()
async def load(ctx, extension):
    '''
    Loads any extension
    '''
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    '''
    Unloads any extension
    '''
    client.unload_extension(f'cogs.{extension}')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
       await ctx.send('Porfavor introduce los argumentos adecuados, maldito usuario')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Emacs, Stallman was rigth"))

#Test------------------------------------------------------------------------------------------------
# this will have the bot join the channel you are in

@client.command(pass_context=True, brief="Makes the bot join your channel", aliases=['j', 'jo'])
async def join(ctx):
        
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await voice.disconnect()
        if voice and voice.is_connected():
            await voice.move_to(channel)
            print(f"The bot has moved to {channel}")
        else:
            voice = await channel.connect()
            print(f"The bot has connected to {channel}")
            
# this will have the bot leave the current voice channel source:https://github.com/Penguin1212/Discord-Bot-BotSpud/blob/master/Bot_Spud.py
@client.command(pass_context=True, brief="Makes the bot leave your channel", aliases=['l', 'le', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        print(f"The bot has left {channel}")
        await voice.disconnect()
                    
#This loop loads all the cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

print(TOKEN)
client.run(TOKEN)