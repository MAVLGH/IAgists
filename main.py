import os
import json
import datetime
from openai import OpenAI
from dotenv import load_dotenv

def save_info(dict_info, now):

    date_path = now.strftime('%Y-%m')
    time_filename = now.strftime('%Y-%m-%dT%H:%M:%S') + '.json'

    folder_path = os.path.join('data', date_path)
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, time_filename)

    with open(file_path, 'w') as json_file:
        json.dump(dict_info, json_file, indent=4)

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

    save_info(dict_info=info, now=now)