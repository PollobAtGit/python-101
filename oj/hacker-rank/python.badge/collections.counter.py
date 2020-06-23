
import collections

if __name__ == "__main__":
    input()

    shoes = list(map(int, input().split()))
    shoes_dic = collections.Counter(shoes)

    purchase_count = int(input())
    t_price = 0

    for _ in range(purchase_count):
        size_price = list(map(int, input().split()))
        if len(size_price) == 2:
            if size_price[0] in shoes_dic:
                shoes_count = shoes_dic[size_price[0]]
                if shoes_count:
                    t_price += size_price[1]
                    shoes_dic[size_price[0]] = shoes_dic[size_price[0]] - 1

    print(t_price)


