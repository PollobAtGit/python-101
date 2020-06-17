if __name__ == "__main__":
    input()
    eng_sub = set(input().split())
    input()
    french_sub = set(input().split())

    print(len(eng_sub ^ french_sub))

