def parse_input():
    data = open('input.txt',"r").read().split("\n")
    return data

def add_into_lists():
    parsed = parse_input()
    print(parsed)
    timeList = []
    distanceList = []
    time = parsed[0].split("    ")[2:]
    distance = parsed[1].split("   ")[1:]
    for tim in time:
        timeList.append(int(tim))
    for dist in distance:
        distanceList.append(int(dist))
    return timeList, distanceList

def find_ways_to_win(time, distanceToBeat):
    winning_loads = []
    wins = 0
    started_winning_at = 0
    for speed in range(25420,time):
        achieved_range = 0
        achieved_range = speed * abs(time-speed)
        if achieved_range > distanceToBeat:
            #winning_loads.append(achieved_range)
            wins += 1
            print("distance {}".format(achieved_range))
            started_winning_at = speed
            
    started_losing_at = 0
    print("WINS {}".format(wins))
    return winning_loads


def partOne():
    times, distances = add_into_lists()
    allWinners = []
    for i in range(4):
       winningWays = find_ways_to_win(times[i], distances[i])
       allWinners.append(len(winningWays))
    pass
    product = 1
    for ways in allWinners:
        product *= ways
    print(product)

def main():
    times, distances = add_into_lists()
    timeToUse = 1
    distanceToBeat = 1
    for time in times:
        timeToUse *= time
    for distance in distances:
        distanceToBeat*= distance
    waysToWin = find_ways_to_win(timeToUse,distanceToBeat)
    print(waysToWin)
if __name__ == "__main__":
    main()