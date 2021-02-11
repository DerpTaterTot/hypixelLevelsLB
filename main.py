# builtin imports
import asyncio
import json

# api imports
import requests

# dotenv
from dotenv import load_dotenv
import os

load_dotenv()

# get your own api token by typing /api new in hypixel
TOKEN = os.getenv('API_TOKEN')

player = " "
playerNames = []

while True:
    player = input("input a player you want to add to the leaderboard (type exit to finish typing): ")
    api = requests.get(f"https://api.hypixel.net/player?key={TOKEN}&name={player}").json()

    if player == "exit":
        break
    elif not api["success"]:
        print("unable to find that player")
    else:
        playerNames.append(player)

playerDict = {}

for playerName in playerNames:
    hypixelAPI = requests.get(f"https://api.hypixel.net/player?key={TOKEN}&name={playerName}").json()
    xp = hypixelAPI["player"]["networkExp"]

    playerDict[playerName] = xp

levelsDict = {}
levelsKeys = sorted(playerNames, key=playerDict.get, reverse=True)

for key in levelsKeys:
    levelsDict[key] = playerDict[key]

currentPos = 1
for player in levelsDict:
    print(f"{currentPos}. {player}: {levelsDict[player]}")
    currentPos += 1
