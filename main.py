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
    5) Score and Rank (only works on Sundays)
    6) Exit"""
    print(text)
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid choice.")
        system(clearcmd)
        mainMenu(tskmng, saver)

    match choice:
        case 1:
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")
            endDay = input("Enter end day: ")
            tskmng.addTask(task_name, task_description, endDay)
        case 2:
            tskmng.printAllTasks()
        case 3:
            for task in tskmng.tasks:
                if task.endDay < dt.datetime.isoweekday(dt.datetime.today()) and not task.checked:
                    task.printTask()
                input("Press enter to continue...")
        case 4:
            taskName = input("Enter task name: ")
            for task in tskmng.tasks:
                if task.name == taskName:
                    checkandscore(task)
                else:
                    print("TASK NOT FOUND")
            input("Press enter to continue...")

        case 5:
            if dt.datetime.isoweekday(dt.datetime.today()) == scoreDay:
                system(clearcmd)
                print(tskmng.weekEndRanking(tskmng.weekEndScore()))
                input("Press enter to continue...")
            else:
                print("You can only get a ranking on the score day, currently Sunday.")
            input("Press enter to continue...")

        case 6:
            system(clearcmd)
            print("SAVING AND QUITING")
            saver.writeSaveFile()
            quit()
        case _:
            print("Invalid choice.")
            system(clearcmd)
            mainMenu(tskmng)

    system(clearcmd)
    mainMenu(tskmng, saver)

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





