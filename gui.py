import functions
import FreeSimpleGUI as sg
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key = "todo" )
add_button = sg.Button("Add")
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica',20))

# 2 values to a tuple or list
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
        case "Edit":
            print("Edit will be soon")
window.close()




