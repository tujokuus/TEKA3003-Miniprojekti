'''
DOC
'''

import bibtex

if __name__ == "__main__":
    entry = bibtex.Entry("testid", "article")
    entry.add_value("authror", "matti nykänen")
    entry.add_value("title", "emt")
    entry.add_value("year", "1990")
    entry.add_value("journal", "American Educator")

    bib = bibtex.Bibtex("testi.bib")
    bib.add(entry)
    bib.save()

    for a in bib:
        print(str(a))
