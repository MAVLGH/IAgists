import datetime

from src.api import client
from src.data import JSONDataManager
from src.path import PATH_DB

now =  datetime.datetime.utcnow()
db = JSONDataManager(base_path=PATH_DB)

if __name__ == '__main__':


    messages = [
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming (en español!)."}
    ]

    info = {
        'now':now.strftime('%Y-%m-%dT%H:%M:%S'),
        'messages': messages,
        'model': "gpt-4-1106-preview",

    }

    response = client.chat.completions.create(
        model=info["model"],
        messages=info["messages"]
        )

    info["response"] = response.choices[0].message.content

    db.save_info(dict_info=info, now=now)