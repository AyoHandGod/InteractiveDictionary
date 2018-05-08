import json       # need json to translate json file
# using SequenceMatcher to see if any
#  missed words have a near match in dict.
from difflib import SequenceMatcher as SM


data = json.load(open("data.json"))  # load dictionary of data in json file


def definition(word):
    """
    Searches dictionary for word.
    :param word: word to search dictionary for
    :return: If word found, returns definition. If not, returns string detailing
             failure.
    """
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist. Please double check spelling"



word = input("Enter word: ")
print(SM(None, "rainn", "rain").ratio())
print(definition(word.lower()))
