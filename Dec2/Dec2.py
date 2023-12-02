def parse_input():
    data = open('input.txt',"r").read().split("\n")        
    return data

def classifyInput(entry):
    entry = entry[1:]
    parted = entry.split(" ")
    return int(parted[0]), parted[1]
    

def evaluate_game(gameLine,max_red, max_green, max_blue):
    line = gameLine.split(":")
    line = line[1]
    games = line.split(";")
    print(games)
    for subgame in games:
       gameData = subgame.split(",")
       for entry in gameData:
            amount, color = classifyInput(entry)
            if color == "red":
                if amount > max_red:
                    return False
            elif color == "green":
                if amount > max_green:
                    return False
                
            else:
                #Color must then be blue
                if amount > max_blue:
                    return False
    return True
  
  
def findLeastAmountOfDice(gameLine):
    line = gameLine.split(":")
    line = line[1]
    game = line.split(";")
    
    max_red = 0
    max_green = 0
    max_blue = 0
    
    for subgame in game:
       gameData = subgame.split(",")
       for entry in gameData:
           amount, color = classifyInput(entry)
           if color == "red":
               if amount > max_red:
                   max_red = amount
           elif color == "green":
                if amount > max_green:
                    max_green = amount
           else:
               if amount > max_blue:
                   max_blue = amount
    return max_red, max_green, max_blue

def main():
    data = parse_input()
    didPass = evaluate_game(data[83],12,13,14)
    totSum = 0
    i = 1
    gameList = []
    for game in data:
        gameList.append(findLeastAmountOfDice(game))
    i = 0
    powerList = []
    for diceset in gameList:
        r = diceset[0]
        g = diceset[1]
        b = diceset[2]
        powerList.append(r*g*b)
    print(sum(powerList))
        

if __name__ == "__main__":
    main()