import json

#function
def avrg_lvl():
    try:
        open("player.json")
        lvl = 0
        with open("player.json","r") as file:
            data = json.load(file)
            for player in data:
                lvl += player["level"]
            avrg_lvl = lvl/len(player)
            print("The average level of the four player is ", avrg_lvl)
            return avrg_lvl
    except FileNotFoundError:
        print("Error: The file 'data.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
def type(avrg_lvl):
    try:
        open("player.json")
        lvl = 0
        with open("player.json","r") as file:
            data = json.load(file)
            for player in data:
                lvl = player["level"]
                if lvl < 25:
                    player["class"] = "beginner"
                    with open(file, 'r') as file1:
                        json.dump(data, file, indent=9)
                elif lvl < 50:
                    player["class"] = "apprentice"
                    with open(file, 'w') as file:
                        json.dump(data, file, indent=9)
                elif lvl < 75:
                    player["class"] = "expert"
                    with open(file, 'w') as file:
                        json.dump(data, file, indent=9)
                elif lvl < 100:
                    player["class"] = "master"
                    with open(file, 'w') as file:
                        json.dump(data, file, indent=9)

    except FileNotFoundError:
        print("Error: The file 'data.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
def online():
    with open("player.json", "r") as file:
        data = json.load(file)
        print("Online player:")
        for player in data:
            if player["is_online"] == "true":
                print(player["name"])
def print_all():
    with open("player.json", "r") as file:
        data = json.load(file)
        for player in data:
            print(player)

#main
avrg_lvl = avrg_lvl()
online()
type(avrg_lvl)
print_all()

