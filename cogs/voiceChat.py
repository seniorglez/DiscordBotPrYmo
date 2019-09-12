import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.utils import get
import youtube_dl
import os

class VoiceChat(commands.Cog):
    
    def __init__(self, client):
        
        self.client = client
        self.isplaying = False #i'm pretty sure that this is not the best way to solve the queue problem, but it can work for now

    @commands.Cog.listener()
    async def on_ready(self):
        print('VoiceChat module is online')
       
    
    
    @commands.command(pass_context=True, aliases=['p', 'pla'])
    async def yt(self,ctx, url):
        
        if not self.isplaying:
            self.isplaying= True
            #song_there = os.path.isfile("song.mp3")
            try:
                #if song_there:
                    #os.remove("song.mp3")
                    for file in os.listdir("./"):
                        if file.endswith(".mp3"):
                            os.remove(file)
                    print("Removed old song file")
            except PermissionError:
                print("Trying to delete song file, but it's being played")
                await ctx.send("ERROR: Music playing")
                return

            await ctx.send("Getting everything ready now")

            voice = get(self.client.voice_clients, guild=ctx.guild)

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("Downloading audio now\n")
                ydl.download([url])

                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        name = file
                        print(f"Renamed File: {file}\n")
                        os.rename(file, "song.mp3")
                
                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e:  print("Song done!"))
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 1

                nname = name.rsplit("-", 2)
                await ctx.send(f"Playing: {nname[0]}")
                print("playing\n")
                self.isplaying = False
               
        else:
            await ctx.send("El bot esta reproduciendo musica")

        



    @commands.command()
    async def summon(self,ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
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

    @commands.command()
    async def fix(self,ctx):
        for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.remove(file)
        self.isplaying=False
    @commands.command()
    async def isply(self, ctx):
        await ctx.send(f"La variable isplaying es {self.isplaying}")
def setup(client):
    client.add_cog(VoiceChat(client))