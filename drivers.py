'''
Mike Ciaccio
11/12/2021
CS152
Section A

This file contains the code for two classes, a Driver class and a Track class. These classes are meant to store the data from the spreadsheets
in one place. In addition, the Driver class contains many variables that are needed for the season simulation.

This file has no output, but can be ran by python3 drivers.py

'''
#Class driver is meant to hold various values for each driver, and the variable will be updated in response to the simulation.
class Driver():
    def __init__(self, name, number, teamName, age, eqRating, shortTrackTop10, shortTrackTop5, shortTrackWins, intermediateTop10, intermediateTop5, intermediateWins, roadCourseTop10, roadCourseTop5, roadCourseWins, superSpeedwayTop10, superSpeedwayTop5, superSpeedwayWins, numChamp):
        '''This Driver class initializer takes in values from the spreadsheet. It takes in name, number, 
        teamName, age, eqRating, shortTrackTop10,5,Wins, intermediateTop10,5,Wins, roadCourseTop10,5,Wins,
        superSpeedwayTop10,5,Wins, and the number of championships each driver has won. These values are then
        assigned into the proper object variables. Additionally, values for the various ratings for each track are initialized to 0,
        statistical categories are initalized to zero and false, to be updated throughout the simulation. Lastly,
        methods are called to calculate the various driver ratings based on the inputted data.  '''
        #Assign inputted variables to the proper object variables
        self.name = name
        self.number = number
        self.age = age
        self.teamName = teamName
        self.eqRating = float(eqRating)

        self.shortTrackTop10 = float(shortTrackTop10)
        self.shortTrackTop5 = float(shortTrackTop5)
        self.shortTrackWins = float(shortTrackWins)

        self.intermediateTop10 = float(intermediateTop10)
        self.intermediateTop5 = float(intermediateTop5)
        self.intermediateWins = float(intermediateWins)

        self.roadCourseTop10 = float(roadCourseTop10)
        self.roadCourseTop5 = float(roadCourseTop5)
        self.roadCourseWins = float(roadCourseWins)

        self.superSpeedwayTop10 = float(superSpeedwayTop10)
        self.superSpeedwayTop5 = float(superSpeedwayTop5)
        self.superSpeedwayWins = float(superSpeedwayWins)

        #Set various statistical categories to zero or false, to be changed by the simulation
        self.shortTrackRating = 0.0
        self.intermediateTrackRating = 0.0
        self.roadCourseRating = 0.0
        self.superSpeedwayRating = 0.0

        self.numChamp = int(numChamp)

        self.pointTotal = 0
        self.top5 = 0
        self.top10 = 0
        self.wins = 0
        self.totalFinish = 0
        self.stagePoints = 0
        self.stageWins = 0
        self.playoffPoints = 0
        self.racesWon = []

        self.madePlayoffs = False
        self.madeRoundOf12 = False
        self.madeRoundOf8 = False
        self.madeRoundOf4 = False
        self.wonChampionship = False

        self.playoffRoundOf16Points = 0
        self.playoffRoundOf12Points = 0
        self.playoffRoundof8Points = 0
        self.playoffRoundOf4Points = 0


        #Call methods to compute the various ratings for each track based on the object variables.
        self.computeShortTrackRating()
        self.computeIntermediateTrackRating()
        self.computeRoadCourseRating()
        self.computeSuperSpeedwayRating()

    def __str__(self):
        '''Returns a string with name, number, team name, age, and various ratings for each type of track.'''
        return self.name + ' drives the number ' + self.number + ' for '+ self.teamName + '. \nHe is ' + self.age + ' years old. \nHis short track rating is: '+ str(self.shortTrackRating) + '\nHis intermediate track rating is: '+ str(self.intermediateTrackRating) + '\nHis road course rating is: '+ str(self.roadCourseRating) + '\nHis superspeedway rating is: '+ str(self.superSpeedwayRating) + '\n'
        

    def getName(self):
        '''Returns the name of the driver object'''
        return self.name

    def getNumber(self):
        '''Returns the number of the driver object.'''
        return self.number

    def getAge(self):
        '''Returns the age of the driver object.'''
        return self.age

    def getTeamName(self):
        '''Returns the team name of the driver object'''
        return self.teamName

    def getEqRating(self):
        '''Returns the equipment rating of the driver object.'''
        return self.eqRating

    def getShortTrackRating(self):
        '''Returns the short track rating of the driver.'''
        return self.shortTrackRating

    def setShortTrackRating(self, rating):
        '''Takes in a rating, and sets the driver's short track rating to that rating. Returns nothing.'''
        self.shortTrackRating = rating

    def getIntermediateTrackRating(self):
        '''Returns the intermediate track rating of the driver.'''
        return self.intermediateTrackRating

    def setIntermediateTrackRating(self, rating):
        '''Takes in a ratings, and sets the driver's intermediate track rating to that rating. Returns nothing.'''
        self.intermediateTrackRating = rating

    def getRoadCourseRating(self):
        '''Returns the road course rating of the driver.'''
        return self.roadCourseRating
    
    def setRoadCourseRating(self, rating):
        '''Takes in a rating, and sets the driver's road course rating to that rating. Returns nothing.'''
        self.roadCourseRating = rating

    def getSuperSpeedwayRating(self):
        '''Returns the superSpeedway rating of the driver'''
        return self.superSpeedwayRating

    def setSuperSpeedwayRaing(self, rating):
        '''Takes in a rating, and sets the driver's superSpeedway rating to that rating. Returns nothing.'''
        self.superSpeedwayRating = rating

    def getNumChamp(self):
        '''Returns the number of championships the driver has won.'''
        return self.numChamp

    def getPointTotal(self):
        '''Returns the season points total for the driver.'''
        return self.pointTotal

    def setPointTotal(self, amount):
        '''Takes in an amount, and sets the point total of the driver to that value. Returns nothing.'''
        self.pointTotal = amount

    def getTop5(self):
        '''Returns the amount of top 5's a driver has.'''
        return self.top5

    def addTop5(self):
        '''This method adds one to the amount of top 5's that the driver has. Returns nothing'''
        self.top5 += 1

    def getTop10(self):
        '''Returns the amount of top 10's a driver has.'''
        return self.top10

    def addTop10(self):
        '''This method adds one to the amount of top 10's that the driver has. Returns nothing'''
        self.top10 += 1

    def getWins(self):
        '''Returns the amount of wins the driver has.'''
        return self.wins

    def addWin(self):
        '''This method adds one to the amount of wins that the driver has. Returns nothing'''
        self.wins += 1

    def getTotalFinish(self):
        '''Returns the total finishing position of the driver.'''
        return self.totalFinish

    def addTotalFinish(self, amount ):
        '''Takes in an amount, and adds that amount to the total finishing position of the driver. Returns nothing.'''
        self.totalFinish += amount

    def addRaceWon(self, race):
        '''Takes in a string race, and adds this race to the list of races won for each driver. Returns nothing.'''
        self.racesWon.append(race)

    def getRacesWon(self):
        '''Returns a list of the races won by the driver.'''
        return self.racesWon

    def setMadePlayoffs(self, boolean):
        '''Takes in a boolean value, and assigns this value to the madePlayoffs value for the driver. Returns nothing.'''
        self.madePlayoffs = boolean
    
    def getMadePlayoffs(self):
        '''Retuns a boolean corresponding to whether or not this driver has made the playoffs.'''
        return self.madePlayoffs

    def setMadeRoundOf12(self, boolean):
        '''Takes in a boolean value, and assigns this value to the madeRoundOf12 value for the driver. Returns nothing.'''
        self.madeRoundOf12 = boolean

    def getMadeRoundOf12(self):
        '''Returns a boolean corresponding to whether or not this driver has made the round of 12.'''
        return self.madeRoundOf12

    def setMadeRoundOf8(self, boolean):
        '''Takes in a boolean value, and assigns this value to the madeRoundOf8 value for the driver. Returns nothing.'''
        self.madeRoundOf8 = boolean
    
    def getMadeRoundOf8(self):
        '''Returns a boolean corresponding to whether or not this driver has made the round of 8'''
        return self.madeRoundOf8
    
    def setMadeRoundOf4(self, boolean):
        '''Takes in a boolean value, and assigns this value to the madeRoundOf4 value for the driver. Returns nothing.'''
        self.madeRoundOf4 = boolean

    def getMadeRoundOf4(self):
        '''Returns a boolean corresponding to whether or not this driver has made the round of 4.'''
        return self.madeRoundOf4

    def getWonChampionship(self):
        '''Returns a boolean value corresponding to whether or not this driver has won the championship.'''
        return self.wonChampionship
    
    def setWonChampionship(self, boolean):
        '''Takes in a boolean value, and assigns this value to the wonChampionship value for the driver. Returns nothing.'''
        self.wonChampionship = boolean

    def getStagePoints(self):
        '''Returns the amount of stage points the driver has accumulated.'''
        return self.stagePoints

    def addStagePoints(self, amount):
        '''Takes in an amount, and adds this amount to the total stage points value for the driver. Returns nothing.'''
        self.stagePoints += amount

    def getStageWins(self):
        '''Returns the amount of stage wins the driver has accumulated.'''
        return self.stageWins

    def addStageWin(self, amount):
        '''Takes in an amount, and adds one to the amount of stage wins value for the driver. Returns nothing.'''
        self.stageWins += amount

    def getPlayoffPoints(self):
        '''Returns the amount of playoff points the driver has accumulated.'''
        return self.playoffPoints

    def addPlayoffPoints(self, amount):
        '''Takes in an amount, and adds this amount to the amount of playoff points this driver has. Returns nothing.'''
        self.playoffPoints += amount
    
    def getRoundOf16Points(self):
        '''Returns the amount of roundOf16Points the driver has earned.'''
        return self.playoffRoundOf16Points

    def addRoundOf16Points(self, amount):
        '''Takes in an amount and adds this amount to the amount of roundOf16Points the driver has. Returns nothing.'''
        self.playoffRoundOf16Points += amount

    def getRoundOf12Points(self):
        '''Returns the amount of roundOf12Points the driver has earned.'''
        return self.playoffRoundOf12Points

    def addRoundOf12Points(self, amount):
        '''Takes in an amount and adds this amount to the amount of roundOf12Points the driver has. Returns nothing.'''
        self.playoffRoundOf12Points += amount

    def getRoundOf8Points(self):
        '''Returns the amount of roundOf8Points the driver has earned.'''
        return self.playoffRoundof8Points

    def addRoundOf8Points(self, amount):
        '''Takes in an amount and adds this amount to the amount of roundOf8Points the driver has. Returns nothing.'''
        self.playoffRoundof8Points += amount

    def getRoundOf4Points(self):
        '''Returns the amount of roundOf4Points the driver has earned.'''
        return self.playoffRoundOf4Points
    
    def addRoundOf4Points(self, amount):
        '''Takes in an amount and adds this amount to the amount of roundOf4Points the driver has. Returns nothing.'''
        self.playoffRoundOf4Points += amount
    def setRoundOf4Points(self, amount):
        '''Tales in an amount and sets the amount to the value of playoff round of 4 points. Returns nothing.'''
        self.playoffRoundOf4Points = amount




    def computeShortTrackRating(self):
        '''This method is meant to calculate the value for shortTrackRating. It does this by assigning a total based on the 
        amount of top10's, top5's, wins, and equipment rating. It then assigns this total to the proper object variable. Returns nothing'''
        #Give value to the amount of good finishes a driver has at this type of track, and create a rating based on this and the driver's equipment rating.
        top10 = self.shortTrackTop10 * .2
        top5 = self.shortTrackTop5 * .4
        win = self.shortTrackWins * 0.8
        equipment = self.eqRating 
        total = top10 + top5 + win + equipment
        #print(self.name, '\'s short track rating is: ', total)
        self.shortTrackRating = total

    def computeIntermediateTrackRating(self):
        '''This method is meant to calculate the value for intermediateTrackRating. It does this by assigning a total based on the 
        amount of top10's, top5's, wins, and equipment rating. It then assigns this total to the proper object variable. Returns nothing'''
        #Give value to the amount of good finishes a driver has at this type of track, and create a rating based on this and the driver's equipment rating.
        top10 = self.intermediateTop10 * .2
        top5 = self.intermediateTop5 * .4
        win = self.intermediateWins * 0.8
        equipment = self.eqRating 
        total = top10 + top5 + win + equipment
        #print(self.name, '\'s intermediate rating is: ', total)
        self.intermediateTrackRating = total

    def computeRoadCourseRating(self):
        '''This method is meant to calculate the value for roadCourseRating. It does this by assigning a total based on the 
        amount of top10's, top5's, wins, and equipment rating. It then assigns this total to the proper object variable. Returns nothing'''
        #Give value to the amount of good finishes a driver has at this type of track, and create a rating based on this and the driver's equipment rating.
        top10 = self.roadCourseTop10 * .2
        top5 = self.roadCourseTop5 * .4
        win = self.roadCourseWins * 0.8
        equipment = self.eqRating 
        total = top10 + top5 + win + equipment
        #print(self.name, '\'s intermediate rating is: ', total)
        self.roadCourseRating = total

    def computeSuperSpeedwayRating(self):
        '''This method is meant to calculate the value for superSpeedwayRating. It does this by assigning a total based on the 
        amount of top10's, top5's, wins, and equipment rating. It then assigns this total to the proper object variable. Returns nothing.'''
        #Give value to the amount of good finishes a driver has at this type of track, and create a rating based on this and the driver's equipment rating.
        top10 = self.superSpeedwayTop10 * .2
        top5 = self.superSpeedwayTop5 * .4
        win = self.superSpeedwayWins * 0.8
        equipment = self.eqRating 
        total = top10 + top5 + win + equipment
        self.superSpeedwayRating = total

class Track():
    def __init__(self, name, type, length, raceName, date, laps, raceNumber):
        '''This Track object initializer takes in a name, type of track, track length, race name, date, number of laps, and race number.
        It then assigns these values to the proper object variables. It also creates a string called str, based on various variables.'''
        self.name = name
        self.type = type
        self.length = length
        self.raceName = raceName
        self.laps = laps
        self.date = date
        self.raceNumber = str(raceNumber)
        self.str = 'Race #'+ self.raceNumber + ' is the '+ self.raceName + ' at '+ self.name+ '.\n This track is a '+ self.length + ' mile ' + self.type + '. '  + '\n'

        self.winner = ''

    def __str__(self):
        '''Returns a string detailing the race number, race name, name, length and type.'''
        return 'Race #'+ self.raceNumber + ' is the '+ self.raceName + ' at '+ self.name+ '.\n This track is a '+ self.length + ' mile ' + self.type + '. '  + '\n'

    def getStr(self):
        '''Returns the str value for the track'''
        return self.str

    def getName(self):
        '''Returns the name of the track'''
        return self.name

    def getType(self):
        '''Returns the type of the track'''
        return self.type

    def getLength(self):
        '''Retuns the length of the track.'''
        return self.length

    def getRaceName(self):
        '''Returns the race name of the track'''
        return self.raceName

    def getDate(self):
        '''Returns the date on which the track took place.'''
        return self.date

    def getLaps(self):
        '''Returns the amount of laps that is for each track'''
        return self.laps

    def setWinner(self, name):
        '''Takes in a driver name and assigns this name to the track variable winner. Returns nothing.'''
        self.winner = name

    def getWinner(self):
        '''Returns a string with the driver that won for each track.'''
        return self.winner  

    def getRaceNumber(self):
        '''Returns the race number of the track.'''
        return self.raceNumber     



    


