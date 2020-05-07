from urllib.request import urlopen

downloaded_lines = urlopen('http://sixty-north.com/c/t.txt')

words = []

for d_line in downloaded_lines:
    for word in d_line.split():
        words.append(word)

downloaded_lines.close()

print(words)
