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

    def test_iteration(self):
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
        a = ""
        for entry in bib:
            a += entry.get_identifier()
        self.assertEqual(a, "toinenTestidtestid")

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
    annote = {emt}
}
"""
        bib = bibtex.Bibtex()
        bib.read(bib_content)
        self.assertEqual(bib.search("matti")[0].get_identifier(), "testid")
        self.assertEqual(len(bib.search("emt")), 2)
        self.assertEqual(len(bib.search("emt", "annote")), 1)

    def test_sort(self):
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

@article{kolmasTestId,
    author = {matti meikäläinen},
    title = {Meikäläisen harkkatyö},
    year = {1995}
}
"""
        bib = bibtex.Bibtex()
        bib.read(bib_content)
        ordered_by_year = bib.sort("year")
        ordered_by_author = bib.sort("author")
        ordered_by_journal = bib.sort("journal")
        ordered_by_journal_desc = bib.sort("journal", desc=True)

        self.assertEqual(ordered_by_year[0].get_value("year"), "1990")
        self.assertEqual(ordered_by_year[2].get_value("year"), "2007")
        self.assertEqual(ordered_by_author[1].get_value("author"), "matti meikäläinen")
        self.assertEqual(ordered_by_author[2].get_value("author"), "matti nykänen")

        # Test for sorting by missing fields always getting sorted to last place
        self.assertEqual(ordered_by_journal[2].get_value("title"), "Meikäläisen harkkatyö")
        self.assertEqual(ordered_by_journal_desc[2].get_value("title"), "Meikäläisen harkkatyö")

    def test_add_valid_acm_link(self):
        acm_link = "https://dl.acm.org/doi/10.1145/2380552.2380613"
        bib = bibtex.Bibtex()
        bib.add_acm_link(acm_link)
        self.assertIn("Three years of design-based research to reform a software engineering curriculum", str(bib))

    def test_add_invalid_acm_link(self):
        bib = bibtex.Bibtex()
        self.assertRaises(FileNotFoundError, lambda: bib.add_acm_link("https://linkkijkl.fi"))
        self.assertRaises(FileNotFoundError, lambda: bib.add_acm_link("https://dl.acm.org/doi?10.1145/2380552.2380613"))
