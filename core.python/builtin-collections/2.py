import copy

nums = [1, 2, [5, 6, 7], {8}]
sliced = nums[:]
copied_via_copy = nums.copy()
copied_via_ctor = list(nums)  # list(...) ctor also creates a shallow copy

deep_copied = copy.deepcopy(nums)

print('nums[2] is copied[0]: ', nums[2] is sliced[2])
print('nums[2] is copied[0]: ', nums[2] is copied_via_copy[2])
print('nums[2] is copied_via_ctor[0]: ', nums[2] is copied_via_ctor[2])
print('nums[2] is deep_copied[0]: ', nums[2] is deep_copied[2])

# assignment was not working because in assignment we get a new object
nums[2].append(9999)

print(nums, "\t", copied_via_copy, "\t", copied_via_ctor, "\t", deep_copied)
