import pandas

def nato_alphabet_translater():
    nato_alph = pandas.read_csv(r'C:\Users\jpnms\Documents\GitHub\nato_phonetic_alphabet.csv')
    nato_df = pandas.DataFrame(nato_alph)
    dictionary1 = {row['letter']:row['code']  for (index,row) in nato_df.iterrows()}
    inp = input('What is your name?\n').strip().upper()
    print([dictionary1[f'{letter}'] for letter in inp])

def __main__():
    nato_alphabet_translater()
if __name__ == '__main__':
    __main__()