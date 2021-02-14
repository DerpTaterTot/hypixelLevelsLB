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

calculations = calculations()
load_dotenv()
class Leaderboard():
    def __init__(self) -> None:
        # get your own api token by typing /api new in hypixel
        self.TOKEN = os.getenv('API_TOKEN')
        
        self.playerDict = {}
        
        self.hypixelAPI = lambda playerName: requests.get(f"https://api.hypixel.net/player?key={self.TOKEN}&name={playerName}").json()
        
        self.currentOptions = ["L", "BWSTAR", "SWSTAR"]
        pass
    
    def listPlayers(self):
        player = " "
        playerNames = []        
        while True:
            player = input("input a player you want to add to the leaderboard (type exit to finish typing): ")
            api = self.hypixelAPI(player)

            if player == "exit":
                break

            elif not api["player"]:
                print("unable to find that player")
            
            elif player in playerNames:
                print("you have already entered this player")

            else:
                playerNames.append(player)
        return playerNames
    
    def findRankings(self, allPlayers, playerDict, type):
        levelsDict = {}
        levelsKeys = sorted(allPlayers, key=playerDict.get, reverse=True)

        for key in levelsKeys:
            levelsDict[key] = self.playerDict[key]

        currentPos = 1
        for player in levelsDict:
            print(f"{currentPos}. {player}: {int(levelsDict[player])} {type}")
            currentPos += 1
            
    def run(self) -> None:
        lb = input("what do you want a leaderboard for? current options are Hypixel Levels (L), Bedwars Stars (BWSTAR), and Skywars Stars (SWSTAR): ")
        
        if lb not in self.currentOptions:
            print("i can't find that option")
            return
        
        allPlayers = self.listPlayers()
        
        if lb == "L":
            for playerName in allPlayers:
                api = self.hypixelAPI(playerName)
                xp = api["player"]["networkExp"]

                self.playerDict[playerName] = xp

            self.findRankings(allPlayers, self.playerDict, "xp")
                
        elif lb == "SWSTAR":
            for playerName in allPlayers:
                api = self.hypixelAPI(playerName)
                swxp = api["player"]["stats"]["SkyWars"]["skywars_experience"]
                
                star = calculations.skywarsLevel(swxp)
                
                self.playerDict[playerName] = star
            
            self.findRankings(allPlayers, self.playerDict, "stars")
        
        elif lb == "BWSTAR":
            for playerName in allPlayers:
                api = self.hypixelAPI(playerName)
                bwstar = api["player"]["achievements"]["bedwars_level"]

                self.playerDict[playerName] = bwstar

            self.findRankings(allPlayers, self.playerDict, "stars")
            
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    leaderboard.run()
    