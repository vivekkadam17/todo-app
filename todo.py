
from datetime import datetime

class TodoApp:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
   
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    task = line.strip()
                    if task: 
                        self.tasks.append(task)
            print(f"Loaded {len(self.tasks)} tasks from {self.filename}")
        except FileNotFoundError:
            print(f"No existing task file found. Starting with empty task list.")
         
            with open(self.filename, 'w') as file:
                pass
    
    def save_tasks(self):
        
        try:
            with open(self.filename, 'w') as file:
                for task in self.tasks:
                    file.write(task + '\n')
            print("Tasks saved successfully!")
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self):
       
        while True:
            task = input("Enter a new task (or 'back' to return to menu): ").strip()
            if task.lower() == 'back':
                return
            if task:
                
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                formatted_task = f"[{timestamp}] {task}"
                self.tasks.append(formatted_task)
                print(f"Task added: {task}")
                self.save_tasks()
                break
            else:
                print("Task cannot be empty. Please try again.")
    
    def view_tasks(self):
        
        if not self.tasks:
            print("\n No tasks found! Your to-do list is empty.")
            return
        
        print(f"\n Your To-Do List ({len(self.tasks)} tasks):")
        print("-" * 50)
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        print("-" * 50)
    
    def remove_task(self):
        
        if not self.tasks:
            print("No tasks to remove!")
            return
        
        self.view_tasks()
        
        while True:
            try:
                choice = input("\nEnter task number to remove (or 'back' to return): ").strip()
                if choice.lower() == 'back':
                    return
                
                task_num = int(choice)
                if 1 <= task_num <= len(self.tasks):
                    removed_task = self.tasks.pop(task_num - 1)
                    print(f"Removed task: {removed_task}")
                    self.save_tasks()
                    break
                else:
                    print(f"Please enter a number between 1 and {len(self.tasks)}")
            except ValueError:
                print("Please enter a valid number or 'back'")
    
    def search_tasks(self):
       
        if not self.tasks:
            print("No tasks to search!")
            return
        
        search_term = input("Enter search term: ").strip().lower()
        if not search_term:
            print("Search term cannot be empty!")
            return
        
        found_tasks = []
        for i, task in enumerate(self.tasks, 1):
            if search_term in task.lower():
                found_tasks.append((i, task))
        
        if found_tasks:
            print(f"\n Found {len(found_tasks)} tasks containing '{search_term}':")
            print("-" * 50)
            for task_num, task in found_tasks:
                print(f"{task_num}. {task}")
            print("-" * 50)
        else:
            print(f"No tasks found containing '{search_term}'")
    
    def clear_all_tasks(self):
        if not self.tasks:
            print("No tasks to clear!")
            return
        
        confirm = input(f"Are you sure you want to delete all {len(self.tasks)} tasks? (yes/no): ").strip().lower()
        if confirm in ['yes', 'y']:
            self.tasks.clear()
            self.save_tasks()
            print("All tasks cleared!")
        else:
            print("Clear operation cancelled.")
    
    def display_menu(self):
        
        print("\n" + "="*20)
        print(" TO-DO LIST MANAGER")
        print("="*20)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Search Tasks")
        print("5. Clear All Tasks")
        print("6. Exit")
        print("-"*20)
    
    def run(self):
       
        print("Welcome to your Personal To-Do List Manager! ")
        
        while True:
            self.display_menu()
            
            choice = input("Choose an option (1-6): ").strip()
            
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.remove_task()
            elif choice == '4':
                self.search_tasks()
            elif choice == '5':
                self.clear_all_tasks()
            elif choice == '6':
                print("\n Thank you for using To-Do List Manager!")
                print("Your tasks have been saved. Have a productive day!")
                break
            else:
                print(" Invalid choice! Please select 1-6.")
            
            
            if choice != '6':
                input("\nPress Enter to continue...")

def main():
   
    try:
        app = TodoApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n Application interrupted. Your tasks have been saved!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()