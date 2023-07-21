import requests
import os
import time
from mojang import API

MojangAPI = API()

userinput = str(input("Enter the player's minecraft username >>> "))

uuid = MojangAPI.get_uuid(userinput)
requestlink = str("https://api.hypixel.net/player?key=9087e613-4ce3-4945-b8d8-9af50b903b03&uuid="+ uuid)
hydata = requests.get(requestlink).json()

swl = hydata["player"]["stats"]["SkyWars"]["levelFormatted"]
swl = swl[2:]
swk = hydata["player"]["stats"]["SkyWars"]["kills"]
swd = hydata["player"]["stats"]["SkyWars"]["deaths"]
kdr = str(float(swk / swd))
kdr = kdr[:4]
gw = hydata["player"]["stats"]["SkyWars"]["wins"]
gp = hydata["player"]["stats"]["SkyWars"]["games_played_skywars"]
winratio = (gw / gp)
winper = str(float(winratio * 100))
winper = winper[:5]
coins = hydata["player"]["stats"]["SkyWars"]["coins"]
pt = hydata["player"]["stats"]["SkyWars"]["time_played"]
pt = int(pt / 60)
pt = int(pt / 60)
bwl = str(hydata["player"]["achievements"]["bedwars_level"])
bwcoins = str(hydata["player"]["stats"]["Bedwars"]["coins"])
fk = float(hydata["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
fd = float(hydata["player"]["stats"]["Bedwars"]["final_deaths_bedwars"])
fkdr = str((fk / fd))
fkdr = float(fkdr[:4])
x = "You might want to dodge this game!"
bgp = float(hydata["player"]["stats"]["Bedwars"]["games_played_bedwars"])
bgw = float(hydata["player"]["stats"]["Bedwars"]["wins_bedwars"])
bwp = (bgw / bgp)
bwp = str(bwp * 100)
bwp = float(bwp[:5])

gamemode = input("(S)kywars or (B)edwars >>> ")

if gamemode == "S" or gamemode == "s":
    os.system('cls')
    a = f"{userinput}'s Skywars Data"
    print(a)
    nod = len(a)
    print("-" * nod)
    print("Skywars Level: "+ swl)
    print(f"Coins: {coins}")
    print(f"KDR: {kdr}")
    print(f"Win Percentage: {winper}%")
    print(f"Playtime: {pt} Hours")
    time.sleep(650)

else:
    b = f"{userinput}'s Bedwars Data"
    print(b)
    bod = len(b)
    print("-" * bod)
    print("Bedwars Level: "+ bwl)
    print(f"Coins: {bwcoins}")
    print(f"FKDR: {fkdr}")
    print(f"Win Percentage: {bwp}%")
    if fkdr > 4 and bwp > 50:
        print("Comment: If this player is in your game, You may want to dodge!")
    if fkdr < 2:
        print("Comment: If this player is in your game, They will be easy to kill!")
    if fkdr < 2 and bwp > 40:
        print("Comment: If this player is in your game,They might be getting boosted due to their low FKDR and high win percentage")
        time.sleep(650)

