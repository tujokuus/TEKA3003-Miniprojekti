'''
DOC
'''

import bibtex

if __name__ == "__main__":
    bib = bibtex.Bibtex("testi.bib")

    entry = bibtex.Entry("testid", "article")
    entry.add_value("author", "matti nykänen")
    entry.add_value("title", "emt")
    entry.add_value("year", "1990")
    entry.add_value("journal", "American Educator")
    bib.add(entry)

    entry2 = bibtex.Entry("toinenTestid", "article")
    entry2.add_value("author", "Jyrki")
    entry2.add_value("title", "toinen emt")
    entry2.add_value("year", "2007")
    entry2.add_value("journal", "Iltalehti")
    bib.add(entry2)

    print(str(bib))
    bib.save()
