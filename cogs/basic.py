import discord
from discord.ext import commands

class Basic(commands.Cog):
    
    def __init__(self, client):
        
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Basic module is online')

    @commands.command()
    async def ping(self, ctx):
        '''
        Shows you the latency of the bot
        '''

        await ctx.send(f'Pong! {round(self.client.latency * 1000)} ms')


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def cls(self,ctx, amount=5):
        '''
        Delete any message number, default=5
        '''
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Basic(client))