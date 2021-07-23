import json
#Get close matches to words
from difflib import get_close_matches
#Import our dictionary
data= json.load(open("English_Thesaurus/DICTIONARY.json"))

def translate(w):
    # 'w' will be our variable for word that is inputted
    w = w.lower()
    # Form an if/else loop with conditionals
    if w in data:
        return data[w]
    # Include inputted words that are Capitalized
    elif w.title() in data:
        return data[w.title()]
    # Include inputted words that are ALL CAPS
    elif w.upper() in data:
        return data[w.upper()]
    # Get close matches if > 0
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        # Responding to Y/N inquiry
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist.  Please double check it"
        else:
            return "We didn't understand your entry"
    else:
        return("The word doesn't exist.  Please double check it")
# USER INPUT
word = input("Enter word: ")

output = (translate(word))
# Storing list object as a variable, so as to print out multiple definitions of a word separately
if type(output) == list:
    for item in output:
        print(item)
# Printing out items that are dictionary type
elif type(output) == dict:
    for item in output:
        print(item)
# Printing out items that are strings
else:
    print(output)



