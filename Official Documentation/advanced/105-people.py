import random
import time
import psutil
import os

def memory_usage_psutil():
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem

names = [ 'john', 'corey', 'adam', 'steve', 'rick', 'thomas' ]
majors = [ 'math', 'engineering', 'comp-sci', 'arts', 'business' ]

print('Memory (Before): {}Mb'.format(memory_usage_psutil()))


def people_list(peoples):

    if peoples:
        return [{ 'id': i, 'name': random.choice(names), 'major': random.choice(majors) } for i in range(1, peoples)]

def people_generator(peoples):

    if peoples:
        return ({ 'id': i, 'name': random.choice(names), 'major': random.choice(majors) } for i in range(1, peoples))
            

before_time = time.perf_counter()
people_lst = people_list(100000)
# people_iterator = people_generator(100000)
# people_lst = list(people_generator(100000))

end_time = time.perf_counter()

# print(len(people_iterator))

print('Memory (After): {}.Mb'.format(memory_usage_psutil()))
print('Took {} seconds'.format(end_time - before_time))

