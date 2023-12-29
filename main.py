import os
import requests
from src.utils import Log
import json
import threading
import asyncio

with open('config.json') as config_file:
    config = json.load(config_file)

os.system('color')

files = {
    "tokens.txt"
}
for file in files:
    if not os.path.exists(file):
        open(file, "w").close()

tokens = []

invite_code = input('Invite Code: ')

with open("tokens.txt", "r") as f:
    for line in f:
        if ":" in line:
            line = line.split(":")[2]
        tokens.append(line.strip())

Log.info("Loaded " + str(len(tokens)) + " tokens from tokens.txt")


async def changeAccountInfo(token):
    profile_config = config['profile_change'];
    payload = {
        "apiKey": config['apiKey'],
        "token": token,
        "form": {}
    }
    headers = {
        'Content-Type': 'application/json'
    }
    
    if (profile_config['globalname_enable']):
        payload["form"]["globalname"] = profile_config['globalname']
    if (profile_config['bio_enable']):
        payload["form"]["bio"] = profile_config['bio']

    try:
        req = requests.post(
            "https://api.z-deliver.uk/discord/edit",
            headers=headers,
            json=payload
        )
        return req.json()['errorId']
    except:
        return 0

def getStatus(token):
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        req = requests.post(
            "https://api.z-deliver.uk/discord/invitetoken",
            headers=headers,
            json={
                "apiKey": config['apiKey'],
                "token": token,
                "inviteCode": invite_code
            }
        )
        return req.json()
    except:
        return 0
    
def join(token):
    asyncio.run(changeAccountInfo(token))
    status = getStatus(token)
    errorId = status['errorId']
    if errorId == 0:
        Log.info("Joined: " + token)
    else:
        Log.error(f"Error: " + token + f" {status['message']}")


for token in tokens:
    Log.info("Joining Token: " + token + "...")
    threading.Thread(target=join, args=(token,)).start()