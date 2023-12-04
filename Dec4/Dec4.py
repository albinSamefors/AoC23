def parse_input():
    data = open('input.txt',"r").read().split("\n")
    return data

def parse_card(inputString):
    yourNumbers = []
    winningNumbers = []
    your, win = inputString.split("|")
    tmp_num = ""
    for character in your:
        if character.isdigit():
            tmp_num += character
        else:
            if len(tmp_num) > 0:
                yourNumbers.append(int(tmp_num))
                tmp_num = ""
    if len(tmp_num) > 0:
        yourNumbers.append(int(tmp_num))
        tmp_num = ""
        
    for character in win:
        if character.isdigit():
            tmp_num += character
        else:
            if len(tmp_num) > 0:
                winningNumbers.append(int(tmp_num))
                tmp_num = ""
    if len(tmp_num) > 0:
        winningNumbers.append(int(tmp_num))
    return yourNumbers, winningNumbers

def evaluateWin(yourNumbers, winningNumbers):
    matchingList = []
    for number in yourNumbers:
        if number in winningNumbers:
            matchingList.append(number)
    #print(matchingList)

    win_sum = 0
    for i in range(len(matchingList)):
        if i == 0:
            win_sum +=1
        else:
            win_sum *=2
    return win_sum, matchingList

def task1():
    initialInput = parse_input()
    tot_sum = 0
    for line in initialInput:
        your, win = parse_card(line)
        points, matching = evaluateWin(your, win)
        tot_sum += points
    #print(tot_sum)

def task2():
    initialInput = parse_input()
    parsed_input = []
    for line in initialInput:
        parsed_input.append([line,1])
    for i in range(len(parsed_input)):
        card_counter = 0
        while (parsed_input[i][1]-card_counter) > 0:
            #parsed_input[i].append(initialInput[i])
            your, win = parse_card(initialInput[i])
            points, matching = evaluateWin(your,win)
            for j in range(1,len(matching)+1):
                parsed_input[i+j][1] +=1 
            card_counter +=1
    sumofcards = 0
    for card in parsed_input:
        sumofcards += card[1]
    print(sumofcards)
        
        

def main():
    
        
    
    pass

if __name__ == "__main__":
    main()