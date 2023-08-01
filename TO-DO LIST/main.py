
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    if 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    if 'edit' in user_action:
        number = int(input("Number of the todo to edit: "))
        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter a new todo: ")
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    if 'complete' in user_action:
        number = int(input("Number of the todo to complete: "))

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1      # This is done to make it easier and not have to do the calc again and again
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        print(f"Todo {todo_to_remove} was removed from the list.")

    if 'exit' in user_action:
        break

print("Bye!")
