# Import
import discord
import json
import os 


# From
from discord.ext import commands
intents = discord.Intents.all()
from pathlib import Path

"""
CTRL SHIFT SAG SOL UST YUKARI SECEREK GITME
CTRL ALT ÇOKLU SATIRA YAZMA
ALT SATIR TAŞIMA
CTRL F2 SEÇİLEN ALANLA AYNI OLAN HER YERI SEÇMEK İÇİN
"""

# CWD
cwd = Path(__file__).parents[0]
cwd = str(cwd)

# Secret File
secret_file = json.load(open(cwd + '/database/secret_file.json'))

# Class
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned, help_command=None, intents=intents)

        
        
    # On Ready
    async def on_ready(self):
        # Log
        print('Loading...')

        # Extension Loader
        try:
            self.load_extension('commands.general')
            
            #Log
            print('Complated')
            
            # Change Presence
            await self.change_presence(activity=discord.Game(name='Mention me!'))
            
            # Log
            print('Bot\'s ready with all functions!')
            print('Developed by Rubn.')
            print('Rubn')
              
        except Exception as e:
            # Log
            print('Error! \n{}'.format(e))
		            
		            
		            
bot = Bot()
bot.run(secret_file['bot_token'])       
    
           