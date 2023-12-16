import requests
import time
import random


# Set your messages here
print("Sending messages on discord")
messages = ["Hello1","Hello2","Hello3","Hello4","Hello5"] # List of messages here


for i in range(1):
    for message in messages:
        payload = {"content": message}
        response = requests.post("https://discord.com/api/v9/channels/channel_id/messages", data=payload , headers={"authorization": "discord_token"})  # replace your channel_id and discord_token here
        time.sleep(5)
print("Exit")
