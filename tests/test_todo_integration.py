from lib.todo_list import TodoList
from lib.todo import Todo

def test_add_todo_in_todo_list():
    todo_list = TodoList()
    todo1 = Todo("Clean the kitchen")
    todo2 = Todo("Go for a walk")
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.incomplete() == [todo1, todo2]

def test_complete_task_not_in_incomplete_list():
    todo_list = TodoList()
    todo1 = Todo("Clean the kitchen")
    todo2 = Todo("Go for a walk")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo1.mark_complete()
    assert todo_list.incomplete() == [todo2]

def test_complete_task_in_complete_list():
    todo_list = TodoList()
    todo1 = Todo("Clean the kitchen")
    todo2 = Todo("Go for a walk")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo1.mark_complete()
    assert todo_list.complete() == [todo1]

