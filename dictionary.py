import json as jn
import difflib

data  = jn.load(open("C:\\Users\LG_ML\Desktop\DATA\Py-main\Programs\dictionary\data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(difflib.get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s? Press Y if Yes and N if No" % difflib.get_close_matches(word, data.keys())[0])
        print(yn)
        if yn =="Y" or yn == "y":
            return data[difflib.get_close_matches(word, data.keys())[0]]
        elif yn =="N" or yn == "n":
            return "Word doesn't exist, Try again"
        else:
            return "Cant understand your entery"
    else:
        return "The word is doesn't exist, Try again"

word = input("Enter word: ")
output = (translate(word))
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
translate()
