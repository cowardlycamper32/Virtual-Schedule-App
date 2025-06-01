from classes import TaskList, ReadWriteTaskList as Saves

taskmanager = TaskList()
saves = Saves(taskmanager)
taskmanager.addTask("test", "This is a test", "Sun")
#print(taskmanager.tasks[0])
taskmanager.tasks[0].checkTask()
score = taskmanager.weekEndScore()
print(taskmanager.weekEndRanking(score))