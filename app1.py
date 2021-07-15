import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        response = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys(), cutoff=0.8)[0])
        if response ==  "Y" or response == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif response == "N" or response == "n":
            return "The word does not exist. Please check it."
        else: 
            return "We didn't understand your entry"
    else:
        return "The word does not exist. Please check it."

word = input("Enter word: ")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)