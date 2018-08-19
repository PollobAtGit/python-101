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
                        return self.internal_array[child_index].frequency
                    return self.__default_min_value

            lft_indx = get_child_index(i, right_child = False)
            rght_indx = get_child_index(i, right_child = True)

            lft_child = get_child_value(lft_indx)
            rigt_child = get_child_value(rght_indx)

            if i < len(self.internal_array) and self.internal_array[i].frequency < max(lft_child, rigt_child):
                
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

            compare_and_swap(lambda : self.internal_array[parent_index].frequency < self.internal_array[i].frequency)

    def swap(self, i, j):
        if i is not None and j is not None:
            if i < len(self.internal_array) and j < len(self.internal_array):
                self.internal_array[i], self.internal_array[j] = self.internal_array[j], self.internal_array[i]

    def __str__(self):
        return "".join([str(x) for x in self.internal_array])

    def is_empty(self):
        return len(self.internal_array) == 0


class CharFreq:
    def __init__(self, ch, freq):
        self.character = ch
        self.frequency = freq

    def __str__(self):
        return '{ ch: ' + self.character + ', freq: ' + str(self.frequency) + ' }'

class Solution(object):

    def frequencySort(self, s):
        if s:
            freq_counter = {}

            for x in s:
                if x in freq_counter:
                    freq_counter[x] = freq_counter[x] + 1
                else:
                    freq_counter[x] = 1

            mh = MaxHeap()

            for yy in freq_counter.items():
                mh.insert(CharFreq(yy[0], yy[1]))

            ret = []
            while not mh.is_empty():
                el = mh.extract_max_from_heap()
                ret.append(el.character * el.frequency)

            return "".join(y for y in ret)
        return ""



s = Solution()

'''
print(s.frequencySort("tree"))
print(s.frequencySort("cccaaa"))
print(s.frequencySort("Aabb"))
print(s.frequencySort(""))
print(s.frequencySort(None))
'''

# print(s.frequencySort("dacca"))
print(s.frequencySort("raaeaedere"))# eeeeaaadrr
# "eeeeaaarrd"