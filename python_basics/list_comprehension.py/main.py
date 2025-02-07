import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
print(nato_dict) 

user_input = input("Enter a word: ")
alphabet = [letter.upper() for letter in user_input]
phonetic_list = [nato_dict[letter] for letter in alphabet if letter in nato_dict]

# for letter in alphabet:
#     if letter in nato_dict:
#         phonetic_list.append(nato_dict[letter])

print(phonetic_list)
