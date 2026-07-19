from functions import add_todo, show_todos, load_todos, write_todos, complete_todo
import FreeSimpleGUI as sg

label = sg.Text("Type in a todo:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", tooltip="Add todo")
list_box = sg.Listbox(values=show_todos(),key="todos", enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit", tooltip="Edit todo")

window = sg.Window('My Todo List', 
                   layout=[[label], [input_box, add_button], 
                   [list_box, edit_button]], 
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = load_todos()
            new_todo = values["todo"] 
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = load_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            write_todos(todos)
            window["todos"].update(values=todos)
        case 'todos':
            window["todo"].update(value=values["todos"][0])
        case sg.WINDOW_CLOSED:
            break