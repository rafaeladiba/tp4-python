from connect import BotTest
import os
from dotenv import load_dotenv
def main():
    
    
    load_dotenv(dotenv_path="config")
    BotTest.run(os.getenv("TOKEN"))

if __name__ == "__main__":
    main()