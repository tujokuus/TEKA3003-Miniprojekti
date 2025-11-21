'''
DOC
'''

import sys
import bibtex

if __name__ == "__main__":
    # Parse arguments
    if len(sys.argv) <= 1:
        print(f"Usage: {sys.argv[0]} <file.bib>")
        sys.exit(1)
    filename = sys.argv[1]

    # Attempt to load bibtex from provided file
    bib = bibtex.Bibtex()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            bib_string = file.read()
            bib.read(bib_string)
            print("Warning: provided bibtex file not found, generating one when saved")
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

    # Print bib contents
    print(bib)

    # Save bibtex (a.k.a database) to file
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(bib))
    except IOError:
        print("Could not save file!")
        sys.exit(1)
