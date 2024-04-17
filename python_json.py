# Copyright 2024 Steve Nginyo
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from PyDictionary import PyDictionary
import nltk
from nltk.corpus import words
import difflib

class MyClass:
    class_var = 'I am a class variable'  # This is a class variable

    def __init__(self, val):
        self.alarm = val  

# Open the JSON file
with open('my_json.json') as file:
    # Load JSON data from file into a Python dictionary
    dict_data = json.load(file)

print(dict_data)

for user in dict_data:
    print(user['lname'])




def get_definition(word):
    try:
        # Try to find the words corpus
        nltk.data.find('corpora/words')
    except LookupError:
        # If the words corpus is not found, download it
        nltk.download('words')

    # Create a set of English words
    english_words = set(words.words())

    word = word.lower()  # Convert to lower case
    if word in english_words:
        # If the word is in the dictionary, return a placeholder definition
        # In a real application, you would look up the actual definition here
        return f"The definition of {word} goes here."
    else:
        # If the word is not in the dictionary, suggest a correct spelling
        close_matches = difflib.get_close_matches(word, english_words)
        if close_matches:
            return f"Did you mean {close_matches[0]}?"
        else:
            return "Word not found and no close matches could be found."

# Example usage:
try:
    print(get_definition("exmple"))  # Outputs: Did you mean example?
    print(get_definition("example"))  # Outputs: The definition of example goes here.
except Exception as e:
    print(f"An error occurred: {e}")


def get_definition(word):
    dictionary = PyDictionary()
    try: 
        mymain = dictionary.meaning(word)
        return mymain
    except Exception as e:
        # print(e)
        return "Error"

# Example usage:
mydef = get_definition(input("Write a word \n"))

if(mydef == "Error"):
    print("Word not found")
else:
    print(mydef)

