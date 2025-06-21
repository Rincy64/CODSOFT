import json
import os

TODO_FILE = 'todo_data.json'

def load_tasks():
  if os.path.exists(TODO_FILE):
    with open(TODO_FILE,'r') as file:
      return json.load(file)
      return []
      
def save_tasks(tasks):
  with open(TODO_FILE,'w') as file:
    json.dump(taks, file, indent=4)
    
def display_tasks(tasks):
  if not tasks:
    print("\n No tasks found.\n")
    return
    print("\n To-Do List:")
    for index, task in enumerate(tasks, 1):
      status ="$" if task["done"]else "*"
      print(f"{index}.[{status}]{task['title']}")

def add_task(task):
  title = input("Enter task title")
  tasks.append({"title":title,"done":False})
  save_tasks(tasks)
  print("Tasks added successfully ")

def mark_done(tasks):
  display_tasks(tasks)
  task_id = int(input("enter task number to mark as done :")) - 1
  if 0<=task_id <len(tasks):
    tasks[tasks_id]["done"]= True
    save_tasks(tasks)
    print("Task marked as done")
  else:
    print("Invalid task number ")

def delete_task(tasks):
  display_tasks(tasks)
  task_id=int(input("Enter task number to delete:")) -1
  if 0<=task_id <len(tasks):
    tasks.pop(tasks_id)
    save_tasks(tasks)
    print("Task deleted successfully")
  else:
    print("Invalid task number")

def main():
  tasks = load_tasks()
  while True:
    print("\n -----TO-DO LIST MENU ----")
    print("1.view task")
    print("2.add task")
    print("3.mark task as done")
    print("4.delete task")
    print("5.exit")
    choice = input("Choose an option (1-5): ")
    if choice =='1':
      display_tasks(task)
    elif choice=='2':
      add_task(tasks)
    elif choice=='3':
      mark_task_done(tasks)
    elif choice=='4':
      delete_task(tasks)
    elif choice=='5':
      print("Exiting......Goodbye!")
      break
    else:
      print("Invalud choice.Please try again.")

if __name__=="__main__":
  main()
      
      
