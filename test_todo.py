import todo
import project
import datetime

test_list = todo.Todo(*project.load("test_load.csv"))


def test_validate_deadline():
    assert test_list.validate_deadline("2023-10-23") == True
    assert test_list.validate_deadline("2023.10.23") == True
    assert test_list.validate_deadline("2023/10/23") == True
    assert test_list.validate_deadline("2023.10/23") == False
    assert test_list.validate_deadline("dog") == False


def test_convert_to_date():
    assert test_list.convert_to_date("") == None
    assert test_list.convert_to_date("2023-10-12") == datetime.date(2023, 10, 12)


def test_sort():
    tasks = [
        {"id": "0", "desc": "a", "deadline": "2023-09-09"},
        {"id": "1", "desc": "b", "deadline": "2022-09-09"},
    ]
    assert test_list.sort(tasks) == [
        {"id": "1", "desc": "b", "deadline": "2022-09-09"},
        {"id": "0", "desc": "a", "deadline": "2023-09-09"},
    ]
