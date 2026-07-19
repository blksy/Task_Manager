from functions import add_todo, show_todos, edit_todo, complete_todo
import FreeSimpleGUI as sg

label = sg.Text("Type in a todo:")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add", tooltip="Add todo")

window = sg.Window('My Todo List', layout=[[label], [input_box], [add_button]])
window.read()
window.close() 

