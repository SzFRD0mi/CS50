import os
import fnmatch
import re
import csv
from todo import Todo
from termcolor import colored


def main():
    print("\nAvailable files to load:")
    print(*get_csv_files(), sep=" ; ")

    file_name = get_file_name()
    if colored(file_name, "cyan") not in get_csv_files():
        create(file_name)
    todo_list = Todo(*load(file_name))

    print_commands()
    while True:
        match input("\nCommand: ").lower():
            case "h" | "help":
                print_commands()
            case "c":
                print(todo_list.add_task())
            case "d":
                print(todo_list.delete_task())  
            case "s":
                print(todo_list)
            case "save":
                save(file_name, todo_list.tasks)
            case "delf":
                answ = input(f"\nAre you sure you want to delete {file_name}? (y) ")
                if answ == "y":
                    delete(file_name)
            case "exit" | "e":
                print("\nExiting...\n")
                break
            case _:
                print("\nPlease use one of the listed commands")


# returns the all csv files from the CSV_Files folder
def get_csv_files():
    csv_files = []
    for file in os.listdir("CSV_Files"):
        if fnmatch.fnmatch(file, "*.csv"):
            csv_files.append(colored(file, "cyan"))
    return sorted(csv_files)


# prompts the user to input a file name
# check if the imput formati is valid, if not, prompts the user again
def get_file_name():
    print(
        "\nPlease type in the name of the file to load.\n"
        + "Alternatively type in a new filename to create a new file."
    )

    while True:
        file_name = input("\nFile name: ")
        try:
            if re.search(r"^[\w/]+(?:\.csv)?$", file_name.lower()):
                return file_name if file_name.endswith(".csv") else file_name.rstrip(".csvCSV") + ".csv"
            else:
                raise TypeError()
        except TypeError:
            print("Invalid file name. Please try again.")


def create(file_name):
    with open("CSV_Files/" + file_name, "a") as file:
        csv.DictWriter(file, fieldnames=["id", "desc", "deadline"])
    print(f"\n{file_name} created")


def save(file_name, tasks):
    with open("CSV_Files/" + file_name, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "desc", "deadline"])
        for task in tasks:
            writer.writerow(
                {"id": task["id"], "desc": task["desc"], "deadline": task["deadline"]}
            )
        print(f"\n{file_name} saved successfully")


def load(file_name):
    tasks = []
    with open("CSV_Files/" + file_name) as file:
        reader = csv.DictReader(file, fieldnames=["id", "desc", "deadline"])
        for row in reader:
            tasks.append(
                {"id": row["id"], "desc": row["desc"], "deadline": row["deadline"]}
            )
    print(f"\n{file_name} loaded succesfully")
    return tasks


def delete(file_name):
    try:
        os.remove("CSV_Files/" + file_name)
        print(f"{file_name} deleted")
    except FileNotFoundError:
        raise FileNotFoundError("File not found")


def print_commands():
    print(
        "\nPlease choose an option:\n"
        + "  'h' or 'help' - list available commands\n"
        + "  'c' - create new task\n"
        + "  'd' - delete a task\n"
        + "  's' - show current tasks\n"
        + "  'save' - save current tasks\n"
        + "  'delf' - delete the current todo list\n"
        + "  'exit' or 'e' - exit the program"
    )


if __name__ == "__main__":
    main()
