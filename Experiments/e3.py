todos = []

while True:
    print()
    user_action = input("Type add, show/display, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a.txt todo: ")
            todos.append(todo)
        case 'show' | 'display':
            print("The items in your todo list so far are: ")
            for item in todos:
                item = item.capitalize()
                print(item)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")