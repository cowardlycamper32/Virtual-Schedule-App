import datetime as dt
from time import sleep as wait
from Exceptions import InvalidConfigPath, InvalidPathException, InvalidTaskException, InvalidScoreException
from os.path import exists, isdir
from os import name, system
import ranks

baseScore = 50
baseMult = 1.5

class Task:
    def __init__(self, name, description, endDay, checked=False, score=0):
        self.name = name
        self.description = description
        self.currentDay = dt.datetime.isoweekday(dt.datetime.today())
        if type(endDay) == str:
            endDay = endDay.lower()
        match endDay:
            case "monday":
                self.endDay = 1
            case "tuesday":
                self.endDay = 2
            case "wednesday":
                self.endDay = 3
            case "thursday":
                self.endDay = 4
            case "friday":
                self.endDay = 5
            case "saturday":
                self.endDay = 6
            case "sunday":
                self.endDay = 7
            case "mon":
                self.endDay = 1
            case "tue":
                self.endDay = 2
            case "wed":
                self.endDay = 3
            case "thu":
                self.endDay = 4
            case "fri":
                self.endDay = 5
            case "sat":
                self.endDay = 6
            case "sun":
                self.endDay = 7
            case 1:
                self.endDay = 1
            case 2:
                self.endDay = 2
            case 3:
                self.endDay = 3
            case 4:
                self.endDay = 4
            case 5:
                self.endDay = 5
            case 6:
                self.endDay = 6
            case 7:
                self.endDay = 7
            case _:
                raise Exception
        self.checked = checked
        self.score = score
    def printTask(self):
        if self.checked:
            symbol = "✓"
        else:
            symbol = "x"
        print(self.name + " - " + str(self.endDay) + "     " + symbol, "\n", self.description)
        input("Press enter to continue...")
        if name == "nt":
            clearcmd = "cls"
        else:
            clearcmd = "clear"
        system(clearcmd)
    def checkTask(self):

        if self.checked:
            return False
        self.checked = True

    def addScore(self):
        self.currentDay = dt.datetime.isoweekday(dt.datetime.today())

        if self.currentDay > self.endDay:
            difference = self.currentDay - self.endDay
        else:
            difference = self.endDay - self.currentDay
        self.score = baseScore * baseMult * (7 - difference)
        #print(self.score)



class Config:
    def __init__(self, configPath="config.cfg"):
        self.configFilePath = configPath

    def doesConfigFileExist(self):
        if not exists(self.configFilePath):
            return False
        else:
            if isdir(self.configFilePath):
                raise InvalidConfigPath
            return True

    def createConfigFile(self):
        try:
            open(self.configFilePath, "a+").close()
            return True
        except IOError:
            raise InvalidConfigPath


    def readConfigFile(self):
        try:
            file = open(self.configFilePath, "r")
            red = file.read()
            file.close()
            return red
        except IOError:
            raise InvalidConfigPath



class TaskList:
    def __init__(self):
        self.tasks = []
        self.currentDay = dt.datetime.isoweekday(dt.datetime.today())
        self.totalScore = 0
    def getCurrentDay(self):
        self.currentDay = dt.datetime.isoweekday(dt.datetime.today())
    def addTask(self, name, description, endDay, checked=False, score=0):
        #print(name, description, endDay)
        try:
            task = Task(name, description, endDay, checked, score)
            self.tasks.append(task)
            return True
        except Exception:
            print("Failed to add task\nPlease use a valid day such as monday or mon")
            return False
    def printAllTasks(self):
        if name == "nt":
            clearcmd = 'cls'
        else:
            clearcmd = 'clear'
        for task in self.tasks:
            system(clearcmd)
            task.printTask()
        input("Press enter to continue...")
        system(clearcmd)


    def weekEndScore(self):
        for task in self.tasks:
            if task.checked == False:
                task.score = 0
            else:
                task.addScore()
            self.totalScore += task.score

        return self.totalScore


    def weekEndRanking(self, score: int):
        numberoftasks = len(self.tasks)
        if numberoftasks == 0:
            return False
        else:
            maxscore = numberoftasks * baseScore * 7 * baseMult
            twenty = maxscore * 0.2
            fourty = maxscore * 0.4
            sixty = maxscore * 0.6
            eighty = maxscore * 0.8

        orgFile = open("history.dat", "r+")
        orgHist = orgFile.readlines()
        orgFile.close()

        newFile = open("history.dat", "w")
        newFile.write(orgHist[-1] + "\n")

        if score < twenty:
            newFile.write("D")
            newFile.close()
            return ranks.D
        elif score >= twenty and score < fourty:
            newFile.write("C")
            newFile.close()
            return ranks.C
        elif score >= fourty and score < sixty:
            newFile.write("B")
            newFile.close()
            return ranks.B
        elif score >= sixty and score < eighty:
            newFile.write("A")
            newFile.close()
            return ranks.A
        elif score >= eighty and score < maxscore:
            newFile.write("S")
            newFile.close()
            return ranks.S
        elif score == maxscore:
            newFile.write("P")
            newFile.close()
            return ranks.P
        else:
            raise InvalidScoreException("HOW TF DID YOU GET HERE?????")




class ReadWriteTaskList:
    def __init__(self, taskList: TaskList):
        self.taskList = taskList.tasks
        self.taskManager = taskList
        self.saveFile = self.OpenSaveFile()

    def OpenSaveFile(self, path="save.sv", type="r"):
        if not self.SaveFileExist(path):
            open(path, "w+").close()
        saveFile = open(path, type)
        return saveFile



    def SaveFileExist(self, path="save.sv"):
        if not exists(path):
            return False
        else:
            if isdir(path):
                print("Please enter a valid Path not a directory. Please send me a bug report")
                raise InvalidPathException
            else:
                return True

    def writeSaveFile(self):
        self.saveFile.close()
        self.saveFile = self.OpenSaveFile(type="w+")
        for task in self.taskList:
            self.saveFile.write(str(task.name) + "," + str(task.description) + "," + str(task.endDay) + "," + str(task.score) + "," + str(task.checked) + "\n")
        self.saveFile.close()
        return True

    def readSaveFile(self, path="save.sv"):
        try:
            file = open(path, "r")
            red = file.readlines()
            file.close()
            #print(red)
        except IOError:
            raise InvalidPathException
        for i in range(len(red)):
            task = red[i].split(",")
            for i in range(len(task)):
                task[i] = task[i].strip()
                task[i] = task[i].strip("\n")
            #print(task)
            if task[3] == "False":
                task[3] = False
            else:
                task[3] = True
            self.taskManager.addTask(task[0], task[1], int(task[2]), task[4], int(task[3]))
            #print(self.taskManager.tasks)
