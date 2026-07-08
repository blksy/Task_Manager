def load_todos(filepath = "todos.txt"):
    """Load todos from a file and return them as a list."""
    try:
        with open(filepath, "r") as file:
            todos = file.readlines()
            todos = [todo.strip() for todo in todos]
            return todos
    except FileNotFoundError:
        return []
      
def write_todos(todos_arg, filepath = "todos.txt"):
    """Write todos to a file."""
    with open(filepath, "w") as file:
        file.writelines(f"{todo}\n" for todo in todos_arg)
        
        
if __name__ == "__main__":
    todos = load_todos()
    print(todos)
