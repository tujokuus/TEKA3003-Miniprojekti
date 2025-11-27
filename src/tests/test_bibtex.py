import unittest
import bibtex

# bib = bibtex.Bibtex()

# entry = bibtex.Entry("testid", "article")
# entry.add_value("author", "matti nykänen")
# entry.add_value("title", "emt")
# entry.add_value("year", "1990")
# entry.add_value("journal", "American Educator")
# bib.add(entry)

# entry2 = bibtex.Entry("toinenTestid", "article")
# entry2.add_value("author", "Jyrki")
# entry2.add_value("title", "toinen emt")
# entry2.add_value("year", "2007")
# entry2.add_value("journal", "Iltalehti")
# bib.add(entry2)

# print(str(bib))

class TestBibtex(unittest.TestCase):
    def setUp(self):
        pass

    def test_open_bib(self):
        bib_content = """@article{toinenTestid,
    author = {Jyrki},
    title = {toinen emt},
    year = {2007},
    journal = {Iltalehti}
}

@article{testid,
    author = {matti nykänen},
    title = {emt},
    year = {1990},
    journal = {American Educator},
    hyehee = {testidataa}
}
"""
        bib = bibtex.Bibtex()
        bib.read(bib_content)
        entry = bib.get("testid")
        self.assertIsNotNone(entry)
        self.assertEqual(entry.get_value("author"), "matti nykänen")

    def test_save_bib(self):
        bib = bibtex.Bibtex()
        entry = bibtex.Entry("testid", "article")
        entry.add_value("author", "matti nykänen")
        entry.add_value("title", "emt")
        entry.add_value("year", "1990")
        entry.add_value("journal", "American Educator")
        bib.add(entry)
        bib_content = str(bib)
        self.assertEqual(bib_content, """@article{testid,
    author = {matti nykänen},
    title = {emt},
    year = {1990},
    journal = {American Educator}
}""")
        
    def test_search(self):
        bib_content = """@article{toinenTestid,
    author = {Jyrki},
    title = {toinen emt},
    year = {2007},
    journal = {Iltalehti}
}

@article{testid,
    author = {matti nykänen},
    title = {testidataa},
    year = {1990},
    journal = {American Educator},
    hyehee = {emt}
}
"""
        bib = bibtex.Bibtex()
        bib.read(bib_content)
        self.assertEqual(bib.search("matti")[0].get_identifier(), "testid")
        self.assertEqual(len(bib.search("emt")), 2)
        self.assertEqual(len(bib.search("emt", "title")), 1)
    
