text = input()
word = input()


def search(text, word):
    text=text.split(' ')
    if word in text:
        return "word found"
    else:
        return "word not found"


print(search(text, word))
