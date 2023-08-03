from lib.todo_list import TodoList

def test_empty_incomplete_list():
    todo_list = TodoList()
    assert todo_list.incomplete() == []

def test_empty_incomplete_list():
    todo_list = TodoList()
    assert todo_list.complete() == []