import requests

ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
MP3_FILE = 'path/to/episode.mp3'
TITLE = 'Episode Title from Filename'

with open(MP3_FILE, 'rb') as f:
    files = {
        'mp3': f,
    }
    data = {
        'name': TITLE,
    }
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
    }
    r = requests.post('https://api.mixcloud.com/upload/', headers=headers, files=files, data=data)
    print(r.json())
