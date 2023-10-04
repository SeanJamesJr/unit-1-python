


# make the list to hold current todos
todos=['yo','ya','yen']


while True:
# states the items in the list  and aks if u want to add or remove one
    print('your current todos are')
    print()
    print()
    print(todos)
    print()
    print()
    print(' would you like to add or remove a Todo?')
    print()
    decision=input('add or remove')
    # adds a item to the list
    if (decision == 'add'): 
        addTodo=input(' What is your new todo ')
        todos.append(addTodo)
        
        print()
        print()
        #  removes a item of choice from the list
    elif (decision == 'remove'):
        RemoveTodo=input('enter word here to remove from Todo list')
        todos.remove(RemoveTodo)
        print(todos)
        print()
        print()
    print('Your current todos are:')
    print(todos)
    print()
    print('would you like to add or remove a todo')
