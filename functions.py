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
        
def add_todo(todo, filepath = "todos.txt"):
    """Add a new todo to the list and save it to the file."""
    todos = load_todos(filepath)
    todos.append(todo)
    write_todos(todos, filepath)
    
def show_todos(filepath = "todos.txt"):
    """Display all todos."""
    return load_todos(filepath)

def edit_todo(index, new_todo, filepath = "todos.txt"):
    """Edit an existing todo at the specified index."""
    todos = load_todos(filepath)
    if 0 <= index < len(todos):
        todos[index] = new_todo
        write_todos(todos, filepath)
    else:
        raise IndexError("Todo index out of range.")
      
def complete_todo(index, filepath = "todos.txt"):
    """Remove a todo at the specified index."""
    todos = load_todos(filepath)
    if 0 <= index < len(todos):
        removed_todo = todos.pop(index)
        write_todos(todos, filepath)
        return removed_todo
    else:
        raise IndexError("Todo index out of range.")
        
if __name__ == "__main__":
    todos = load_todos()
    print(todos)
