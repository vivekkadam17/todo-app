# todo-app
To-Do List Application
A simple yet feature-rich console-based to-do list manager built with Python.

Features

 Add Tasks: Add new tasks with automatic timestamps
 View Tasks: Display all tasks in a formatted list
 Remove Tasks: Remove specific tasks by number
 Search Tasks: Find tasks containing specific keywords
 Clear All: Remove all tasks with confirmation
 Persistent Storage: Tasks are saved to tasks.txt file
 Error Handling: Robust error handling for file operations

 -Usage-
Running the Application: python todo.py


-Menu Options-

Add Task: Enter a new task to add to your list
View Tasks: Display all current tasks with timestamps
Remove Task: Remove a specific task by selecting its number
Search Tasks: Find tasks containing specific text
Clear All: Remove all tasks (with confirmation)
Exit: Save and quit the application

-Example Usage:
 TO-DO LIST MANAGER
========================================
1. Add Task
2. View Tasks
3. Remove Task
4. Search Tasks
5. Clear All Tasks
6. Exit
----------------------------------------
Choose an option (1-6): 1
Enter a new task (or 'back' to return to menu): Complete Python assignment
Task added: Complete Python assignment
Tasks saved successfully!

File Structure
todo-list-app/
── todo.py          # Main application file
── tasks.txt        # Auto-generated file to store tasks
── README.md        # This file
Technical Details
Key Concepts Implemented

File Handling: Reading from and writing to text files
Lists: Dynamic task storage and manipulation
String Manipulation: Input validation and formatting
Error Handling: Graceful handling of file operations
Object-Oriented Programming: Clean class-based structure

File Operations

Tasks are automatically saved to tasks.txt after each modification
If the file doesn't exist, it's created automatically
Uses context managers (with statement) for safe file handling