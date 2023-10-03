


# make the list to hold ncurrent todos
todos=['yo','ya','yen']
# adds a item to the list
addTodo=input(' enter word here to add Todo list')
todos.append(addTodo)
#  removes a item of choice from the list
RemoveTodo=input('enter word here to remove from Todo list')
todos.remove(input)

print('your current todos are')
print(todos)
print(' would you like to add or remove a Todo?')
decision=input('Add or remove')
if (decision == 'Add'): 
    addTodo=input(' What is your new todo')
    todos.append(addTodo)
elif (decision == 'remove'):
    RemoveTodo=input('enter word here to remove from Todo list')
    todos.remove(input)
print('Your current todos are:')
print(todos)
print('would you like to add or remove a todo')
