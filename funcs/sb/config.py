import json

with open('config.json', 'r') as file:
    config = json.load(file)

api = config["api"]
debug = config["debug"]
outputToFile = config["outputToFile"]
delay = config["delay"]
printSnusbaseLogs = config["printSnusbaseLogs"]
onlyOutputConfirmed = config["onlyOutputConfirmed"]
outputSnusbaseLogs = config["outputSnusbaseLogs"]