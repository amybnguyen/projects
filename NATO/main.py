import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for letter, row in data.iterrows()}
# print(nato_dict)


def generate_phonetic():
    user_input = input("Enter your word: ").upper()
    try:
        nato_list = [nato_dict[n] for n in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_list)


generate_phonetic()
