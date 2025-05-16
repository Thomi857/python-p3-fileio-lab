file_name = "/Development/code/se-prep/PHASE-3/python-p3-fileio-lab/file_learn"
file_content = "This is a test content."

def write_file(file_name, file_content):
    with open(f"{file_name}.txt", 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", 'a') as file:
        file.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt", 'r') as file:
        return file.read()
