import os


def write_to_file(lines, file_name):
    
    if lines:
    
        with open(file_name, 'w+') as f:
            
            new_line = '\r\n'

            for x in lines:
                f.write(x + new_line)

            f.write(new_line)

def copy_and_remove(file_to_copy):
    
    import shutil
    import os

    shutil.copy(file_to_copy, 'text-file.txt')
    os.remove(file_to_copy)

print(os.getcwd())
os.system('mkdir internal-dir')
os.chdir('internal-dir')

# get working directory
print(os.getcwd())


# change directory
os.chdir('./..')

os.rmdir('internal-dir')

# list given directory contents
print(os.listdir('./'))


print("dir(...)")


# print(dir(os))

import shutil

temp_file_name = 'temp-file.txt'

write_to_file(['asdf', 'vtpo'], temp_file_name)

# copy_and_remove(temp_file_name)

shutil.move(temp_file_name, 'text-file.txt')


import glob

# print(os.listdir('*.py'))

# wildcard can't be used with os.listdir(...)
print(glob.glob('./*.txt'))

