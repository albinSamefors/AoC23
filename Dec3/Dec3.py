
def parse_input():
    data = open('input.txt',"r").read().split("\n")
    return data

def createBlocks(top,mid,bot):
    return[top,mid,bot]
    
def findNumbers(mid):
    numbers_found = []
    tmp_digit = []
    for i in range(len(mid)):
        if mid[i].isdigit():
            tmp_digit.append(mid[i])
            
        else:
            if len(tmp_digit) > 0:
                numbers_found.append([tmp_digit,i-len(tmp_digit)])
                tmp_digit = []
        i += 1
    return numbers_found

def findRatioSymbol(mid):
    ratiosFound = []
    for i in range(len(mid)):
        if mid[i] == "*":
            ratiosFound.append(i)
    return ratiosFound

def numberInRange(number,ratioIndex):
    inRange = False
    for i in range(len(number[0])):
        numberindex = number[1] + i
        distance = abs(ratioIndex-numberindex)
        if distance > 1:
            pass
        else:
            inRange = True
    return inRange,number[0]
            
        

def calculateRatios(block):
    ratioSymbols = findRatioSymbol(block[1])
    numbersInBlock = [findNumbers(block[0]),findNumbers(block[1]),findNumbers(block[2])]
    foundNumbers = []
    foundNumbersInBlock = []
    for symbol in ratioSymbols:
        foundNumbers = []
        for block in numbersInBlock:
            for number in block:
                if numberInRange(number,symbol)[0]:
                    strNr = ""
                    for char in number[0]:
                        strNr += char
                        
                    foundNumbers.append(int(strNr))
        
        if(len(foundNumbers) == 2):
            print(foundNumbers)
            foundNumbersInBlock.append(foundNumbers)
        
    #print("FOUND RATIOS {}".format(foundNumbersInBlock))    
    ratiosum = 0
    
    for ratios in foundNumbersInBlock:
        ratiosum += (ratios[0] * ratios[1])
    return ratiosum
        
def createSquares(block):
    squareList = []
    numbers = findNumbers(block[1])
    for number in numbers:
        squareList.append([block[0][number[1]-1:(number[1] + len(number[0]) + 1)],
                           block[1][number[1]-1:(number[1] + len(number[0]) + 1)],
                          block[2][number[1]-1:(number[1] + len(number[0]) + 1)]])
    return squareList

def classifySquare(square):
    for symbol in square[0]:
        if symbol == ".":
            pass
        else:
            return True
    for symbol in square[2]:
        if symbol == ".":
            pass
        else:
            return True
    if square[1][0] != ".":
        return True
    if square[1][-1] != ".":
        return True
    return False

def extractNumber(mid):
    print(mid[1:-1])
    return int(mid[1:-1])

def task1():
    lines = parse_input()
    blocks = []
    squares = []
    for i in range(1,len(lines)-1):
        blocks.append(createBlocks(lines[i-1],lines[i],lines[i+1]))
        
    for block in blocks:
        unparsed_squares = createSquares(block)
        for square in unparsed_squares:
            if classifySquare(square):
                squares.append(square)
    
    totVal = 0
    for square in squares:
        totVal += extractNumber(square[1])
        
    print(totVal)

def main():
    lines = parse_input()
    blocks = []
    for i in range(1,len(lines)-1):
        blocks.append(createBlocks(lines[i-1],lines[i],lines[i+1]))
    totsum = 0
    for block in blocks:
        totsum += calculateRatios(block)
    print(totsum)
if __name__ == "__main__":
    main()