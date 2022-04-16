import connect
import os
from dotenv import load_dotenv
from discord import Embed,Colour
from connect import BotTest
def main():
    
    #BotTest.remove_command("help")
  
    load_dotenv(dotenv_path="config")

    connect.BotTest.run(os.getenv("TOKEN"))

if __name__ == "__main__":
    main()