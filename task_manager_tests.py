from functions import load_todos, write_todos

def test_load_todos_returns_empty_list_when_file_does_not_exist(tmp_path):
    filepath = tmp_path / "missing.txt"

    result = load_todos(filepath)

    assert result == []


def test_write_todos_creates_file_with_correct_content(tmp_path):
    filepath = tmp_path / "todos.txt"
    todos = ["Buy milk", "Walk the dog", "Learn Python"]

    write_todos(todos, filepath)

    with open(filepath, "r") as file:
        result = file.read()

    assert result == "Buy milk\nWalk the dog\nLearn Python\n"


def test_load_todos_reads_todos_correctly(tmp_path):
    filepath = tmp_path / "todos.txt"

    with open(filepath, "w") as file:
        file.write("Buy milk\nWalk the dog\nLearn Python\n")

    result = load_todos(filepath)

    assert result == ["Buy milk", "Walk the dog", "Learn Python"]


def test_write_and_load_todos(tmp_path):
    filepath = tmp_path / "todos.txt"
    todos = ["Task 1", "Task 2", "Task 3"]

    write_todos(todos, filepath)

    loaded = load_todos(filepath)

    assert loaded == todos