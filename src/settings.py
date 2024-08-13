import discord
import os
from dotenv import load_dotenv

try:
    load_dotenv()
except:
    print("dotenv environment was not found. pip install python-dotenv ")
    
try:
    GUILDS_ID = discord.Object(id=int(os.getenv("GUILD")))
except:
    print("GUILDS_ID was not found. Create .env file and declare your GUILDS_ID")
    print("remember to add .env to gitignore to keep your guild id off github")