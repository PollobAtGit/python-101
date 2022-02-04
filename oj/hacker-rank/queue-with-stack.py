class Queue:

    def __init__(self):
        self.queue= []

    def process(self, query, value):
        if query == 1:
            self.queue = self.queue + [value] 
        elif query == 2:
            self.queue = self.queue[1:]
        elif query == 3 and self.queue:
            print(self.queue[0])


if __name__ == '__main__':
    query_count = int(input())

    queue = Queue()

    while query_count:

        input_arr = input().split()
        query = int(input_arr[0])
        value = None

        if query == 1:
            value = int(input_arr[1])

        queue.process(query, value)

        query_count = query_count - 1
