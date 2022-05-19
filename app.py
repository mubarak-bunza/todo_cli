from model import *
import json
import os

path=os.getcwd()
FileDB = fr"{path}/todo.json"

def init_db():
    try:
        with open(FileDB, "r") as f:
            obj = json.load(f)
    except Exception as e:
        with open(FileDB, "w") as f:
            json.dump([], f, indent=2)

class Todos():
    """
    # Todo App Blueprint
    """
    def __init__(self):
        init_db()
        self.FileDB = FileDB
    
    def read_from_file(self):
        with open(self.FileDB, "r") as f:
            self.obj = json.load(f)
        return self.obj

    def write_to_file(self, obj):
        with open(self.FileDB, "w") as f:
            json.dump(self.obj, f, indent=2)

    def add(self, task):
        print("added -> ", task)
        
        self.obj = self.read_from_file()

        self.obj.append({"todo": task, "status": False })

        self.write_to_file(self.obj)    
    
    def list(self):
        self.obj = self.read_from_file()
        if len(self.obj) < 1:
            print("You have no task")
        else:
            for i, todo in enumerate(self.obj):
                if self.obj[i]["status"] == True:
                    print(f"({str(i+1)}*)" + " " + self.obj[i]["todo"])
                else:
                    print(f"({str(i+1)})" + " " + self.obj[i]["todo"])

    
    def complete(self, task):
        self.obj = self.read_from_file()
        try:
            self.obj[task-1]["status"] = True
            
            self.write_to_file(self.obj)
        except Exception as e:
            print(f"task {task} does not exist")

    def delete(self, task):
        self.obj = self.read_from_file()
        try:
            todo = self.obj.pop(task - 1)

            print(f"task \"{todo['todo']}\" deleted")

            self.write_to_file(self.obj)
        
        except Exception as e:
          print(f"todo {task} does not exist")


