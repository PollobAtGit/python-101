
class MaxHeap:
    
    def __init__(self):
        self.internal_array = []
        self.__default_min_value = -65536

    def get_parent_index(self, i):
        
        if i is not None:
            if i == 0:
                return i
            indx = (i - 2) / 2 if i % 2 == 0 else (i - 1) / 2
            return int(indx)

    def insert(self, x):
        
        if x is not None:
            self.internal_array.append(x)
            self.up_heapify(len(self.internal_array) - 1)

    def extract_max_from_heap(self):

        if self.is_empty():
            return self.__default_min_value

        last_el = self.internal_array.pop()

        if self.is_empty():
            return last_el

        max_value = self.internal_array[0]
        self.internal_array[0] = last_el
        self.down_heapify(0)

        return max_value

    def down_heapify(self, i):
        if i is not None:

            def get_child_index(i, right_child = True):
                if i is not None:
                    if i == len(self.internal_array) - 1:
                        return i

                    if right_child:
                        return 2 * i + 2
                    return 2 * i + 1

            def get_child_value(child_index):
                if child_index is not None:
                    if child_index <= len(self.internal_array) - 1:
                        return self.internal_array[child_index]
                    return self.__default_min_value

            lft_indx = get_child_index(i, right_child = False)
            rght_indx = get_child_index(i, right_child = True)

            lft_child = get_child_value(lft_indx)
            rigt_child = get_child_value(rght_indx)
            
            if self.internal_array[i] < max(lft_child, rigt_child):
                
                dwned_indx = lft_indx if rigt_child == self.__default_min_value or lft_child > rigt_child  else rght_indx

                self.swap(i, dwned_indx)
                self.down_heapify(dwned_indx)


    def up_heapify(self, i):
        
        if i:
            parent_index = self.get_parent_index(i)

            def compare_and_swap(comparison_fn):
                if comparison_fn and callable(comparison_fn):
                    if comparison_fn():
                        self.swap(i, parent_index)
                        self.up_heapify(parent_index)

            compare_and_swap(lambda : self.internal_array[parent_index] < self.internal_array[i])

    def swap(self, i, j):
        if i is not None and j is not None:
            self.internal_array[i], self.internal_array[j] = self.internal_array[j], self.internal_array[i]

    def __str__(self):
        return str(self.internal_array)

    def is_empty(self):
        return len(self.internal_array) == 0



mh = MaxHeap()

mh.insert(0)
mh.insert(1)
mh.insert(2)
mh.insert(3)
mh.insert(4)
mh.insert(5)
mh.insert(5)

print(mh)

print(mh.extract_max_from_heap())
print(mh)

print(mh.extract_max_from_heap())
print(mh)

print(mh.extract_max_from_heap())
print(mh)

print(mh.extract_max_from_heap())
print(mh)

print(mh.extract_max_from_heap())
print(mh)

print(mh.extract_max_from_heap())
print(mh)

print(mh.extract_max_from_heap())
print(mh)

print(mh.extract_max_from_heap())
print(mh)

print(mh.extract_max_from_heap())
print(mh)

# [5, 3, 4, 0, 2, 1]
