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

    def lisaa_syote(self, teksti):
        self.inputs.append(teksti)


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.bib = bibtex.Bibtex()
        entry = bibtex.Entry("foo", "article")
        entry.add_value("title", "Testi artikkeli")
        self.bib.add(entry)

    def test_add_new_source(self):
        stubio = StubIO(["baa", "Wise works by Luke", "Y"])
        konsoli = console.Console(self.bib, stubio)
        konsoli.ask_new_source()
        #Testaamme että lähteen liittämis tapahtuma sujuu halutulla tavalla
        #Onko saaduissa konsoli outputeissa tallenetaan
        self.assertIn("Tallennetaan lähde", stubio.outputs)

    def test_add_already_exisiting_key(self):
        #Testiohjelma suuttuu jos inputit "jäävät kesken", täten
        #lisäämme oikean arvon ja suoritamme lisäystapahtuman loppuun
        #virheellisen syötön annon jälkeen
        stubio = StubIO(["foo", "baa", "Wise works by Luke", "Y"])
        konsoli = console.Console(self.bib, stubio)
        konsoli.ask_new_source()

        self.assertTrue(
            any("Syotetty avain on jo olemassa, lisää parempi" in out for out in stubio.outputs)
        )

    def test_add_empty_key(self):
        stubio = StubIO(["", "baa", "Wise works by Luke", "Y"])
        konsoli = console.Console(self.bib, stubio)
        konsoli.ask_new_source()

        self.assertTrue(
            any("Syotetty avain on tyhjä, lisää parempi" in out for out in stubio.outputs)
        )

    def test_add_empty_title(self):
        stubio = StubIO(["bar", "", "Wise works by Luke", "Y"])
        konsoli = console.Console(self.bib, stubio)
        konsoli.ask_new_source()

        self.assertTrue(
            any("Syotetty nimi on tyhjä, lisää parempi" in out for out in stubio.outputs),
        )