import sys
import heapq


class Solution(object):
    def findRestaurant(self, listOne, listTwo):
        if listOne and listTwo:

            hashTable = {}
            resultHashTable = {}

            for i, v in enumerate(listOne):
                hashTable[v] = i

            for i, v in enumerate(listTwo):
                q = hashTable.get(v)
                if q is not None:
                    resultHashTable[v] = q + i

            minimum = []
            minimumValue = sys.maxsize

            for key, value in resultHashTable.items():
                if value == minimumValue:
                    minimum.append(key)
                    minimumValue = value
                if value < minimumValue:
                    minimum = [key]
                    minimumValue = value

            return minimum

    def findRestaurantUsingheap(self, listOne, listTwo):
        if listOne and listTwo:

            hashTable = {}
            minHeap = []

            for i, v in enumerate(listOne):
                hashTable[v] = i

            for i, v in enumerate(listTwo):
                if v in hashTable:
                    heapq.heappush(minHeap, (hashTable[v] + i, v))

            q = heapq.heappop(minHeap)
            pres = q[0]
            ret = []

            while q and q[0] == pres:
                ret.append(q[1])
                q = None if not minHeap else heapq.heappop(minHeap)

            return ret


s = Solution()

assert (
    s.findRestaurantUsingheap(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
    )
    == ["Shogun"]
)

assert (
    s.findRestaurantUsingheap(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Shogun", "Burger King"],
    )
    == ["Shogun"]
)
