def parse_input():
    data = open('input.txt',"r").read().split("\n")
    return data

def putIntoTuples(hand):
    separated = hand.split(" ")
    separated[1] = int(separated[1])
    return separated

def findValues(hand):
    list_of_values = [["A",0],["K",0],["Q",0],["J",0],["T",0],["9",0],["8",0],["7",0],["6",0],["5",0],["4",0],["3",0],["2",0],["1",0]]
    
    for value in hand:
        if value == "A":
            list_of_values[0][1] += 1
            pass
        elif value == "K":
            list_of_values[1][1] += 1
            pass
        elif value == "Q":
            list_of_values[2][1] += 1
            pass
        elif value == "J":
            pass
        elif value == "T":
            list_of_values[3][1] += 1
            pass
        else:
            list_of_values[12-int(value)][1] += 1
            pass
    returnList = []
    for value in list_of_values:
        if value[1] == 0:
            pass
        else:
            returnList.append(value)
    
    return returnList
            

def classifyCards(hand):
    hand[0] = findValues(hand[0])
    hand[0].sort(key = lambda x: x[1])
    
    print(hand)
        
        
        

def main():
    allHands = parse_input()
    parsedHands = []
    for hand in allHands:
        parsedHands.append(putIntoTuples(hand))
    for hand in parsedHands:
        hand = classifyCards(hand)
    

if __name__ == "__main__":
    main()