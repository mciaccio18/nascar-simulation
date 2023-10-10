'''
Mike Ciaccio
11/8/2021
CS 152
Section A

This file contains the code for running a simulation of the NASCAR season. It has various methods to take in input, and then 
runs calculations to find the season champion and other statistics.

Upon running this program, a window will appear that shows key statistics to showcase the outcome of the season.

To run this file, type python3 race.py

'''
#Import statements to bring in graphics, drivers and random.
import drivers as dr
import random
import graphics as gr
import math

#These IDX values are for the Driver class to take in data from the spreadsheet. These numbers correspond to the rows in the spreadsheet.
IDXName = 0
IDXNumber = 1
IDXAge = 2
IDXTeam = 3
IDXEquipmentRating = 4
IDXShortTrackTop10 = 5
IDXShortTrackTop5 = 6
IDXShortTrackWins = 7
IDXIntermediateTop10 = 8
IDXIntermediateTop5 = 9
IDXIntermediateWins = 10
IDXRoadCourseTop10 = 11
IDXRoadCourseTop5 = 12
IDXRoadCourseWins = 13
IDXSuperSpeedwayTop10 = 14
IDXSuperSpeedwayTop5 = 15
IDXSuperSpeedwayWins = 16
IDXChampionships = 17

#These IDX values are for the Track class to take in data from the spreadsheet. These numbers correspond to the rows in the spreadsheet.
IDXTrackName = 0
IDXTrackType = 1
IDXTrackLength = 2
IDXRaceName = 3
IDXDate = 4
IDXLaps = 5



def collectTrackData():
    '''This file is meant to open the Race_Tracks_Final.csv spreadsheet, and collect the data from it. The data that is collected is
    passed into creating a track object for each set of data in the file. Then, a dictionary containing the race number as the keys, corresponding to the
    proper track object is returned.'''
    #Create empty track dictionary
    tracks = {}
    #Open the file and read the header
    fp = open('Race_Tracks_Final.csv', 'r')
    fp.readline()

    race = 1
    for line in fp:
        #For each line in the file, split it into a list of strings.
        words = line.split(',')

        #Slice up this string to get various values, assign them to local variables
        trackName = words[IDXTrackName]
        trackType = words[IDXTrackType]
        trackLength = words[IDXTrackLength]
        raceName = words[IDXRaceName]
        date = words[IDXDate]
        laps = words[IDXLaps]
        
        #Pass in these local variables to create a track object.
        track = dr.Track(trackName, trackType, trackLength, raceName, date, laps, race)

        #Add the track object to the dictionary, with the race number as the key.
        tracks[race] = track
        race += 1

    #Close the file and return the completed track dictionary.
    fp.close()
    return tracks

    
def collectDriverData():
    '''This file is meant to open the Nascar_Driver_Stats.csv spreadsheet, and collect the data from it. The data that is collected is
    passed into creating a driver object for each set of data in the file. Then, a dictionary containing the driver name as the keys, corresponding to the
    proper driver object is returned.'''
    #Create an empty driver dictionary
    drivers = {}

    #Open the file and read the header
    fp = open('Nascar_Driver_Stats_Final.csv', 'r')
    fp.readline()
    
    for line in fp:
        #For each line in the file, split it into a list of strings.
        words = line.split(',')
        
        #Slice up this string to get various values, assign them to local variables
        name = words[IDXName]
        number = words[IDXNumber]
        age = words[IDXAge]
        team = words[IDXTeam]
        equipmentRating = words[IDXEquipmentRating]
        shortTrackTop10 = words[IDXShortTrackTop10]
        shortTrackTop5 = words[IDXShortTrackTop5]
        shortTrackWins = words[IDXShortTrackWins]
        intermediateTop10 = words[IDXIntermediateTop10]
        intermediateTop5 = words[IDXIntermediateTop5]
        intermediateWins = words[IDXIntermediateWins]
        roadCourseTop10 = words[IDXRoadCourseTop10]
        roadCourseTop5 = words[IDXRoadCourseTop5]
        roadCourseWins = words[IDXRoadCourseWins]
        superSpeedwayTop10 = words[IDXSuperSpeedwayTop10]
        superSpeedwayTop5 = words[IDXSuperSpeedwayTop5]
        superSpeedwayWins = words[IDXSuperSpeedwayWins]
        championships = words[IDXChampionships]

        #Pass in these local variables to create a driver object.
        driver = dr.Driver(name,number,team,age,equipmentRating,shortTrackTop10, shortTrackTop5, shortTrackWins, intermediateTop10, intermediateTop5, intermediateWins, roadCourseTop10, roadCourseTop5, roadCourseWins, superSpeedwayTop10, superSpeedwayTop5, superSpeedwayWins, championships)

        #Add the driver object to the dictionary, with the driver name as the key.
        drivers[name] = driver

    #Close the file and return the completed driver dictionary.
    fp.close()
    return drivers


def generateStartingLineup(driverDict, typeOfTrack):
    '''This function takes in a driverDictionary, and a string that tells the type of track. It then calculates
    the rating for each driver based on the type of track and a randomness factor. Then, based on this, a lineup is ge
    nerarted for the start of a race. It returns a dictionary of the starting lineup with keys being starting position,
    and the corresponding driver name. '''
    #Initialize dictionaries for 
    trackRatings = {}
    ratings = []
    startingLineUp = {}

    for driver in driverDict:
        #For each driver, get the object instead of the just the name.
        currentDriverObject = driverDict[driver]
        
        #Create a randomness factor
        randomnessFactor = random.random()*5
        #Based on the input parameter, assign a rating to the driver plus a randomness factor
        if typeOfTrack == 'Short Track':
            rating = currentDriverObject.shortTrackRating + randomnessFactor
        elif typeOfTrack == 'Intermediate':
            rating = currentDriverObject.intermediateTrackRating + randomnessFactor 
        elif typeOfTrack == "Road Course":
            rating = currentDriverObject.roadCourseRating + randomnessFactor 
        elif typeOfTrack == "SuperSpeedway":
            rating = currentDriverObject.superSpeedwayRating + 2*randomnessFactor
        #Create a dictionary that has keys the ratings for the track, and the corresponding driver name
        trackRatings[rating] = driver
    
    #Add the calculated rating for each driver to a list
    for number in trackRatings:
        ratings.append(number)

    #Sort this list in reverse order, so that the least rating is the first element
    ratings.sort(reverse = True)
    
    #For each rating in the list of now sorted ratings, get the driver based on the trackRatings dict
    #Then, add each driver to a final dictionary with the starting position as the key.
    for i in range(len(ratings)):
        driver = trackRatings[ratings[i]]
        #print('Starting in', i+1 , 'place is', driver, 'with a rating of', ratings[i] )
        #print('Starting in', 39-i , 'place is', driver, 'with a rating of', 39-i )
        startingLineUp[i+1] = driver

    #return the startingLineup dictionary with the places and corresponding drivers.
    return startingLineUp


def simulateLap(driverDictionary, lineup):
    '''This function takes in the driverDictionary and a lineup of drivers. It then adds values to each driver 
    based on randomness and includes chances of having a crash or a flat tire. These values are then sorted, and 
    a new running order is produced, simulating drivers passing each other. The lineup after the lap is then returned.'''

    #Initialize empty lists and dictionaries to be used later
    driverTotals = []
    newLineup = {}
    interList = []
    finalLineup = {}

    #For each rating value that each driver has. 
    for position in lineup:
        #append to a list, the drivers name and position.
        driverName = lineup[position]
        miniList = [driverName, float(position)]
        #Append each of the small lists to a big 2D list.
        driverTotals.append(miniList)
    #So, now driverTotals contains a bunch of mini lists with a driver name and rating.

   
    for drivers in driverTotals:
        #For each driver and ratings combination
        randomPoints = random.random() * random.randint(-1,1)
        if randomPoints == 0:
            randomPoints = random.random()
        drivers[1] += randomPoints/2
        #Add a random amount of points to each driver to simulate a pass in a race.
        
        #Add a chance that the driver will crash, to simulate this, the rating is multiplied by 100, so they can't pass other drivers anymore
        DNFChance = 0.0003
        if random.random() < DNFChance:
            drivers[1] = drivers[1] + 10000

        #Add a chance that the driver will have a flat tire. To simulate this, a value of 20 is added to the rating to simulate losing position.
        flatTireChance = 0.005
        if random.random() < flatTireChance:
            drivers[1] += 20
        #Assign to a newLineup the updated rating as a key, and the driver name as the value in the dict.
        newLineup[drivers[1]] = drivers[0]
        #Append the ratings to a list.
        interList.append(drivers[1])

    #Sort this list 
    interList.sort(reverse = True)
   
   #For each rating in the list, create a final dictionary with the score and the key, and the driver name.
    for score in interList:
        finalLineup[score] = newLineup[score]
    #So, now the dictionary finalLineup has the updated running order and the corresponding driver name
    #place = 39
    #for driver in finalLineup:
        #print('Currently in', place, 'place is ', finalLineup[driver], 'with a score of ', driver)
        #place -= 1
    #firstPlaceNum = interList[38]
    #currentLeader = finalLineup[firstPlaceNum]
    
    #Return the finalLineup
    return finalLineup


def printWinner(lineup):


    '''Takes in a lineup and returns the current leader or winner'''
    order = 39
    for element in lineup:
        #Option to print out the entire running order.
        #print("Currently in ", order, 'is', lineup[element], 'with a score of ', element )
        order -= 1
    #print('The winner is', lineup[element])
    #return the name of the winner
    return lineup[element]

def caution(drivers, runningOrder, lap):
    #print("Caution on lap ", lap)
    orderAfterCaution = {}

    DNFs = 0
    
    #print(runningOrder)
    #print()
    for driverPosition in runningOrder:
        if driverPosition > 1000:
            DNFs += 1
    position = 39 - DNFs
    for driverPosition in runningOrder:
        if driverPosition < 1000:
            orderAfterCaution[position] = runningOrder[driverPosition]
            position -= 1
        else:

            orderAfterCaution[driverPosition] = runningOrder[driverPosition]
        

    #print(orderAfterCaution)
    #print()
    #print()
    return orderAfterCaution

def updateLapDownCars(drivers, runningOrder):
    frozenField = caution(runningOrder)
    

def simulateRace(drivers, track, numOfLaps, raceNumber):
    '''This function takes in the drivers dictionary, the track dictionary, the number of laps, and the race number.'''
    #Calculate the starting lineup
    runningOrder = generateStartingLineup(drivers, track)
    startingLineup = runningOrder
    #Calculate the amount of laps that corresponds to stage1End and stage2End
    stage1End = int(numOfLaps/4)
    stage2End = int(numOfLaps/2)

    #print(runningOrder)
    lapsSinceLastCaution = 0
    chanceOfCaution = .025
    #Simulate the amount of laps in the race.
    for i in range(numOfLaps):
        
        isCaution = False


        #Pause at the end of stage1 and calculate the stage points
        if i == stage1End:
            calculateStagePoints(runningOrder, drivers)
            isCaution = True
        #Pause at the end of stage2 and calculate the stage points
        if i == stage2End:
            calculateStagePoints(runningOrder, drivers)
            isCaution = True

        runningOrder = simulateLap(drivers, runningOrder)


        if random.random() < chanceOfCaution:
            isCaution = True
        if isCaution:
            runningOrder = caution(drivers, runningOrder, i)
            chanceOfCaution = .025
            lapsSinceLastCaution = 0
        else:
            chanceOfCaution += .0001
            lapsSinceLastCaution += 1

        
        


        
        #Pause at the end of stage1 and calculate the stage points
        if i == stage1End:
            calculateStagePoints(runningOrder, drivers)
        #Pause at the end of stage2 and calculate the stage points
        if i == stage2End:
            calculateStagePoints(runningOrder, drivers)
        
    #After the race is complete, calculate the race stats 
    calculateRaceStats(runningOrder, drivers, track, raceNumber)
    #Return the final running order of the race.
    return startingLineup, runningOrder


def calculateStagePoints(runningOrder, driverDictionary):
    '''This function takes in the current running order and the driver dictionary. It then adds stage points, 
    stage wins, and playoff points based on the current position of the drivers.'''
    #Create a dictionary for holding the top ten values and the finishing position
    top10 = {}
    i = 1
    p = 10
    for finishingTotal in runningOrder:
        #Add the top ten finishers at the stage end to a dictionary with where they finished.
        if i > 29:
            top10[p] = runningOrder[finishingTotal]
            p -= 1
        i += 1
        
    pointsEarned = 10
    #Then, for each driver in the top 10, give them additional points. 1rst gets 10, 2nd gets 9, and so on.
    for place in top10:
        driverName = top10[place]
        driverObject = driverDictionary[driverName]
        driverObject.addStagePoints(pointsEarned)
        pointsEarned -= 1
        #For the winner of the stage, add a stage win, and a playoff point for the driver object.
        if place == 1:
            driverObject.addStageWin(1)
            driverObject.addPlayoffPoints(1)


def calculateRaceStats(finishingOrderDict, driverDictionary, track, raceNumber):
    '''This function takes in a finishing order dictionary of a race, the driver dictionary, the track dictionary,
    and the race number. Based on this finishing order dictionary, add points to each driver according to how
    they finished. Then, for the races in the playoffs, add points to the proper variable based on which round of the
    playoffs they are in. Also, if a race is won in the playoffs, and the driver is still in the playoffs, automatically
    move them to the next round.'''
    #Create a dictionary with keys being finishing position, and the value being the driver.
    finalOrder = {}
    place = 39
    for driver in finishingOrderDict:
        finalOrder[place] = finishingOrderDict[driver]
        place -= 1
    points = 2
    for finishingPosition in finalOrder:
        
        driverName = finalOrder[finishingPosition]
        driverObject = driverDictionary[driverName]
        currentPoints = driverObject.getPointTotal()
        #If the driver finished 35+, add one point to the proper variable, both total points and the proper playoff round.
        if finishingPosition > 35:
            #Add one point to the total points 
            driverObject.setPointTotal(currentPoints + 1)
            if driverObject.getMadePlayoffs() and raceNumber > 26 and raceNumber <= 29:
                #If a driver is in the playoffs, and it is in the first round of the playoffs, add one point to round of 16 points
                driverObject.addRoundOf16Points(1)
            if driverObject.getMadeRoundOf12() and raceNumber > 29 and raceNumber <= 32:
                #If a driver is in the round of 12, and it is the second round of the playoffs, add one point to round of 12 points.
                driverObject.addRoundOf12Points(1)
            if driverObject.getMadeRoundOf8() and raceNumber > 32 and raceNumber <= 35:
                #If a driver is in the round of 8, and it is in the third round of the playoffs, add one point to round of 8 points
                driverObject.addRoundOf8Points(1)
            if driverObject.getMadeRoundOf4() and raceNumber == 36:
                #If a driver is in the round of 4, and it is in the final round of the playoffs, add one point to the round of 4 points
                driverObject.addRoundOf4Points(1)
                
        elif finishingPosition == 1:
            #Add 40 points to the current points totals for the season
            driverObject.setPointTotal(currentPoints + 40)
            if driverObject.getMadePlayoffs() and raceNumber > 26 and raceNumber <= 29:
                #If the driver has made the playoffs, and it is in the first round of the playoffs, add 40 points to the round of 16 points
                driverObject.addRoundOf16Points(40)
            if driverObject.getMadeRoundOf12() and raceNumber > 29 and raceNumber <= 32:
                #If the driver has made the round of 12, and it is in the second round of the playoffs, add 40 points to the round of 12 points
                driverObject.addRoundOf12Points(40)
            if driverObject.getMadeRoundOf8() and raceNumber > 32 and raceNumber <= 35:
                #If the driver has made the round of 8, and it is in the third round of the playoffs, add 40 points to the round of 8 points
                driverObject.addRoundOf8Points(40)
            if driverObject.getMadeRoundOf4() and raceNumber == 36:
                #If the driver has made the round of 4, and it is in the last round of the playoffs, add 40 points to the round of 8 points
                driverObject.addRoundOf4Points(40)
                
        else:
            #If the driver finished between 2-35, add points based on finishing position.
            driverObject.setPointTotal(currentPoints + points)
            if driverObject.getMadePlayoffs() and raceNumber > 26 and raceNumber <= 29:
                #If the driver has made the playoffs, and it is in the first round of the playoffs, add the proper amount of points to round of 16 points
                driverObject.addRoundOf16Points(points)
            if driverObject.getMadeRoundOf12() and raceNumber > 29 and raceNumber <= 32:
                #If the driver has made the round of 12, and it is in the second round of the playoffs, add the proper amount of points to round of 12 points
                driverObject.addRoundOf12Points(points)
            if driverObject.getMadeRoundOf8() and raceNumber > 32 and raceNumber <= 35:
                #If the driver has made the round of 8, and it is in the third round of the playoffs, add the proper amount of points to round of 8 points
                driverObject.addRoundOf8Points(points)
            if driverObject.getMadeRoundOf4() and raceNumber == 36:
                #If the driver has made the round of 4, and it is in the last round of the playoffs, add the proper amount of points to round of 4 points
                driverObject.addRoundOf4Points(points)
                
            
            points += 1

        if finishingPosition <= 10:
            #If the driver finished in the top 10, add this to the drivers stats
            driverObject.addTop10()
        if finishingPosition <= 5:
            #If the driver finished in the top 5, add this to the drivers stats.
            driverObject.addTop5()
        if finishingPosition == 1 and raceNumber <= 26:
            #If the driver won a race in the regular season, add a win, add 5 playoff points, add the track to races won, and set make playoffs true
            driverObject.addWin()
            driverObject.addPlayoffPoints(5)
            driverObject.addRaceWon(track)
            driverObject.setMadePlayoffs(True)
    
        if finishingPosition == 1 and raceNumber > 26 and raceNumber <= 29 and driverObject.getMadePlayoffs():
            #If a playoff driver wins a race in the first round, add the proper stats, and move them to the next round of the playoffs.
            driverObject.addWin()
            driverObject.addPlayoffPoints(5)
            driverObject.addRaceWon(track)
            driverObject.setMadeRoundOf12(True)
        elif finishingPosition == 1 and raceNumber > 26 and raceNumber <= 29:
            #If a non playoff driver wins a race in the first round of the playoffs, add the proper stats.
            driverObject.addWin()
            driverObject.addPlayoffPoints(5)
            driverObject.addRaceWon(track)

        if finishingPosition == 1 and raceNumber > 29 and raceNumber <= 32 and driverObject.getMadeRoundOf12():
            #If a driver in the round of 12 wins a race in the second round, add the proper stats, and move them into the next round of the playoffs
            driverObject.addWin()
            driverObject.addPlayoffPoints(5)
            driverObject.addRaceWon(track)
            driverObject.setMadeRoundOf8(True)
        elif finishingPosition == 1 and raceNumber > 29 and raceNumber <= 32:
            #If a non playoff driver wins a race in the second round of the playoffs, add the proper stats.
            driverObject.addWin()
            driverObject.addPlayoffPoints(5)
            driverObject.addRaceWon(track)

        if finishingPosition == 1 and raceNumber > 32 and raceNumber <= 35 and driverObject.getMadeRoundOf8():
            #If a driver in the round of 8 wins a race in the third round of the playoffs, add the proper stats, and move them into the next round of the playoffs.
            driverObject.addWin()
            driverObject.addPlayoffPoints(5)
            driverObject.addRaceWon(track)
            driverObject.setMadeRoundOf4(True)
        elif finishingPosition == 1 and raceNumber > 32 and raceNumber <= 35:
            #If a non playoff driver wins a race in the third round of the playoffs, add the proper stats.
            driverObject.addWin()
            driverObject.addPlayoffPoints(5)
            driverObject.addRaceWon(track)

        if finishingPosition == 1 and raceNumber == 36 and driverObject.getMadeRoundOf4():
            #If a driver in the round of 4 wins the final race, add the proper stats, and make them the champion
            driverObject.addWin()
            driverObject.addPlayoffPoints(5)
            driverObject.addRaceWon(track)
            driverObject.setWonChampionship(True)
        elif finishingPosition == 1 and raceNumber == 36:
            #If a non playoff driver wins the final race, add the proper stats.
            driverObject.addWin()
            driverObject.addPlayoffPoints(5)
            driverObject.addRaceWon(track)


        
            #print(driverName, 'won at', track, 'and has made the playoffs')
        driverObject.addTotalFinish(finishingPosition)
    
def printBiggestMover(drivers, startingOrder, finishingOrder):
    maxDriver = ''
    maxMovement = 0
    maxStart = 0
    maxFinish = 0
    minDriver = ''
    minMovement = 100
    minStart = 0
    minFinish = 0
    totalMovement = 0
    driverNum = 0
    for driver in drivers:
        startingPosition = startingOrder[driver]
        finishingPosition = finishingOrder[driver]
        movement = startingPosition - finishingPosition
        totalMovement += abs(movement)
        driverNum += 1 
        #print(movement)
        if abs(movement) > maxMovement:
            maxMovement = abs(movement)
            maxDriver = driver
            maxStart = startingPosition
            maxFinish = finishingPosition
        if abs(movement) < minMovement:
            minMovement = movement
            minDriver = driver
            minStart = startingPosition
            minFinish = finishingPosition

    
    #print("The biggest mover in this race was", maxDriver, '.\nHe went from', maxStart, 'to', maxFinish)
    #print("The smallest mover of the race was", minDriver, '.\nHe went from', minStart, 'to', minFinish)
    #print("During this race, that average driver moved", totalMovement/driverNum)

    
    return maxDriver

def simulateSeason(drivers, tracks):
    '''This function takes in a dictionary of drivers and a dictionary of tracks. It then goes through the tracks and 
    simulates a race at each of them, stopping to calculate the drivers that move onto the various rounds of the playoffs, and the 
    eventual champion. It then calculates the season stats based on the information in the driver dictionary after the season.'''

    currentTrackType = tracks[3].getType()
    numOfLaps = int(tracks[3].getLaps())
    finalOrder = simulateRace(drivers, currentTrackType,numOfLaps, 3 )
    startingOrder = finalOrder[0]
    startingOrderFinal = {}

    for finishingPosition in startingOrder:
        startingOrderFinal[startingOrder[finishingPosition]] = finishingPosition


    #print('The starting order is', startingOrderFinal)

    #print()
    #print('The finishing order is ', finalOrder[1])

    
    
    finalOrderPosition = {}
    i = 39
    for position in finalOrder[1]:
        
        finalOrderPosition[finalOrder[1][position]] = i
        i -= 1

    #for driver in finalOrderPosition:
        #print(driver, 'finished', finalOrderPosition[driver])
    #orderDone(reversedict(finalOrderPosition))
    
    #print('The finishing order is ', finalOrderPosition)

    #printBiggestMover(drivers, startingOrderFinal, finalOrderPosition)
    #print("The biggest mover in this race was ", biggestMover)
    #Need to invert one of the dicitonaries to ensure proper use in new function printBiggestMovers.

    
    #Simulate the regular season races and calculate drivers that made the playoffs
    race = 1
    for i in range(len(tracks)-10):
        currentTrackType = tracks[race].getType()
        simulateRace(drivers, currentTrackType, int(tracks[race].getLaps()),race)
        race += 1
    calculatePlayoffs(drivers)

    #Simulate the first round of the playoffs, and calculate the drivers that made the round of 12
    for i in range(race, race + 3):
        currentTrackRoundOf12 = tracks[race].getType()
        simulateRace(drivers, currentTrackRoundOf12, int(tracks[race].getLaps()), race)
        race += 1
    calculateRoundOf12(drivers)

    #Simulate the second round of the playoffs, and calculate the drivers that made the round of 8
    for i in range(race, race + 3):
        currentTrackRoundOf8 = tracks[race].getType()
        simulateRace(drivers, currentTrackRoundOf8, int(tracks[race].getLaps()), race)
        race += 1
    calculateRoundOf8(drivers)

    #Simulate the third round of the playoffs, and calculate the drivers that made it to the round of 4
    for i in range(race, race + 3):
        currentTrackRoundOf4 = tracks[race].getType()
        simulateRace(drivers, currentTrackRoundOf4, int(tracks[race].getLaps()), race)
        race += 1
    calculateRoundOf4(drivers)

    #Simulate the final round of the playoffs, and determine the champion
    for i in range(race, race + 1):
        currentTrackChampionshipRound = tracks[race].getType()
        simulateRace(drivers, currentTrackChampionshipRound, int(tracks[race].getLaps()), race)
    calculateChampionship(drivers)
    
    #Calculate the season stats after the season is complete.
    calculateSeasonStats(drivers)


def calculateChampionship(driverDict):
    '''This function takes in the driver dictionary, goes through the dictionary, and produces the winner of the championship.'''
    championList = []
    driverPointsInRoundOf4 = {}
    middlePointsList = []

    counter = 0
    for driver in driverDict:
    #Go through the driver dictionary
        if driverDict[driver].getWonChampionship() == True :
            #If the driver has already won the race, add this driver to the list of champions
            championList.append(driver)

        if driverDict[driver].getMadeRoundOf4() == True:
            #For the remaining drivers in the playoffs, add the proper amount of points based on the final round finish
            driverPointsInRoundOf4[driverDict[driver].getRoundOf4Points()] = driver
            middlePointsList.append(driverDict[driver].getRoundOf4Points())
            counter += 1
    #Sort this list in reverse
    middlePointsList.sort(reverse = True)
    #Calculate how many open spots are left for the championship list
    openSpots = 1 - len(championList)
    
    i = 1
    for eachPoints in middlePointsList:
        #For the remaining drivers
        
        if i <= openSpots:
            #If there is open spots, append the highest scoring driver to the champions list
            driver = driverPointsInRoundOf4[eachPoints]
            
            if driver in championList:
                continue
            else:
                championList.append(driver)
                driverDict[driver].setWonChampionship(True)

        i += 1
    #Print out the driver who won the championship
    #print(championList)
    


def calculateRoundOf4(driverDict):
    '''This function takes in the driver dictionary, goes through the dictionary, and produces the list of the final four drivers'''
    roundOf4List = []
    driverPointsInRoundOf8 = {}
    middlePointsList = []

    counter = 0
    for driver in driverDict:
        #For each driver in the dictionary
        
        num = random.random()
        if driverDict[driver].getMadeRoundOf4() == True :
            #If the driver wins in the round of 8, add them to the list.
            roundOf4List.append(driver)

        if driverDict[driver].getMadeRoundOf8() == True:
            #For the remaining drivers, add the amount of points to each driver.
            driverPointsInRoundOf8[driverDict[driver].getRoundOf8Points()+num] = driver
            middlePointsList.append(driverDict[driver].getRoundOf8Points()+num)
            counter += 1
    middlePointsList.sort(reverse = True)
    #Sort this list
    openSpots = 4 - len(roundOf4List)
    #Find out how many open spots are left for points
    
    i = 1
    
    for eachPoints in middlePointsList:
        if i <= openSpots:
            #If there is open spots, append the highest scoring drivers to the next round.
            driver = driverPointsInRoundOf8[eachPoints]
            if driver in roundOf4List:
                #If the driver is already in the list, ignore it.
                continue
            else:
                roundOf4List.append(driver)

        i += 1
    
    
    #print(roundOf4List)
    for driver in roundOf4List:
        driverDict[driver].setMadeRoundOf4(True)
        #If the driver made the round of 4, update the driver's status


def calculateRoundOf8(driverDict):
    '''This function takes in the driver dictionary, goes through the dictionary, and produces the list of the final 8 drivers'''
    roundOf8List = []
    driverPointsInRoundOf12 = {}
    middlePointsList = []

    counter = 0
    for driver in driverDict:
        #For each driver in the dictionary
        num = random.random()
        if driverDict[driver].getMadeRoundOf8() == True :
            #If the driver wins in the round of 12, add them to the list.
            roundOf8List.append(driver)

        if driverDict[driver].getMadeRoundOf12() == True:
            #For the remaining drivers, add the amount of points to each driver.
            driverPointsInRoundOf12[driverDict[driver].getRoundOf12Points()+num] = driver
            middlePointsList.append(driverDict[driver].getRoundOf12Points()+num)
            counter += 1
    middlePointsList.sort(reverse = True)
    #Sort this list
    openSpots = 8 - len(roundOf8List)
    #Find out how many open spots are left for points
    
    i = 1
    for eachPoints in middlePointsList:
        if i <= openSpots:
            #If there is open spots, append the highest scoring drivers to the next round.
            driver = driverPointsInRoundOf12[eachPoints]
            if driver in roundOf8List:
                #If the driver is already in the list, ignore it.
                continue
            else:
                roundOf8List.append(driver)

        i += 1
    
    #print(roundOf8List)
    for driver in roundOf8List:
        driverDict[driver].setMadeRoundOf8(True)
        #If the driver made the round of 8, update the driver's status


def calculateRoundOf12(driverDict):
    '''This function takes in the driver dictionary, goes through the dictionary, and produces the list of the round of 12 drivers'''
    roundOf12List = []
    driverPointsInRoundOf16 = {}
    middlePointsList = []

    counter = 0
    for driver in driverDict:
         #For each driver in the dictionary
        num = random.random()
        if driverDict[driver].getMadeRoundOf12() == True :
            #If the driver wins in the round of 12, add them to the list.
            roundOf12List.append(driver)

        if driverDict[driver].getMadePlayoffs() == True:
            #For the remaining drivers, add the amount of points to each driver.
            driverPointsInRoundOf16[driverDict[driver].getRoundOf16Points()+num] = driver
            middlePointsList.append(driverDict[driver].getRoundOf16Points()+num)
            counter += 1
    middlePointsList.sort(reverse = True)
    #Sort this list
    openSpots = 12 - len(roundOf12List)
    #Find out how many open spots are left for points
    
    i = 1
    for eachPoints in middlePointsList:
        if i <= openSpots:
            #If there is open spots, append the highest scoring drivers to the next round.
            driver = driverPointsInRoundOf16[eachPoints]
            if driver in roundOf12List:
                continue
                #If the driver is already in the list, ignore it.
            else:
                roundOf12List.append(driver)

        i += 1
    #print(roundOf12List)
    for driver in roundOf12List:
        driverDict[driver].setMadeRoundOf12(True)
        #If the driver made the round of 8, update the driver's status
        

def calculatePlayoffs(driverDict):
    '''This function takes in the driver dictionary, goes through the dictionary, and produces the list of the playoff drivers'''
    
    playoffDrivers = []
    playoffDriversDict = {}

    driverSeasonPointsList = []
    middlePointsDict = {}
    seasonPoints = {}

    driversAddedByWins = 0
    driversAddedByPoints = 0
    #If the driver has won a race, add them to the list
    for driver in driverDict:
        if driverDict[driver].getMadePlayoffs() == True and len(playoffDrivers) < 16:
            
            playoffDrivers.append(driver)
    #print(playoffDrivers)
    #Calculate the amount of open spots left for points
    openSpots = 16 - len(playoffDrivers)
    if openSpots == 0:
        for driver in playoffDrivers:
            #Make a dictionary with playoff drivers and playoff points.
            playoffDriversDict[driver] = driverDict[driver].getPlayoffPoints()
            driversAddedByWins += 1

    else:
        for driver in playoffDrivers:
            #Calculate how many drivers have made the playoffs by wins
            playoffDriversDict[driver] = driverDict[driver].getPlayoffPoints()
            driversAddedByWins += 1
        for driver in driverDict:
            #Calculate the remaining drivers points
            driverSeasonPointsList.append(driverDict[driver].getPointTotal())
            middlePointsDict[driverDict[driver].getPointTotal()] = driver
        driverSeasonPointsList.sort(reverse = True)
        b = 1
        #Get a list of the top 16 points leaders
        for pos in driverSeasonPointsList:
            if b <= 16:
                driver = middlePointsDict[pos]
                points = driverDict[driver].getPointTotal()
                seasonPoints[driver] = points
            b += 1
        
        #print(seasonPoints)
        #If the driver is already in the playoffs, ignore it, then append the other drivers with the most points to the playoffs.
        for driver in seasonPoints:
            if driver in playoffDriversDict:
                continue
            elif len(playoffDriversDict) < 16:
                playoffDriversDict[driver] = driverDict[driver].getPlayoffPoints()
                #print(driver, 'was added by points ')
                #Calculate how many drivers are added to the playoffs by points
                driverDict[driver].setMadePlayoffs(True)
                driversAddedByPoints += 1

    
    
    for driver in playoffDriversDict:
        driverDict[driver].setMadePlayoffs(True)
        #Update every playoff drivers status.
        
    #print(driversAddedByWins, 'drivers added by wins, and ', driversAddedByPoints, 'drivers added by points ')
 

def calculateSeasonStats(drivers):
    '''This function takes in the driver dictionary, and calculates the season stats from it. Then calls createStats window with the top 5 drivers 
    from each statistical category as different dictionaries.'''
    #Create final dictionaries
    winners = {}
    seasonPoints = {}
    top5 = {}
    top10 = {}

    #Create various lists and dictionaries to sort the statistical leaders
    driverWinList = []
    middleWinDict = {}
    driverSeasonPointsList = []
    middlePointsDict = {}
    driverTop5List = []
    middleTop5Dict = {}
    driverTop10List = []
    middleTop10Dict = {}

    listOfFinalFour = []
    champion = []

    for driver in drivers:
        #For each driver, append to the proper list, the driver's points + stagepoints, amount of wins, amount of top5's and top 10's
        points = drivers[driver].getPointTotal()
        stagePoints = drivers[driver].getStagePoints()
        drivers[driver].setPointTotal(points + stagePoints)
        #print(driver, 'finished with', drivers[driver].getPointTotal(),'points')
        num = random.random()
        #Append driver wins
        driverWinList.append(drivers[driver].getWins() + num)
        middleWinDict[drivers[driver].getWins() + num] = driver

        #Appends point totals
        driverSeasonPointsList.append(drivers[driver].getPointTotal()+num)
        middlePointsDict[drivers[driver].getPointTotal() + num] = driver

        #Appends top 5's
        driverTop5List.append(drivers[driver].getTop5() + num)
        middleTop5Dict[drivers[driver].getTop5() + num] = driver

        #Appends top 10's
        driverTop10List.append(drivers[driver].getTop10() + num)
        middleTop10Dict[drivers[driver].getTop10() + num] = driver

        if drivers[driver].getMadeRoundOf4() == True:
            listOfFinalFour.append(driver)
            #If the driver made the final 4, add to the list
        if drivers[driver].getWonChampionship() == True:
            #If the driver won the championship, add the name to the champion
            champion = drivers[driver].getName()


    #Sort all of these lists.
    driverWinList.sort(reverse = True)
    driverSeasonPointsList.sort(reverse = True)
    driverTop5List.sort(reverse = True)
    driverTop10List.sort(reverse = True)
    
    #Take the top 5 drivers in each statistical category and make dictionaries with drivers and values for each category.

    #Take the top 5 winners
    a = 1
    for pos in driverWinList:
        if a <= 5:
            driver = middleWinDict[pos]
            wins = drivers[driver].getWins()
            winners[driver] = wins
            a += 1
    #Take the top 5 points leaders
    b = 1
    for pos in driverSeasonPointsList:
        if b <= 5:
            driver = middlePointsDict[pos]
            points = drivers[driver].getPointTotal()
            seasonPoints[driver] = points
            b += 1
    #Take the top 5 drivers with the most top 5's
    c = 1
    for pos in driverTop5List:
        if c <= 5:
            driver = middleTop5Dict[pos]
            topFive = drivers[driver].getTop5()
            top5[driver] = topFive
            c += 1
    #Take the top 10 drivers with the most top 10's
    d = 1
    for pos in driverTop10List:
        if d <= 5:
            driver = middleTop10Dict[pos]
            topTen = drivers[driver].getTop10()
            top10[driver] = topTen
            d += 1
            


    #print(winners)
    #Now that all of these dictionaries have been made, create a stats window that outputs all of this data.
    countdown(5)
    createStatsWindow(seasonPoints, winners, top5, top10, listOfFinalFour, champion)
    
        


def outputSeasonStats(dictOfDrivers):
    '''This function takes in the dictionary of drivers, and can output various seasonal statistics.'''
    dictOfAvgFinish = {}
    listOfAvgFinishes = []
    #Calculate the average finish of each driver
    for driver in dictOfDrivers:
        dictOfAvgFinish[dictOfDrivers[driver].getTotalFinish()/36] = driver
        listOfAvgFinishes.append(dictOfDrivers[driver].getTotalFinish()/36)
    #Sort the list of average finishes
    listOfAvgFinishes.sort(reverse = True)
    print(listOfAvgFinishes)

    #Output the avg finish of each driver in order
    for avgFinish in listOfAvgFinishes:
        currentDriver = dictOfAvgFinish[avgFinish]
        print(currentDriver, 'had an average finish of', round(avgFinish,1), 'with', dictOfDrivers[currentDriver].getWins(), 'wins',dictOfDrivers[currentDriver].getTop5(), 'top 5\'s and' , dictOfDrivers[currentDriver].getTop10(),'top 10\'s')
    #Output the amount of wins the top drivers have, and which tracks they have won at.
    for driver in dictOfDrivers:
        driverObject = dictOfDrivers[driver]
        if driverObject.getWins() >= 1:

            print(driver, 'won at', driverObject.getRacesWon())
        print(driver, 'had', driverObject.getStageWins(), 'stage wins, and', driverObject.getStagePoints(), 'stage points, had', driverObject.getWins(), 'wins, for a total of', driverObject.getPlayoffPoints(), 'playoff points and finished with', driverObject.getPointTotal(),'points')


def createStatsWindow(points, winners, top5, top10, finalFourList, champion):
    '''This function takes in dictionaries filled with the top 5 drivers for each statistically category, as well as the driver who won
    the championship. These values are then outputted to a window for easier viewing.'''

    #Create a window
    win = gr.GraphWin('Season Statistics', 1000, 500, False)
    
    #Create the title
    title = gr.Text( gr.Point(500, 50), "Nascar Season Stats")
    title.setSize(35)
    title.draw(win)

    #Create the title for Most wins
    winLeaders =  gr.Text( gr.Point(200, 130), "Most Wins")
    winLeaders.setSize(25)
    winLeaders.draw(win)

    winnersYValue = 160

    #Output text for each driver and the corresponding statistical category.
    for driver in winners:
        string = driver + ': ' + str(winners[driver])
        object = gr.Text(gr.Point(200, winnersYValue), string)
        object.setSize(20)
        object.draw(win)
        winnersYValue += 25

    #Create a title for Points leaders
    pointsLeaders =  gr.Text( gr.Point(400, 130), "Points Leaders")
    pointsLeaders.setSize(25)
    pointsLeaders.draw(win)

    pointsYValue = 160
    #Output text for each driver and the corresponding statistical category.
    for driver in points:
        string = driver + ': ' + str(points[driver])
        object = gr.Text(gr.Point(400, pointsYValue), string)
        object.setSize(20)
        object.draw(win)
        pointsYValue += 25

    #Create a title for top 5 leaders
    top5Leaders =  gr.Text( gr.Point(600, 130), "Top 5 Leaders")
    top5Leaders.setSize(25)
    top5Leaders.draw(win)

    top5YValue = 160
    #Output text for each driver and the corresponding statistical category.
    for driver in top5:
        string = driver + ': ' + str(top5[driver])
        object = gr.Text(gr.Point(600, top5YValue), string)
        object.setSize(20)
        object.draw(win)
        top5YValue += 25

    #Create a title for the top 10 leaders
    top10Leaders =  gr.Text( gr.Point(800, 130), "Top 10 Leaders")
    top10Leaders.setSize(25)
    top10Leaders.draw(win)

    top10YValue = 160
    #Output text for each driver and the corresponding statistical category.
    for driver in top10:
        string = driver + ': ' + str(top10[driver])
        object = gr.Text(gr.Point(800, top10YValue), string)
        object.setSize(20)
        object.draw(win)
        top10YValue += 25

    #Create a title for the final four
    finalFour = gr.Text(gr.Point(200, 320), "Final Four")
    finalFour.setSize(25)
    finalFour.draw(win)

    finalFourYValue = 350
    #Output text for the top 4 drivers left in the playoffs.
    for driver in finalFourList:
        object = gr.Text(gr.Point(200, finalFourYValue), driver)
        object.setSize(20)
        object.draw(win)
        finalFourYValue += 25

    #Create a title for the champion
    champ = gr.Text(gr.Point(600, 320), "Champion")
    champ.setSize(30)
    champ.draw(win)

    #Output the champion
    object = gr.Text(gr.Point(600, 380), champion)
    object.setSize(35)
    object.draw(win)

    win.getMouse()
    win.close()

def countdown(n):
    if n == 0:
        print("TADA")
    else:
        print(n)
        countdown(n-1)




def main():
    '''The main function does 3 things. Gets the driver dictionary from calling collectDriverData, gets the track dictionary
    fro calling collectTrackData, and then calls simulateSeason, passing in the driver and track dictionaries.'''
    #Create a driver dictionary
    drivers = collectDriverData()

    import json
    import sys

    sys.stdout = open("declare.js", "w")

    jsonObject = json.dumps(drivers)
    #Create a track dictionary
    tracks = collectTrackData()
    #Simulate the season, passing in the two dictionaries.
    simulateSeason(drivers, tracks)

if __name__ == "__main__":
    main()



