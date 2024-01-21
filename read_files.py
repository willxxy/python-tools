### TXT STUFF
file_path = '/path/to/txt_file.txt'

with open(file_path, 'r') as file:
    file_contents = file.readlines()

### JSON STUFF
with open('your_file.json', 'r') as file:
    data = json.load(file)
