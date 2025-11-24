import bibtex

#Tätä luokkaa käytetään tunnistamaan testeissä olion kirjoittamaa/syöttämää tekstiä
class KonsoliIO:
    def lue(self, teksti):
        return input(teksti)

    def kirjoita(self, teksti):
        print(teksti)

#Console olio kysyy käyttäjältä syötettävän lähteen tiedot,
# tallentaa ne dict olioon, ja lähettää ne bibtex oliolle
#lahdeAvaimet halutaan Array/List muodossa
class Console:
    def __init__(self, bib_olio, lahde_avaimet, konsoli_io):
        self.bib = bib_olio
        #Tarvitsemme listan jo olemassa olevista lähteistä,
        # jotta voimme vertailla niitä uuteen lisättävään (esim. samannimiset avaimet)
        self.lahteet = lahde_avaimet
        self.konsoli_io = konsoli_io

    def ask_new_source(self):
        epavarma = True

        while epavarma:
            #Alustetaan lähteen tiedot
            src_key         = ""
            src_title       = ""
            #src_author      = ""
            #src_date        = ""
            #src_bookTitle   = ""
            #src_volume      = 0
            #src_pages       = ""
            #src_publisher   = ""
            #src_doi         = ""

            #Kysytään käyttäjältä konsolissa lähteen tiedot
            self.konsoli_io.kirjoita("Alustetaan uusi artikkeli:")
            src_key = self.__ask_key()
            src_title = self.__ask_title()

            #Kysymme käyttäjältä, onko hän varma, että annetut arvot ovat oikein
            self.konsoli_io.kirjoita("Olemme lisäämässä seuraavan lähteen, onko se oikein?")
            self.konsoli_io.kirjoita(f"key: {src_key}")
            self.konsoli_io.kirjoita(f"title: {src_title}")
            confirmation = self.konsoli_io.lue('[Y/N]')
            if confirmation.strip().upper() == "Y":
                epavarma = False

        #Viedään hyvaksytty dict olio tallennettavaksi bibtex oliolle
        self.konsoli_io.kirjoita("Tallennetaan lähde")
        entry = bibtex.Entry(src_key, "article")
        entry.add_value("title", src_title)
        self.bib.add(entry)
        self.konsoli_io.kirjoita(str(entry))

    #Päivitetään avaimet
    def update_keys(self, uudet_avaimet):
        self.lahteet = uudet_avaimet

    #Kysytään ja tarkistetaan annettava avain lähteelle
    #REQUIRED
    def __ask_key(self):
        invalid = True

        while invalid:
            self.konsoli_io.kirjoita("Lisaa lähteen avain: ")
            src_key = self.konsoli_io.lue('=> ')

            duplikaatti = False
            for lahde in self.lahteet:
                if lahde.strip() == src_key:
                    duplikaatti = True

            if duplikaatti:
                self.konsoli_io.kirjoita("Syotetty avain on jo olemassa, lisää parempi")
            elif src_key.strip() == "":
                self.konsoli_io.kirjoita("Syotetty avain on tyhjä, lisää parempi")
            else:
                invalid = False

        return src_key

    #Kysytään ja tarkistetaan annettava lähteen nimi
    #REQUIRED
    def __ask_title(self):
        invalid = True

        while invalid:
            self.konsoli_io.kirjoita("Lisaa lähteen nimi: ")
            src_title = self.konsoli_io.lue('=> ')

            if src_title.strip() == "":
                self.konsoli_io.kirjoita("Syotetty nimi on tyhjä, lisää parempi")
            else:
                invalid = False

        return src_title
