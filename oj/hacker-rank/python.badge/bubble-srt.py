
def bubble_sort(s):
    if s is not None:
        swap_count = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] > s[j]:
                    s[i], s[j] = s[j], s[i]
                    swap_count += 1

        print("Array is sorted in " + str(swap_count) + " swaps.")
        print("First Element: " + str(s[0]))
        print("Last Element: " + str(s[len(s) - 1]))

def test_code():
    bubble_sort(list(map(int, input().split())))


test_code()
