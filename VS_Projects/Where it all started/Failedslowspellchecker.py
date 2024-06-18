
import contextlib
from spellchecker import SpellChecker

spell = SpellChecker()

def load(filename):
    for encoding in ["utf-8", "latin-1", "windows-1252"]:
        with contextlib.suppress(UnicodeDecodeError):
            with open(filename, 'r', encoding=encoding) as file:
                all_lines = file.readlines()
                for line in all_lines:
                    corrected_word = spell.correction(line)
                    if corrected_word == "i":  # Check if correction exists
                        print()
                    elif corrected_word is not None:  # Check if correction exists
                        print(f"{corrected_word}")
                    else:
                        print(line)
        print(f"Error: Unable to decode file '{filename}' with common encodings.")
        return  # Exit after trying all encodings

load('A_Courier_For_Kivotos.txt')
