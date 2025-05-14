from classes import TaskList, ReadWriteTaskList as Saves
import datetime as dt

script = False
configFilePath = "config.cfg"
def main():
    taskManager = TaskList()
    saver = Saves(taskManager)
    #taskManager.addTask("a", "b", "mon")
    #saver.writeSaveFile()
    saver.readSaveFile()



if __name__ == '__main__':
    script = True
    main()





