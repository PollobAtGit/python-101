import mem_profile
import random
import time

names = [ 'john', 'corey', 'adam', 'steve', 'rick', 'thomas' ]
majors = [ 'math', 'engineering', 'comp-sci', 'arts', 'business' ]

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))


def people_list(peoples):

    if peoples:
        return [{ 'id': i, 'name': random.choice(names), 'major': random.choice(majors) } for i in range(1, peoples)]

def people_generator(peoples):

    if peoples:
        return ({ 'id': i, 'name': random.choice(names), 'major': random.choice(majors) } for i in range(1, peoples))
            

before_time = time.clock()
people_list(100000)
end_time = time.clock()

print('Memory (After): {}.Mb'.format(mem_profile.memory_usage_psutil()))
print('Took {} seconds'.format(end_time - before_time))

