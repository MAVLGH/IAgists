import os
from openai import OpenAI
from dotenv import load_dotenv

from src.path import PATH_ENV

load_dotenv(dotenv_path=PATH_ENV)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    )