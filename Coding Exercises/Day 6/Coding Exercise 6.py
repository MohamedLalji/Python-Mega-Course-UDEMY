filenames = ['doc.txt', 'report.txt', 'presentation.txt']

content = "Hello"

for text, filename in zip(content, filenames):
    file = open(f"{filename}", 'w')
    file.write(content)
    file.close()