# builtin imports
import asyncio
import json

# api imports
import requests

# dotenv
from dotenv import load_dotenv, main
import os

# local imports
from calculations import calculations

load_dotenv()
class Leaderboard():
    def __init__(self) -> None:
        # get your own api token by typing /api new in hypixel
        self.TOKEN = os.getenv('API_TOKEN')
        
        self.playerDict = {}
        pass
    
    def listPlayers(self):
        player = " "
        playerNames = []        
        while True:
            player = input("input a player you want to add to the leaderboard (type exit to finish typing): ")
            api = requests.get(f"https://api.hypixel.net/player?key={self.TOKEN}&name={player}").json()

            if player == "exit":
                break
            elif not api["player"]:
                print("unable to find that player")
            else:
                playerNames.append(player)
        return playerNames
    
    def run(self) -> None:
        lb = input("what do you want a leaderboard for? current options are Hypixel Levels (L), Bedwars Stars (BWSTAR), and Skywars Stars (SWSTAR): ")
        allPlayers = self.listPlayers()
        if lb == "L":
            for playerName in allPlayers:
                hypixelAPI = requests.get(f"https://api.hypixel.net/player?key={self.TOKEN}&name={playerName}").json()
                xp = hypixelAPI["player"]["networkExp"]

                self.playerDict[playerName] = xp

            levelsDict = {}
            levelsKeys = sorted(allPlayers, key=self.playerDict.get, reverse=True)

            for key in levelsKeys:
                levelsDict[key] = self.playerDict[key]

            currentPos = 1
            for player in levelsDict:
                print(f"{currentPos}. {player}: {levelsDict[player]}")
                currentPos += 1

if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    leaderboard.run()
    