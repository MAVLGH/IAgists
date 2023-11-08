import os
import datetime
from openai import OpenAI
from dotenv import load_dotenv


from src.data import JSONDataManager
from src.path import PATH_DB

now =  datetime.datetime.utcnow()
load_dotenv()

db = JSONDataManager(base_path=PATH_DB)

if __name__ == '__main__':

    client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
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