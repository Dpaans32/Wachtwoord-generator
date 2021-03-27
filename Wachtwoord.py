import string
from string import punctuation
import numbers
import os
import ssl
import random
import discord
from discord import Intents
from discord import Message
import discord.ext
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import time



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

wwtxt = open("wachtwoorden.txt", "w")

# lijst met letters en tekens

al_string = string.ascii_lowercase #kleine letters
al_list = list(al_string)

au_string = string.ascii_uppercase #hoofdletters
au_list = list(au_string)

sk_string = punctuation #leestekens
sk_list = list(sk_string)

n_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]#nummers

tkn_list = al_list + au_list + sk_list + n_list #alle tekens

def getRandom(list):
    return random.choice(list)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    # beginnen
    if message.content.startswith('ww maken'):


        # naam account invoeren
        await message.channel.send('Wat is uw login?')

        if  user == message.author:
            continue
        else:
            break
    
        lin = message.content #accountnaam/emailadres     

        # wachtwoordlengte invoeren
        await message.channel.send('Uit hoeveel karakters moet het wachtwoord bestaan?')
        nk = message.content # aantal karakters
        ak = int(nk)

        if ValueError:
            await message.channel.send("Dat is geen nummer, typ 'ww maken' om opnieuw te beginnen")

        

        # wachtwoord genereren
        i=0
        ww = []
        while True:


            #Willekeurige tekens genereren en samenvoegen
        
            tkn = getRandom(tkn_list)
            ww.append(tkn)
            i+=1
        
            if i>ak:
                waw = ''
                waw = waw.join(ww)
                ww=waw
                break 




        # wachtwoord geven
        await message.channel.send(ww)


        # wachtwoord opslaan
        #lin = login en ww = wachtwoord
        #bestand aanmaken waarin alles is opgeslagen, met lin boven en ww onder en ze moeten aan elkaar gekoppeld zijn
        wwtxt.write("Login:" + lin + "\n" + "Wachtwoord:" + ww + "\n")


        # opgeslagen wachtwoorden teruggeven met account naam, bericht verwijderen na 10 sec.



        # functie om opgeslagen wachtwoorden aan te passen of te verwijderen



client.run(TOKEN)