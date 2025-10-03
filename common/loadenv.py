import os
from dotenv import load_dotenv, dotenv_values

dotenv_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '.env'))
print(dotenv_path)
def returnToken():
    if os.path.exists(dotenv_path):
        return dotenv_values(dotenv_path)['BOT_TOKEN']


