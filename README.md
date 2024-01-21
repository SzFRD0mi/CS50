# Todo Lists Application
### Video Demo:  https://youtu.be/ov-00ZOriJs
### Description:
This is my final project for the CS50P course, a console application that creates or loads in a "Todo List" from a CSV file and allows the user to make changes to the list.
The main goal for this project was to create a simple but useful application that anyone would be able to utilize in their everyday lives.
I have tried to incorporate a lot of different programming techniques and tricks shown throughout the course, whilst trying to keep my program simple, robust and easy to read.

The program has two files called `project.py` and `todo.py`.
- `project.py` unilizes file I/O and the program's main function can also be found here
- `todo.py` contains the `Todo` class, which encapsulates every function that is related to the tasks inside a todo list

#### Usage of the program:

The program works with a console interface for outputting information to the user, such as what the program does and what commands the user should use to successfully create and change tasks in a todo list. The progrm will keep prompting the user for a command until they exit the program.


When the program starts it outputs the name of every csv file from the CSV_Files directory and prompts the user to choose a file to load. Alternatively, they can create a new file by entering a file name that does not exist yet. At this point, the `get_file_name` function is called that is responsible for prompting the user for a file name and checking whether the input is in a valid format. If it is valid, the function will return the file name, formatted as "file.csv", if not, the program will keep re-prompting the user until a valid input is received. The name of the file, that the user entered will be stored in a str called `file_name`, which will be used multiple times throughout the lifespan of the program.
After the file name is stored, the `load` function is called, that accepts the file name as a parameter and reads through the file, then returns its content as a list of dictionaries.
The return value of this function will be used as a parameter when instantiating the Todo class, thus creating our `todo_list` instance, which we will use to work with the contents of the file.
After the Todo class is instantiated, the `print_commands` function is called, and the user will see a nicely formatted console output, that describes the list of commands that the user can use as follows:
```
  Please choose an option:
    'h' or 'help' - list available commands
    'c' - create new task
    'd' - delete a task
    's' - show current tasks
    'save' - save current tasks
    'delf' - delete the current todo list
    'exit' or 'e' - exit the program
```

Each command calls a function that is responsible for doing the tasks described next to the commands.
At this point the program will utilize a match-case statement to simulate an interactive environment. It will accept every command shown in the message above, case insensitively. If the user types in something other than the listed commands, the program will re-prompt the user for a "correct" command.

Below, you can find a thorough explanation on what happens when each of the commands are pressed:
  - **'h' or 'help'** - calls the `print_commands` function (again), that outputs the above message to the console, listing all available commands and a brief description on what each command is responsible for. I wanted to allow the user to check the available commands in case they forgot the commands and did not want to scroll up the terminal but I didn't want to output it between each command prompt.
  - **'c'** - calls the `add_task` instance function, which does the following:
    - prompts the user for a task description.
    - `ask_if_deadline` function is called, which asks the user if they would like a deadline for the task.
    The user will be able to use the 'y' or 'n' commands to answer, if they do not use either, they will be reprompted.
    - if the answer to the above is yes, then the `get_deadline` function is called, and the user will also be prompted for a deadline.
    This function accepts the following date formats: 'YYY-MM-DD' or 'YYY/MM/DD' or 'YYY.MM.DD' and returns a datetime.date object.
    The user will keep getting prompted for a date until they use either of the 3 formats listed above
    - creates a new dictionary based on the user inputs and adds it to the list of tasks inside the `todo_list` class instance
    - returns a str describing that the task was created
  - **'d'** - calls the `delete_task` instance function, which does the following:
    - if the list of tasks inside the class instance is empty, it returns a str describing that the list is empty
    - if the list of tasks is not empty, the list of tasks will be printed to the console sorted by ID and the user will be prompted to input the ID of the task that they would like to remove or press c to cancel the deletion process. If the user inputs something, that is not an existing ID, they will be re-prompted
    - the chosen task will be removed from the list of tasks and the function returns a str confirming the deletion
  - **'s'** - calls the __str__ instance function, that returns a formatted string. The string includes each tasks description and their deadlines - if they have a deadline - and the output is sorted by the deadlines. The tasks with no deadlines will be put at the end of the output. Also, if a deadline is past due - meaning that the deadline is before or on the same day, when the program is used - it will be shown in red.

  Here is an example output of the __str__ instance function, where <span style="color:red">2023-10-18</span> would be output in red as of today, 10/18/2023:
```
    Todo List:
      Task: Go to work - Deadline: 2023-10-18
      Task: Clean - Deadline: 2023-12-31
      Task: Random task - Deadline: 9999-12-31
      Task: Workout
      Task: Study
      Task: Wash the dishes
```
  - **'save'** - calls the `save` function, that writes the contents of the list of tasks to the CSV file specified as a parameter
  - **'delf'** - this is an abbreviation to "delete file", it calls the `delete` function, which deletes the CSV file specified as a parameter. In this case, the currently used `file_name` will be the parameter of the function, hence the "currently used" file will be deleted if the user types in 'y' after being prompted
  - **'e' or 'exit'** - this will break out of the match-case statement and the programs life cycle will come to an end

I have debated making the `Todo` class "static", because only one todo list would be used in my program. However, I decided to design the class the way it is because I realized that it enables the class to be used in more way. For example, if I wanted to create a program that works on multiple todo lists (files) at the same time, I could use the class from this program.

I have enjoyed working on this project and I feel like I have learned a lot through the way. It was difficult to decide how I would design the code at first, but I kept working on one thing at a time and achieved what I wanted in the end.
