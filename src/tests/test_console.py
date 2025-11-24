import unittest
import bibtex
import console

class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def lue(self, _teksti):
        return self.inputs.pop(0)

    def kirjoita(self, teksti):
        self.outputs.append(teksti)


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.bib = bibtex.Bibtex()

    def test_add_new_source(self):
        stubio = StubIO(["baa", "Wise works by Luke", "Y"])
        konsoli = console.Console(self.bib, ["foo"], stubio)
        konsoli.ask_new_source()
        #Testaamme että lähteen liittämis tapahtuma sujuu halutulla tavalla
        #Onko saaduissa konsoli outputeissa tallenetaan
        self.assertIn("Tallennetaan lähde", stubio.outputs)

    # def test_add_already_exisiting_key(self):
    #     self.konsoli.ask_new_source()

    # def test_add_empty_key(self):
    #     self.konsoli.ask_new_source()

    # def test_add_empty_author(self):
    #     self.konsoli.ask_new_source()
