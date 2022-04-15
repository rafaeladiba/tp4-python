#import discord
from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")
    
    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")

    async def on_message(self,message):
        if message.content == "Hello":
            await message.channel.send("hey!")
        if message.content.startswith("!del"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number + 1).flatten()
            for each_message in messages:
                await each_message.delete()




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