import pytest
import project
import os


def test_create():
    project.create("test_create.csv")
    assert os.path.exists("CSV_Files/test_create.csv")


def test_save():
    project.create("test_save.csv")
    tasks = [
        {"id": "0", "desc": "a", "deadline": ""},
        {"id": "1", "desc": "b", "deadline": "2022-09-09"},
    ]
    project.save("test_save.csv", tasks)

    assert project.load("test_save.csv") == tasks


def test_load():
    tasks = [
        {"id": "0", "desc": "a", "deadline": ""},
        {"id": "1", "desc": "b", "deadline": "2022-09-09"},
    ]
    assert project.load("test_load.csv") == tasks


def test_delete():
    project.create("test_delete.csv")
    project.delete("test_delete.csv")
    assert not os.path.exists("CSV_Files/test_delete.csv")

    with pytest.raises(FileNotFoundError):
        project.delete("abc.txt")
