import datetime as dt
from time import sleep as wait
from Exceptions import InvalidConfigPath, InvalidPathException
from os.path import exists, isdir

class Task:
    def __init__(self, name, description, endDay):
        self.name = name
        self.description = description
        match endDay.lower():
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
        self.checked = False
        self.score = 0




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
    def getCurrentDay(self):
        self.currentDay = dt.datetime.isoweekday(dt.datetime.today())
    def addTask(self, name, description, endDay):
        try:
            task = Task(name, description, endDay)
            self.tasks.append(task)
            return True
        except Exception:
            print("Failed to add task\nPlease use a valid day such as monday or mon")
            return False

class ReadWriteTaskList:
    def __init__(self, taskList: TaskList):
        self.taskList = taskList.tasks
        self.taskManager = taskList
        self.saveFile = self.OpenSaveFile()

    def OpenSaveFile(self, path="_help.sv"):
        if not self.SaveFileExist(path):
            open(path, "w+").close()
        saveFile = open(path, "a+")
        return saveFile



    def SaveFileExist(self, path="_help.sv"):
        if not exists(path):
            return False
        else:
            if isdir(path):
                print("Please enter a valid Path not a directory. Please send me a bug report")
                raise InvalidPathException
            else:
                return True

    def writeSaveFile(self):
        for task in self.taskList:
            self.saveFile.write(str(task.name) + "," + str(task.description) + "," + str(task.endDay) + "," + str(task.score) + "\n")
        self.saveFile.close()
        return True

    def readSaveFile(self, path="_help.sv"):
        try:
            file = open(path, "r")
            red = file.readlines()
            file.close()
        except IOError:
            raise InvalidPathException
        for i in range(len(red)):
            task = red[i].split(",")
            self.taskManager.addTask(task[0], task[1], task[2])
            print(self.taskManager.tasks)



tskmng = TaskList()
a = ReadWriteTaskList(tskmng)
a.readSaveFile()