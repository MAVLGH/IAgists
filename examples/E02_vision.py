import datetime

from src.api import client
from src.path import PATH_DB
from src.data import JSONDataManager

now =  datetime.datetime.utcnow()
db = JSONDataManager(base_path=PATH_DB)
messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s in this image? (respuesta en español!)"},
                {
                    "type": "image_url",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                },
            ],
        }
]

info = {
    'now':now.strftime('%Y-%m-%dT%H:%M:%S'),
    'messages': messages,
    'model': "gpt-4-vision-preview",

}

response = client.chat.completions.create(
    model=info["model"],
    messages=info["messages"],
    max_tokens=300,
)

info["response"] = response.choices[0].message.content

db.save_info(dict_info=info, now=now, suffix='vision')