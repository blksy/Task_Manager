from functions import load_todos, write_todos

while True:
    user_action = input(
        "Choose one of the following options: add, show, edit, complete or exit: "
    ).strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()

        if not todo:
            print("Todo cannot be empty.")
            continue

        todos = load_todos()

        todos.append(todo)

        write_todos(todos)

        print("Todo added successfully.")

    elif user_action == "show":

        todos = load_todos()

        if not todos:
            print("No todos found.")
            continue

        for index, todo in enumerate(todos, start=1):
            print(f"{index}. {todo}")

    elif user_action.startswith("edit"):

        try:
            todo_index = int(user_action[5:]) - 1

            todos = load_todos()

            new_todo = input("Enter new todo: ").strip()

            if not new_todo:
                print("Todo cannot be empty.")
                continue

            todos[todo_index] = new_todo

            write_todos(todos)

            print("Todo updated successfully.")

        except ValueError:
            print("Please enter a valid number.")

        except IndexError:
            print("There is no todo with that number.")

    elif user_action.startswith("complete"):

        try:
            todo_index = int(user_action[9:]) - 1

            todos = load_todos()

            removed_todo = todos.pop(todo_index)

            write_todos(todos)

            print(f'"{removed_todo}" was removed.')

        except ValueError:
            print("Please enter a valid number.")

        except IndexError:
            print("There is no todo with that number.")

    elif user_action == "exit":

        break

    else:
        print("Unknown command.")

print("Program exited successfully.")