class Fib:
    def fib_rec(self, s):
        if s == 1 or s == 2: return 1

        fib_n = self.fib(s - 1) + self.fib(s - 2)
        return fib_n

    def sum_fib(self, k):
        arr = [1, 1]

        for i in range(2, k):
            arr.append(arr[i - 1] + arr[i -2])
        
        return sum(arr)

if __name__ == "__main__":
    f = Fib()

    l = int(input())
    
    for x in range(l):
        print(f.sum_fib(int(input())))
