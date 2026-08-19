# todo 1 . create dict in format:
# {"a":"alpha" , "b":"beta" }

# todo 2 : create a list of phonetic code words from a word that user inputs.

import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
# {new_key:new_value for (index,row) in data.iterrows()}
phonetic_dict = {row.letter:row.code for(index,row) in data.iterrows()}
print(phonetic_dict)

word=input("Enter a word:").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)