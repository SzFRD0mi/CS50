from termcolor import colored
from datetime import date
import re


class Todo:
    def __init__(self, *tasks):
        self.tasks = tasks
        for task in self.tasks:
            task["deadline"] = self.convert_to_date(task["deadline"])

    # returns a formatted string, that lists the todo list
    def __str__(self):
        if not self.tasks:
            return "\nThe list is empty"

        # store each task in the output string sorted by date
        # if the task does not have a deadline, omit the date from the output
        # also, check if the deadline is past due, if so, output the date in red color
        output = "\nTodo List:\n"

        for task in self.sort(self.tasks):
            if type(task["deadline"]) is not date:
                task["deadline"] = self.convert_to_date(task["deadline"])
            if task["deadline"]:
                if date.today() >= task["deadline"]:
                    output += f"  Task: {task["desc"]} - Deadline: {colored(task["deadline"], "red")}\n"
                else:
                    output += f"  Task: {task["desc"]} - Deadline: {task["deadline"]}\n"
            else:
                output += f"  Task: {task["desc"]}\n"

        return output.rstrip("\n")

    def add_task(self):
        desc = input("\nTask: ")
        deadline = self.get_deadline() if self.ask_if_deadline() else None

        self.tasks.append(
            {"id": None, "desc": desc, "deadline": deadline}
        )

        self.reset_id()

        return f'\nTask "{desc}" created'

    def delete_task(self):
        if not self.tasks:
            return "\nThe list is empty"

        print("\nTasks: ")
        for task in sorted(self.tasks, key=lambda task: task["id"]):
            print(f"{task['id']} - {task['desc']}")

        print("Which task would you like to remove? ")
        while True:
            id = input(
                "\nPlease input the id of an existing task or press 'c' to cancel\n"
                + "Id: "
            )
            if id == "c":
                return "\nDeletion canceled"

            for task in self.tasks:
                if id == task["id"]:
                    self.tasks.remove(task)
                    self.reset_id()
                    return f"\nTask \"{task['desc']}\" removed"


    def reset_id(self):
        i = 0
        for task in self.tasks:
            task["id"] = str(i)
            i += 1

    def ask_if_deadline(self):
        while True:
            use_dl = input("Would you like to set a deadline? (y/n): ").lower()
            if use_dl == "y":
                return True
            elif use_dl == "n":
                return False
            else:
                print("Please use the 'y' or 'n' characters\n")

    def get_deadline(self):
        while True:
            deadline = input(
                "\nValid formats: YYYY-MM-DD, YYYY/MM/DD or YYYY.MM.DD\n" + "Deadline: "
            )
            if self.validate_deadline(deadline):
                if "/" in deadline:
                    year, month, day = deadline.split("/")
                elif "-" in deadline:
                    year, month, day = deadline.split("-")
                else:
                    year, month, day = deadline.split(".")

                return date(int(year), int(month), int(day))
            else:
                print("Invalid date format")

    def validate_deadline(self, deadline):
        match = re.search(
            r"^(\d{4}/\d{2}/\d{2})|(\d{4}-\d{2}-\d{2})|(\d{4}\.\d{2}\.\d{2})$", deadline
        )
        if match:
            return True
        else:
            return False

    def convert_to_date(self, str):
        if str:
            year, month, day = str.split("-")
            return date(int(year), int(month), int(day))
        return None

    def sort(self, tasks):
        list_with_dl = []
        list_without_dl = []

        for task in tasks:
            if task["deadline"]:
                list_with_dl.append(task)
            else:
                list_without_dl.append(task)

        sorted_list = []

        for task in sorted(list_with_dl, key=lambda task: task["deadline"]):
            sorted_list.append(task)
        for task in list_without_dl:
            sorted_list.append(task)

        return sorted_list

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        self._tasks = list(tasks)
