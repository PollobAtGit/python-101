def p(v):
    print(v)

def lengthOfLastWord(s):
    length = 0
    for word in s.split():
        v = word.strip()
        if v:
            length = len(v)
    return length

p(lengthOfLastWord(""))
p(lengthOfLastWord("Hello World"))
p(lengthOfLastWord("   fly me   to   the moon  "))
p(lengthOfLastWord("luffy is still joyboy"))
p(lengthOfLastWord(""))
