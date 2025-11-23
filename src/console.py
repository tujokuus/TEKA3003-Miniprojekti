import bibtex

#Console olio kysyy käyttäjältä syötettävän lähteen tiedot, tallentaa ne dict olioon, ja lähettää ne bibtex oliolle
#lahdeAvaimet halutaan Array/List muodossa
class Console:
    def __init__(self, bibOlio, lahdeAvaimet):
        self.bib = bibOlio
        #Tarvitsemme listan jo olemassa olevista lähteistä, jotta voimme vertailla niitä uuteen lisättävään (esim. samannimiset avaimet)
        self.lahteet = lahdeAvaimet

    def ask_new_source():
        epavarma = True

        while(epavarma):
            #Alustetaan lähteen tiedot
            src_key         = ""
            src_title       = ""
            src_author      = ""
            src_date        = ""
            src_bookTitle   = ""
            src_volume      = 0
            src_pages       = ""
            src_publisher   = ""
            src_doi         = ""

            #Kysytään käyttäjältä konsolissa lähteen tiedot
            print("Alustetaan uusi lähde:")
            src_key = __ask_key()
            src_title = __ask_title()

            #Kysymme käyttäjältä, onko hän varma, että annetut arvot ovat oikein
            print("Olemme lisäämässä seuraavan lähteen, onko se oikein?")
            print("key", src_key)
            print("title", src_title)
            confirmation = input('[Y/N]')
            if confirmation.strip().upper() == "Y":
                epavarma = False

        #Viedään hyvaksytty dict olio tallennettavaksi bibtex oliolle
        print("Tallennetaan lähde")
        entry = bibtex.Entry(src_key, "article")
        entry.add_value("title", src_title)
        #self.bib.add(entry)
        print(str(entry))

    #Kysytään ja tarkistetaan annettava avain lähteelle
    #REQUIRED
    def __ask_key():
        invalid = True

        while(invalid):
            print("Lisaa lähteen avain: ")
            src_key = input('=> ')

            duplikaatti = False
            for lahde in lahdeAvaimet:
                if lahde.strip() == src_key:
                    duplikaatti = True

            if duplikaatti:
                print("Syotetty avain on jo olemassa, lisää parempi")
            elif src_key.strip() == "":
                print("Syotetty avain on tyhjä, lisää parempi")
            else:
                invalid = False

        return src_key

    #Kysytään ja tarkistetaan annettava lähteen nimi
    #REQUIRED
    def __ask_title():
        invalid = True

        while(invalid):
            print("Lisaa lähteen nimi: ")
            src_key = input('=> ')

            if src_key.strip() == "":
                print("Syotetty nimi on tyhjä, lisää parempi")
            else:
                invalid = False      

        return src_title