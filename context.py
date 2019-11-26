import os
from contextlib import contextmanager

class ManagedFile:
    """custom context manager to write to file"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exec_type, exec_value, exec_traceback):
        if self.file:
            self.file.close()
        if exec_type:
            print('Error: ', exec_type, exec_value)
        return True

@contextmanager
def open_managed_file(filename, mode):
    f = open(filename, mode)
    try:
        #everything that we have written in the enter function
        yield f
    finally:
        f.close()

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir("directory 1"):
    print(os.listdir())

with ManagedFile('notes.txt', 'w') as file:
    file.write("File content")

with open_managed_file('note.txt', 'w') as file:
    file.write("File content")


