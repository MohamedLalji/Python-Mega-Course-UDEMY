waiting_list = ["sen", "ben", "John"]
waiting_list.sort()

for x, name in enumerate(waiting_list):
    print(f"{x + 1}.{name.capitalize()}")
