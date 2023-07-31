# Daily journal app

date = input("Enter today's date: ")
mood_rating = input("How do you rate your day today? ")
content = input("Let your thoughts flow:\n")

with open(f"journal/{date}.txt", 'w') as file:
    file.write(mood_rating + 2 * "\n")
    file.write(content)