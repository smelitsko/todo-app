from functions import get_todos, write_todos
import time
# import functions
# functions.function_name()
# python day time format
# python module index ej: csv

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is " , now)

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    # remove white spaces:
    user_action = user_action.strip()
    # match user_action:
    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)
    elif user_action.startswith("show"):
        todos = get_todos()
        # new_todos = [item.strip('\n') for item in todos]
        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            todos = get_todos()
            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter a new to do: ") + '\n'
            todos[number] = new_todo
            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith("complete"):
        try:
            todos = get_todos()
            number = int(user_action[9:])
            todo_to_remove = todos[number-1]
            todo_to_remove = todo_to_remove.strip('\n')
            print(f"Se elimino el item {todo_to_remove} de la lista")
            todos.pop(number-1)
            # write_todos(filepath="files/todos.txt", todos_arg=todos)
            write_todos(todos)
        except IndexError:
            print("Out of index")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Hey you entered an unknown command")
print("Bye!")