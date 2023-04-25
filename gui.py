import functions
import folder
import PySimpleGUI as sg
import time
import os

folder.folder_check()
folder.file_check()

icon_path = os.path.abspath(os.path.join(os.getcwd(), 'logo.ico'))

sg.theme("DarkPurple4")
sg.set_options(icon=icon_path)

clock = sg.Text('', key="clock")
label = sg.Text("Type in a Note", text_color="orange")

input_box = sg.InputText(tooltip="Enter a note", size=32, key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_notes(), key='todos_listbox',
                      enable_events=True, size=(30, 7))
edit_button = sg.Button("Edit", tooltip="Select a note")
remove_button = sg.Button("Remove")
exit_button = sg.Button("Exit", button_color=('orange', None))

buttons_col = sg.Column([[edit_button], [remove_button]], justification='center')
window = sg.Window("My Notes",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, buttons_col],
                           [exit_button]],
                   font=('Helvetica', 12, 'bold'),
                   icon=icon_path)


def refresh(input_key='todo', listbox_key='todos_listbox'):
    window[listbox_key].update(values=todos)
    window[input_key].update(value='')


while True:
    event, value = window.read(timeout=500)
    window["clock"].update(
        value=time.strftime("%Y-%b-%d, "
                            "%H:%M:%S"))

    todos = functions.get_notes()
    match event:
        case "Add":
            todo_to_add = value['todo'] + "\n"
            todos.append(todo_to_add)
            functions.write_notes(todos)
            refresh()

        case "Edit":
            if len(value['todos_listbox']) != 0:
                try:
                    todo_to_remove = value['todos_listbox'][0]
                    index = todos.index(todo_to_remove)
                    todo_to_add = value['todo'] + "\n"
                    todos[index] = todo_to_add
                    functions.write_notes(todos)
                    refresh()
                except IndexError:
                    sg.popup("Please select an item first", font=('Helvetica', 12, 'bold'), icon=icon_path)
                    continue
            else:
                sg.popup("Please enter a note before editing it", font=('Helvetica', 12, 'bold'), icon=icon_path)
                continue

        case "Remove":
            if len(value['todos_listbox']) != 0:
                try:
                    todo_to_remove = value['todos_listbox'][0]
                    index = todos.index(todo_to_remove)
                    todos.pop(index)
                    functions.write_notes(todos)
                    refresh()
                except IndexError:
                    sg.popup("Please select an item first", font=('Helvetica', 12, 'bold'), icon=icon_path)
                    continue
            else:
                sg.popup("The list is empty!", font=('Helvetica', 12, 'bold'), icon=icon_path)
                continue

        case sg.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()
