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

    def test_add_already_exisiting_key(self):
        stubio = StubIO(["baa", "foo", "Wise works by Luke", "Y"])
        konsoli = console.Console(self.bib, ["baa"], stubio)
        konsoli.ask_new_source()

        self.assertTrue(
            any("Syotetty avain on jo olemassa, lisää parempi" in out for out in stubio.outputs)
        )

    def test_add_empty_key(self):
        stubio = StubIO(["", "foo", "Wise works by Luke", "Y"])
        konsoli = console.Console(self.bib, ["baa"], stubio)
        konsoli.ask_new_source()

        self.assertTrue(
            any("Syotetty avain on tyhjä, lisää parempi" in out for out in stubio.outputs)
        )

    def test_add_empty_title(self):
        stubio = StubIO(["bar", "", "Wise works", "Y"])
        konsoli = console.Console(self.bib, ["foo"], stubio)
        konsoli.ask_new_source()

        self.assertTrue(
            any("Syotetty nimi on tyhjä, lisää parempi" in out for out in stubio.outputs),
        )