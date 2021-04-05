import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        choice = input("Did you mean %s instead? Enter Y if yes, N if no. " %
                       get_close_matches(word, data.keys())[0])
        if choice.upper() == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif choice.upper() == 'N':
            return "The word doesn't exist"
        else:
            return "Please input Y or N."
    else:
        return "Ths word doesn't exist"


word = input("Enter: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
