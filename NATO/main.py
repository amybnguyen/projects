import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for letter, row in data.iterrows()}
# print(nato_dict)

user_input = input("Enter your word: ").upper()
nato_list = [nato_dict[n] for n in user_input]
print(nato_list)
