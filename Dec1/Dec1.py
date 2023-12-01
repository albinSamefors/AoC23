import re
def parse_input():
    data = open('input.txt',"r").read().split("\n")
    return data

def detectWrittenNumbers(row):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    foundNumberIndexes = []
    for number in numbers:
        indexes = [m.start() for m in re.finditer(number, row)]
        print("FOUND INDEXES {}".format(indexes))
        if len(indexes)>0:
            for index in indexes:
                foundNumberIndexes.append([index,str(numbers.index(number) + 1)])
        else:
            pass
    return foundNumberIndexes

def detectNumericalNumbers(row):
    foundNumberIndexes = []
    i = 0
    for char in row:
        if char.isdigit():
            foundNumberIndexes.append([i,char])
        else:
            pass
        i+=1
    return foundNumberIndexes

def calculateTrueSum(row):
    foundAlphabetical = detectWrittenNumbers(row)
    foundNumerical = detectNumericalNumbers(row)
    allFoundNumbers = foundAlphabetical + foundNumerical
    sortedNumbers = sorted(allFoundNumbers)
    return int(sortedNumbers[0][1] + sortedNumbers[-1][1])
              

def calculateCombination(row):
    digits = []
    for char in row:
        if char.isdigit():
            digits.append(char)
        else:
            pass
    result = digits[0] + digits[-1]
    return result

def calculateResultOfAllInput(data):
    sum = 0
    for line in data:
        sum += int(calculateTrueSum(line))
    print(sum)

def main():
    data = parse_input()
    calculateResultOfAllInput(data)
    pass

if __name__ == "__main__":
    main()