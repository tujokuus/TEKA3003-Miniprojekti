import unittest
import bibtex
import console

class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def lue(self, _teksti):
        try:
            i = self.inputs.pop(0)
        except IndexError as exc:
            print("StubIO: no available input left")
            raise exc
        print(f"StubIO: read {i}")
        return i

    def kirjoita(self, teksti):
        print(f"StubIO: write {teksti}")
        self.outputs.append(teksti)

    def lisaa_syote(self, teksti):
        print(f"StubIO: input {teksti}")
        self.inputs.append(teksti)


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.bib = bibtex.Bibtex()
        entry = bibtex.Entry("foo", "article")
        entry.add_value("title", "Testi artikkeli")
        self.bib.add(entry)
        self.json = bibtex.Fields()

        class FakeForms:
            def get_required(self):
                return ["title"]
            def get_optional(self):
                return ["author"]

        self.forms = FakeForms()

    def test_add_new_source(self):
        stubio = StubIO(["book", "baa", "Luukas", "Wise works by Luke", "JYU", "2025",
         "", "", "", "", "", "", "", "", "", "Y"])
        konsoli = console.Console(self.bib, stubio, self.json)
        konsoli.ask_new_source()
        #Testaamme että lähteen liittämis tapahtuma sujuu halutulla tavalla
        #Onko saaduissa konsoli outputeissa tallenetaan
        self.assertIn("Tallennetaan lähde", stubio.outputs)

    def test_add_already_exisiting_key(self):
        #Testiohjelma suuttuu jos inputit "jäävät kesken", täten
        #lisäämme oikean arvon ja suoritamme lisäystapahtuman loppuun
        #virheellisen syötön annon jälkeen
        stubio = StubIO(["book", "foo", "baa", "Luukas", "JYU", "Wise works by Luke", "2025",
         "", "", "", "", "", "", "", "", "", "Y"])
        konsoli = console.Console(self.bib, stubio, self.json)
        konsoli.ask_new_source()

        self.assertTrue(
            any("Syotetty avain on jo olemassa, lisää parempi" in out for out in stubio.outputs)
        )

    def test_add_empty_key(self):
        stubio = StubIO(["book", "", "baa", "Luukas", "JYU", "Wise works by Luke", "2025",
         "", "", "", "", "", "", "", "", "", "Y"])
        konsoli = console.Console(self.bib, stubio, self.json)
        konsoli.ask_new_source()

        self.assertTrue(
            any("Syotetty avain on tyhjä, lisää parempi" in out for out in stubio.outputs)
        )

    def test_add_empty_title(self):
        stubio = StubIO(["book", "baa", "Luukas", "JYU", "","Wise works by Luke" , "2025",
         "", "", "", "", "", "", "", "", "", "Y"])
        konsoli = console.Console(self.bib, stubio, self.json)
        konsoli.ask_new_source()

        self.assertTrue(
            any("Syotetty title on tyhjä, lisää parempi" in out for out in stubio.outputs),
        )

    def test_activate_console_and_leave(self):
        stubio = StubIO(["Q"])
        konsoli = console.Console(self.bib, stubio, self.json)
        konsoli.activate()

        self.assertTrue(
            any("Kiitoksia käytöstä" in out for out in stubio.outputs),
        )

    def test_add_unknown_input(self):
        stubio = StubIO(["jasdjaklsdjakldjkaljdskal", "Q"])
        konsoli = console.Console(self.bib, stubio, self.json)
        konsoli.activate()

        lause = "Antamaanne käskyä ei tunnistettu, antakaa se uudestaan"
        self.assertTrue(
            any(lause in out for out in stubio.outputs),
        )

    def test_add_new_source_from_main(self):
        stubio = StubIO(["A", "book", "", "baa", "Luukas", "JYU", "Wise works by Luke", "2025",
         "", "", "", "", "", "", "", "", "", "Y", "Q"])
        konsoli = console.Console(self.bib, stubio, self.json)
        konsoli.activate()

        self.assertTrue(
            any("Tallennetaan lähde" in out for out in stubio.outputs),
        )

    def test_sort_empty_attribute(self):
        stubio = StubIO([""])  # käyttäjä syöttää tyhjän attribuutin
        konsoli = console.Console(self.bib, stubio, self.json)
        konsoli.sort_sources()

        self.assertTrue(
            any("Atribuutti ei voi olla tyhjä." in out for out in stubio.outputs)
        )

    def test_sort_by_title(self):
        # syötetään attribuutti "title" ja järjestys "N" (asc)
        stubio = StubIO(["title", "N"])
        konsoli = console.Console(self.bib, stubio, self.json)
        konsoli.sort_sources()

        # tarkistaa että järjestäminen käynnistyi
        self.assertTrue(
            any("Lähteet järjestetty attribuutin 'title' mukaan:" in out for out in stubio.outputs)
        )

        # tarkistaa että tulostettiin olemassa oleva entry
        self.assertTrue(
            any("Testi artikkeli" in out for out in stubio.outputs)
        )

    def test_sort_from_main_menu(self):
        # C = sort, annetaan attribuutti title, järjestys N (asc), lopuksi Q
        stubio = StubIO(["C", "title", "N", "Q"])
        konsoli = console.Console(self.bib, stubio, self.json)
        konsoli.activate()

        self.assertTrue(
            any("Lähteet järjestetty attribuutin 'title' mukaan:" in out
                for out in stubio.outputs)
        )

    def test_sort_descending(self):
        # luodaan toinen entry, jonka title alkaa "Z"
        second = bibtex.Entry("bar", "article")
        second.add_value("title", "Z-title")
        self.bib.add(second)

        stubio = StubIO(["title", "Y"])  # laskeva järjestys

        konsoli = console.Console(self.bib, stubio, self.json)
        konsoli.sort_sources()

        # tarkistetaan että Z-title tulostui ennen Testi artikkeli
        outputs = "\n".join(stubio.outputs)
        self.assertLess(outputs.index("Z-title"), outputs.index("Testi artikkeli"))


    def test_sort_invalid_attribute(self):
        # luodaan testibib
        e1 = bibtex.Entry("testi1", "article")
        e1.add_value("title", "Testi artikkeli")
        self.bib.add(e1)
        e2 = bibtex.Entry("testi2", "article")
        e2.add_value("author", "Author2")
        self.bib.add(e2)

        # StubIO: syötetään attribuutti, jota ei ole olemassa
        stubio = StubIO(["not_a_field"])

        konsoli = console.Console(self.bib, stubio, self.json)
        konsoli.sort_sources()

        # tarkistetaan että tulostuu virheilmoitus attribuutista, jota ei löydy
        outputs = "\n".join(stubio.outputs)
        self.assertIn("Atribuuttia 'not_a_field' ei löydy yhdeltäkään lähteeltä.", outputs)

    def test_remove_source(self):
        """ Testataan lähteen poisto """
        # syötteet: valitaan 'testi1', painetaan 'D' poistaakseen
        stubio = StubIO(["foo", "D"])
        konsoli = console.Console(self.bib, stubio, self.forms)
        konsoli.edit_source()

        self.assertIsNone(self.bib.get("foo"))
        outputs = "\n".join(stubio.outputs)
        self.assertIn("Lähde 'foo' poistettu", outputs)

    def test_search_sources(self):

        stubio = StubIO(["title","Testi"])
        konsoli = console.Console(self.bib, stubio, self.json)
        konsoli.search_sources()

        self.assertTrue(
            any("Löydettiin 1 lähdettä:" in out for out in stubio.outputs)
        )

        self.assertTrue(
            any("Testi artikkeli" in out for out in stubio.outputs)
        )
