import os

# non-pythonic approach
def read_lines_from_file(file_name):

    if file_name:

        if os.access(file_name, os.R_OK):
            with open(file_name) as f:
                return f.read()

        else:
            print("file can't be accessed")


def read_lines_from_file_pythonic(file_name):
    pass

    # not working
    
    '''
    if file_name:
        f = None
        try:
            f = open(file_name)
        except IOError as error:
            # print('File ({file_name}) not found'.format(file_name))
            print('File (' + file_name + ') not found')
        finally:

            # using context manager
            with f:
                return f.read()
    '''


print(read_lines_from_file('some_random_txt_file.txt'))
print(read_lines_from_file_pythonic('some_random_txt_file.txt'))
