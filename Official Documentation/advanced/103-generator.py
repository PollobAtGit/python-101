
def cubic(nums):
	if nums:
		for x in nums:
			yield x * x * x

"""
1000
8000
27000
"""

for y in cubic([10, 20, 30]):
	print(y)

# <generator object cubic at 0x03458CF0>
print(cubic([10, 20, 30]))

# list creates a list from the generator
print(list(cubic([10, 20, 30])))# [1000, 8000, 27000]

is_generator = (x * x for x in [56, 89, 74])

print(list(is_generator))
