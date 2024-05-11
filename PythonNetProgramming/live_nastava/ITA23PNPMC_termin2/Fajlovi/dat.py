file = open('file_path.txt', 'w')
file.write('hello world !')
file.close()

file = open('file_path.txt', 'a')
file.write('hello world!!!!!!!!!!!')
file.close()

file = open('file_path.txt', 'w')
try:
    file.write('hello world')
finally:
    file.close()

with open('file_path.txt', 'w') as file:
    file.write('hello world !')
    

class MessageWriter2:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, *args):
        self.file.close()


# using with statement with MessageWriter

with MessageWriter2('my_file.txt') as xfile:
    xfile.write('hello world.........')
