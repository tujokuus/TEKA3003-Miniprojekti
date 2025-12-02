'''
Main for our reference helper
'''

import sys
from app import App
from console import Console, KonsoliIO
from bibtex import Bibtex, Fields

if __name__ == "__main__":
    # Parse arguments
    if len(sys.argv) <= 1:
        print(f"Usage: {sys.argv[0]} <file.bib>")
        sys.exit(1)
    filename = sys.argv[1]

    # Attempt to load bibtex from provided file
    bibtex = Bibtex()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            bib_string = file.read()
            bibtex.read(bib_string)
    except FileNotFoundError:
        print("Warning: provided bibtex file not found, generating one when saved")

    io = KonsoliIO()
    formaatit = Fields()
    console = Console(bibtex, io, formaatit)
    app = App(console)
    app.run()

    # Save bibtex (a.k.a database) to file
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(bibtex))
    except IOError:
        print("Could not save file!")
        sys.exit(1)
