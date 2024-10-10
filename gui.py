import functions
import time
import FreeSimpleGUI as Sg
now = time.strftime("%b %d, %Y %H:%M:%S")
# Elementos (10)
time_label = Sg.Text(now)
input_box_label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter to-do", key="todo" )
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(), key="selected_todo",
                      enable_events=True, size=(45,10))
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit")

window = Sg.Window('My To-Do App',
                   layout=[[time_label] ,
                           [input_box_label],
                           [input_box, add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]
                           ],
                   font=('Helvetica', 20))

# 2 values to a tuple or list
while True:
    event, values = window.read()
    match event:
        case "selected_todo":
            window['todo'].update(value=values['selected_todo'][0])
        case "Add":
            print(event)
            print(values)
            todos = functions.get_todos()
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)
            window['selected_todo'].update(values=todos)
        case "Edit":
            todo_to_edit = values['selected_todo']
            new_to_do = values['todo'] + '\n'
            todos = functions.get_todos()
            index = todos.index(todo_to_edit[0])
            todos[index] = new_to_do
            functions.write_todos(todos)
            window['selected_todo'].update(values=todos)
        case "Complete":
            todo_to_complete = values['selected_todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_complete[0])
            todos.pop(index)
            functions.write_todos(todos)
            window['selected_todo'].update(values=todos)
        case "Exit":
            print("Bye")
            break
        case Sg.WIN_CLOSED:
            print("Bye")
            break
window.close()




