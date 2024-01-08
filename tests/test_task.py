import pytest
from PyQt6.QtWidgets import QApplication
from tasks_list import TasksList


@pytest.fixture
def tasks_list():
    app = QApplication([])
    tasks_list = TasksList()
    yield tasks_list
    app.quit()


def test_add_task(tasks_list):
    tasks_list.add_task("Test Task 1")
    assert tasks_list.count() == 1


def test_remove_checked_tasks(tasks_list):
    tasks_list.add_task("Test Task 1")
    tasks_list.add_task("Test Task 2")

    assert tasks_list.count() == 2

    tasks_list.remove_checked_tasks()
    assert tasks_list.count() == 2
