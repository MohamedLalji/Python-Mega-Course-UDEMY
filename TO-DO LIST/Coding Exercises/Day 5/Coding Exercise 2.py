ips = ['100.122.133.105', '100.122.133.111']

user_input = int(input("Enter the index of the IP you want: "))

match user_input:
    case 0:
        print(f"You chose {ips[0]}")
    case 1:
        print(f"You chose {ips[1]}")
