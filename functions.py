FILEPATH = "todos.txt"
FILECPATH= "complete.txt"

def get_todos(filename=FILEPATH):
    with open(filename, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg,filename=FILEPATH):
    with open(filename, "w") as file:
        file.writelines(todos_arg)


def complete_todos(todos_arg,filename=FILECPATH):
    with open(filename, "w") as file:
        file.writelines(todos_arg)


def get_complete_todos(filename=FILECPATH):
    with open(filename, "r") as file:
        todos_local = file.readlines()
    return todos_local