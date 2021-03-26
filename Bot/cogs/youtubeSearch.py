import discord
from discord.ext import commands
from urllib import parse, request
import re

class YoutubeSeach(commands.Cog):
    
    def __init__(self, client):
        
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('YoutubeSearch module is online')

   
    @commands.command()
    async def youtube(self,ctx, *, search):
        '''
        Search a youtube video
        '''
        query_string = parse.urlencode({'search_query': search})
        html_content = request.urlopen("https://www.youtube.com/results?" + query_string)
        search_results = re.findall('href=\"\\/watch\\?v+(.{12})', html_content.read().decode())
        await ctx.send("https://www.youtube.com/watch?v" + search_results[1])
    
def setup(client):
    client.add_cog(YoutubeSeach(client))