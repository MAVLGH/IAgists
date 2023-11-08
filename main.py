import os
import json
import datetime
from openai import OpenAI
from dotenv import load_dotenv


from src.data import JSONDataManager
from src.path import PATH_DATA

db = JSONDataManager(base_path=PATH_DATA)


if __name__ == '__main__':
    now =  datetime.datetime.utcnow()
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")

    client = OpenAI(
    api_key=api_key,
    )

    messages = [
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming (en español!)."}
    ]

    info = {
        'now':now.strftime('%Y-%m-%dT%H:%M:%S'),
        'messages': messages,
        'model': "gpt-4-1106-preview",

    }

    completion = client.chat.completions.create(
        model=info["model"],
        messages=info["messages"]
        )

    info["content"] = completion.choices[0].message.content

    db.save_info(dict_info=info, now=now)