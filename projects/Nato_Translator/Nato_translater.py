import pandas as pd
import os

def nato_alphabet_translater():
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    # Construct the full path to the CSV file
    csv_path = os.path.join(script_dir, 'nato_phonetic_alphabet.csv')
    
    # Read the CSV file
    nato_df = pd.read_csv(csv_path)
    
    # Create the dictionary
    dictionary1 = {row['letter']: row['code'] for (index, row) in nato_df.iterrows()}
    
    # Get user input
    inp = input('What is your name?\n').strip().upper()
    
    # Translate the input to the NATO phonetic alphabet
    translated_name = [dictionary1[letter] for letter in inp]
    
    # Print the translated name
    print(translated_name)

def __main__():
    nato_alphabet_translater()

if __name__ == '__main__':
    __main__()
