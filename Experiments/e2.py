user_prompt = "Enter a.txt todo: "

todos = []


while True:
    todo = input(user_prompt)
    print(todo.title())
    todos.append(todo)
    print(todos)

