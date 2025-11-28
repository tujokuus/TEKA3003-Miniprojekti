'''
Main for our reference helper
'''

import sys
import json
import bibtex
import console


if __name__ == "__main__":

    # Read reference types from refs.json file
    try:
        with open('refs.json', 'r',encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: file 'refs.json' not found.")
    json = bibtex.Fields(data['Reference_types'])

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
    except FileNotFoundError:
        print("Warning: provided bibtex file not found, generating one when saved")

    # Print bib contents
    print(bib)

    #Aktivoidaan konsoli (kysytään käyttäjältä uusi tiedosto)
    konsoli = console.Console(bib , console.KonsoliIO())
    konsoli.ask_new_source()

    # Save bibtex (a.k.a database) to file
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(bib))
    except IOError:
        print("Could not save file!")
        sys.exit(1)
