from classes import TaskList, ReadWriteTaskList as Saves, Task
import datetime as dt
from os import system
from os import name

if name == 'nt':
    clearcmd = 'cls'
else:
    clearcmd = 'clear'

script = False
configFilePath = "config.cfg"

scoreDay = 7


def mainMenu(tskmng: TaskList, saver: Saves):
    text = """==========SCHEDULE============
    1) Add a task
    2) Show all tasks
    3) Show overdue tasks
    4) Mark task as completed
    5) Exit"""
    print(text)
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid choice.")
        system(clearcmd)
        mainMenu(tskmng)

    match choice:
        case 1:
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")
            endDay = input("Enter end day: ")
            tskmng.addTask(task_name, task_description, endDay)
            return True
        case 2:
            tskmng.printAllTasks()
            return True
        case 3:
            for task in tskmng.tasks:
                if task.endDay <= dt.datetime.isoweekday(dt.datetime.today()) and not task.checked:
                    task.printTask()
            return True
        case 4:
            taskName = input("Enter task name: ")
            for task in tskmng.tasks:
                if task.taskName == taskName:
                    checkandscore(task)

        case 5:
            if dt.datetime.isoweekday(dt.datetime.today()) == scoreDay:
                print(f"Total Score: {tskmng.weekEndScore()}")

        case 6:
            system(clearcmd)
            print("SAVING AND QUITING")
            saver.writeSaveFile()
            return False
        case _:
            print("Invalid choice.")
            system(clearcmd)
            mainMenu(tskmng)


def main():
    taskManager = TaskList()
    saver = Saves(taskManager)
    saver.readSaveFile()
    running = True
    while running:
        running = mainMenu(taskManager, saver)


def checkandscore(task: Task):
    if task.checkTask():
        task.checkTask()
        task.addScore()
        return True
    return False




if __name__ == '__main__':
    script = True
    main()





