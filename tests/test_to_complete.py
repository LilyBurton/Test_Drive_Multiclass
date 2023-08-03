from lib.todo import Todo

def test_construct_task():
    todo = Todo("Clean the kitchen")
    assert todo.task == "Clean the kitchen"

def test_task_is_incomplete():
    todo = Todo("Clean the kitchen")
    assert todo.complete == False
    
def test_task_is_complete():
    todo = Todo("Clean the kitchen")
    todo.mark_complete()
    assert todo.complete == True

