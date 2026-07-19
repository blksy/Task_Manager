# Task Manager CLI

A simple command-line task manager written in Python that allows users to create, view, edit, and complete todos.

The project focuses on practicing Python fundamentals, file handling, modular programming, and writing unit tests.

## Features

- Add new todos
- Display existing todos
- Edit todos
- Complete/remove todos
- Store todos permanently in a text file
- Handle invalid user input
- Unit tests with pytest

## Technologies

- Python 3
- Pytest

## Project Structure

task-manager/
│
├── main.py
├── functions.py
├── todos.txt
├── tests/
│ └── test_functions.py
│
└── README.md

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/task-manager.git
```

Navigate to the project folder:
cd task-manager

Install dependencies:
pip install pytest

Usage:
Run the application:
python main.py

Available commands:
add <todo>
show
edit <number>
complete <number>
exit

Example:
add Learn Python

1. Learn Python

edit 1
Enter new todo: Learn pytest

complete 1
"Learn pytest" was removed from the list.

Testing

Run tests:

pytest
