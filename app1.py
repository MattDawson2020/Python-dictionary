import json
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word does not exist. Please check it."

word = input("Enter word: ")

print(translate(word))