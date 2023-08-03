class TodoList:
    def __init__(self):
        self._todo = []
        
        

    def add(self, todo):
        self._todo.append(todo)
        
    
    def incomplete(self):
        return [task for task in self._todo if not task.complete]
        

    def complete(self):
        return [task for task in self._todo if task.complete == True]
        
        
