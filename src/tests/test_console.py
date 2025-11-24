import unittest
import bibtex
import console

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.biblio = bibtex.Bibtex()
        self.konsoli = console.Console(self.biblio, ["foo"])

    def test_add_new_source(self):
        self.konsoli.ask_new_source()

    def test_add_already_exisiting_key(self):
        self.konsoli.ask_new_source()

    def test_add_empty_key(self):
        self.konsoli.ask_new_source()

    def test_add_empty_author(self):
        self.konsoli.ask_new_source()
