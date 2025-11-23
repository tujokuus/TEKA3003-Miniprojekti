import bibtex

#Console olio kysyy käyttäjältä syötettävän lähteen tiedot, tallentaa ne dict olioon, ja lähettää ne bibtex oliolle
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
            src_key = ask_key()
            src_title = ask_title()

            #Sijoitetaan lähteen tiedot dict olioon
            lahde = {
                "key":          src_key,
                "title":        src_nimi,
                "auhtor":       src_author,
                "date":         src_date,
                "book_title":   src_bookTitle,
                "volume":       src_volume,
                "pages":        src_pages,
                "publisher":    src_publisher,
                "DOI":          src_doi
            }

            #Kysymme käyttäjältä, onko hän varma, että annetut arvot ovat oikein
            print("Olemme lisäämässä seuraavan lähteen, onko se oikein?")
            print(lahde)
            confirmation = input('[Y/N]')
            if confirmation.strip().upper() == "Y":
                epavarma = False

        #Viedään hyvaksytty dict olio tallennettavaksi bibtex oliolle
        print("Tallennetaan lähde")
        #self.bib.add(lahde)


    #Kysytään ja tarkistetaan annettava avain lähteelle
    #REQUIRED
    def ask_key():
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
    def ask_title():
        invalid = True

        while(invalid):
            print("Lisaa lähteen nimi: ")
            src_key = input('=> ')

            if src_key.strip() == "":
                print("Syotetty nimi on tyhjä, lisää parempi")
            else:
                invalid = False      

        return src_title