#import discord
from discord.ext import commands
from discord import Embed, Colour, TextChannel,Intents
import logging
from time import strftime

    

class Bot(commands.Bot):
    def __init__(self):
       
       logging.basicConfig(filename='logging.log', filemode='w', level=logging.INFO)
       intents = Intents.default()
       intents.members = True
       super().__init__(command_prefix="!", intents=intents)
       
               
       
    async def on_member_join(self,member):
        
        general_channel:TextChannel= self.get_channel(964423566386937879)
        await general_channel.send(content=f"Bienvenue {member.display_name} sur Le Serveur de pitu !")
        print(f"L'utilisateur {member.display_name} a rejoint le serveur !")
        logging.info(f"User  {member.display_name} now connected on the server.")

    async def on_member_remove(self,member):
        general_channel = self.get_channel(964423566386937879)
        await general_channel.send(content=f"Au revoir {member.display_name}. Ce n'est qu'un au revoir.")
        print(f"L'utilisateur {member.display_name} a quitté le serveur !")
        logging.info(f"User  {member.display_name} now removed from the server.")


    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")

    

    
    
    async def on_message(self,message):
        #FORMAT = "%(asctime)s  %(message)s"
        datefmt=strftime("%a, %d %b %Y %H:%M:%S")
        #logging.basicConfig(format='%(datefmt)s %(message)s')
       
        logging.info("%s Message from %s -> %s",datefmt,message.author,message.content)

        
        """switcher = {
            0:"hey!",
            1:"bienvenue",
            2:"au revoir",
            
        }"""
        #switcher.get(0)
        #eventuellement utiliser la structure match case par la suite pour avoir un code plus propre
        
        if message.content == "Hello":
            await message.channel.send("hey !")
        if message.content == "Au revoir" or message.content == "bye":
            await message.channel.send("Bye bye ! À bientôt")
        if message.content == "Time":
            await message.channel.send(strftime("%a, %d %b %Y %H:%M:%S"))
        



        if message.content.startswith("!del"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number + 1).flatten()
            for each_message in messages:
                await each_message.delete()
        if message.content.startswith("!help"):
            await message.channel.send("Commandes : \n- Hello renvoie 'hey !'\n- Au revoir / bye renvoie 'Bye bye ! À bientôt'\n- Time renvoie la date et l'heure")

    
    




BotTest = Bot()


#load_dotenv(dotenv_path="config")

#client = discord.Client()
"""
@client.event
async def on_ready():
    print("Le bot est prêt.")

@client.event
async def on_member_join(member):
        
        general_channel:discord.TextChannel= client.get_channel(964423566386937879)
        await general_channel.send(content=f"Bienvenue{member.display_name} sur Discord Serveur!")
        general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")
        print(f"L'utilisateur {member.display_name} a rejoint le serveur !")



@client.event
async def on_message(message):
    if message.content == "Hello":
        await message.channel.send("hey!")
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()

client.run(os.getenv("TOKEN"))"""
#BotTest.run(os.getenv("TOKEN"))