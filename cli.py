from functions import add_todo, show_todos, edit_todo, complete_todo
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")

while True:
    user_action = input(
        "Choose one of the following options: add, show, edit, complete or exit: "
    ).strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()

        if not todo:
            print("Todo cannot be empty.")
            continue

        add_todo(todo)
        print("Todo added successfully.")

    elif user_action == "show":

        todos = show_todos()

        if not todos:
            print("No todos found.")
            continue

        for index, todo in enumerate(todos, start=1):
            print(f"{index}. {todo}")

    elif user_action.startswith("edit"):

        try:
            todo_index = int(user_action[5:]) - 1

            new_todo = input("Enter new todo: ").strip()

            if not new_todo:
                print("Todo cannot be empty.")
                continue

            edit_todo(todo_index, new_todo)

            print("Todo updated successfully.")

        except ValueError:
            print("Please enter a valid number.")

        except IndexError:
            print("There is no todo with that number.")

    elif user_action.startswith("complete"):

        try:
            todo_index = int(user_action[9:]) - 1

            removed_todo = complete_todo(todo_index)

            print(f'"{removed_todo}" was removed from the list.')

        except ValueError:
            print("Please enter a valid number.")

        except IndexError:
            print("There is no todo with that number.")

    elif user_action == "exit":

        break

    else:
        print("Unknown command.")

print("Program exited successfully.")