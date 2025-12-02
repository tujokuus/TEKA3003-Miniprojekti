import bibtex

#Tätä luokkaa käytetään tunnistamaan testeissä olion kirjoittamaa/syöttämää tekstiä
class KonsoliIO:
    def lue(self, teksti):
        return input(teksti)

    def kirjoita(self, teksti):
        print(teksti)


class Console:
    """ Console olio kysyy ja suorittaa käyttäjältä haluttavia toimintoja """

    def __init__(self, bib_olio, konsoli_io, formaatit):
        self.bib = bib_olio
        #Olio sisältää pakolliset atrbituutit eri lähde tyypeille
        self.forms = formaatit
        #Tarvitsemme listan jo olemassa olevista lähteistä,
        # jotta voimme vertailla niitä uuteen lisättävään (esim. samannimiset avaimet)
        self.konsoli_io = konsoli_io

    #Käydään läpi käsiteltävän lähteen kaikki pakolliset tietokentät,
    # katsotaan jos niissä on jo jotakin ja ilmoitetaan se käyttäjälle
    #Käyttäjä EI VOI poistaa/jättää tyhjäksi atribuuttia, mutta voi skipata
    #Käyttäjä voi  poistua välittömästi muokkauksesta painamalla 'q' näppäntä
    def __edit_required(self, lahde, required, poistutaan):
        pass
            

    #Käydään läpi käsiteltävän lähteen kaikki tietokentät, jotka eivät ole required listassa
    # katsotaan jos niissä on jo jotakin ja ilmoitetaan se käyttäjälle
    #Käyttäjä VOI poistaa/jättää tyhjäksi atribuutin valitsemalla 'd', ja voi skipata muokkauksen '' arvolla
    #Käyttäjä voi  poistua välittömästi muokkauksesta painamalla 'q' näppäntä
    def __edit_extras(self, lahde, required, all_fields, poistutaan):
        pass

    #Kysyy käyttäjältä mitä hän haluaa tehdä, ja ohjataan sen mukaiseen aliohjelmaan
    def activate(self):
        """ Aktivoi konsolin, käyttäjä ohjataan 'main menuun' """
        self.konsoli_io.kirjoita("Tervetuloa 'Bib tiedosto lukijaan', mitä tehtäisiin?")

        active = True
        while active:
            self.konsoli_io.kirjoita("Vaihtoehtona ovat: ")
            self.konsoli_io.kirjoita("'A' lisää uusi lähde, ")
            self.konsoli_io.kirjoita("'B' muokataan/poistetaan olemassa olevaa lähdetta, ")
            self.konsoli_io.kirjoita("'C' järjestetään lähteet atribuutin mukaan, ")
            self.konsoli_io.kirjoita("'Q' poistutaan sovelluksesta. ")
            confirmation = self.konsoli_io.lue('=>')

            if confirmation.strip().upper() == "A":
                self.ask_new_source()
            elif confirmation.strip().upper() == "B":
                self.edit_source()
            elif confirmation.strip().upper() == "C":
                self.sort_sources()
            elif confirmation.strip().upper() == "Q":
                self.konsoli_io.kirjoita("Kiitoksia käytöstä")
                active = False
            else:
                self.konsoli_io.kirjoita("Antamaanne käskyä ei tunnistettu, antakaa se uudestaan")

    #Kysytään uusi lähde (tällä hetkellä automaattisesti article)
    def ask_new_source(self):
        """ Käyttäjältä kysytään uuden lisättävän lähteen tiedot """
        epavarma = True
        tyyppi = ""
        required = []
        optional = []

        while epavarma:
            self.konsoli_io.kirjoita("Kirjoita lähteen luokka:")
            tyyppi = self.konsoli_io.lue('=>').strip().lower()
            self.konsoli_io.kirjoita(f"Valittuna luokkana: {tyyppi}")
            required = self.forms.get_required(tyyppi)
            if required is None:
                self.konsoli_io.kirjoita("Luokkaa ei tunnistettu, lisätäänkö se kuitenkin?")
                confirmation = self.konsoli_io.lue('[Y/N]')
                if confirmation.strip().upper() == "Y":
                    epavarma = False
            else:
                optional = self.forms.get_optional(tyyppi)
                epavarma = False

        self.__form_source(tyyppi, required, optional)

    def __form_source(self, tyyppi, required, optional):
        epavarma = True

        while epavarma:
            #Alustetaan lähteen tiedot
            tiedot = [] # [{"key_value": "key_information"}]

            #Kysytään käyttäjältä konsolissa lähteen tiedot
            self.konsoli_io.kirjoita(f"Alustetaan uusi {tyyppi}:")
            src_key = self.__ask_key()
            for field in required:
                src_value = self.__ask_required(field)
                tiedot.append(src_value)
            for field in optional:
                src_value = self.__ask_optional(field)
                tiedot.append(src_value)
            lisaa = True
            while lisaa:
                self.konsoli_io.kirjoita("Lisää vapaa arvo? Jätä nimi tyhjäksi jos ei.")
                self.konsoli_io.kirjoita("Atribuutin nimi:")
                src_type = self.konsoli_io.lue('=>')
                if src_type.strip() == "":
                    lisaa = False
                    break
                self.konsoli_io.kirjoita("Atribuutin sisältö:")
                src_value = self.konsoli_io.lue('=>')
                tiedot.append({"type": src_type, "value": src_value})

            #Kysymme käyttäjältä, onko hän varma, että annetut arvot ovat oikein
            self.konsoli_io.kirjoita("Olemme lisäämässä seuraavan lähteen, onko se oikein?")
            for tieto in tiedot:
                if tieto is not None:
                    self.konsoli_io.kirjoita(f"{tieto['type']}: {tieto['value']}")
            confirmation = self.konsoli_io.lue('[Y/N]')
            if confirmation.strip().upper() == "Y":
                epavarma = False

        #Viedään hyvaksytty dict olio tallennettavaksi bibtex oliolle
        self.konsoli_io.kirjoita("Tallennetaan lähde")
        entry = bibtex.Entry(src_key, tyyppi)
        for tieto in tiedot:
            if tieto is not None:
                entry.add_value(tieto['type'], tieto['value'])
        self.bib.add(entry)
        self.konsoli_io.kirjoita(str(entry))


    def update_bib(self, uusi_bib):
        """ Konsolille päivitetään uusi bibtex/tietokanta """
        self.bib = uusi_bib


    #Kysytään ja tarkistetaan annettava avain lähteelle
    #REQUIRED
    def __ask_key(self):
        invalid = True

        while invalid:
            self.konsoli_io.kirjoita("Lisaa lähteen avain: ")
            src_key = self.konsoli_io.lue('=> ')

            duplikaatti = False
            if self.bib.get(src_key):
                duplikaatti = True

            if duplikaatti:
                self.konsoli_io.kirjoita("Syotetty avain on jo olemassa, lisää parempi")
            elif src_key.strip() == "":
                self.konsoli_io.kirjoita("Syotetty avain on tyhjä, lisää parempi")
            else:
                invalid = False

        return src_key


    #Kysytään tarvittava luokan atribuutti, annetaan atribuutin nimi
    #REQUIRED
    def __ask_required(self, tyyppi):
        invalid = True
        palautus = {}

        while invalid:
            self.konsoli_io.kirjoita(f"Lisaa lähteen pakollinen {tyyppi}: ")
            src_value = self.konsoli_io.lue('=> ')

            if src_value.strip() == "":
                self.konsoli_io.kirjoita(f"Syotetty {tyyppi} on tyhjä, lisää parempi")
            else:
                invalid = False

        palautus["type"] = tyyppi
        palautus["value"] = src_value
        return palautus


    #Kysytään ja tarkistetaan annettava lähteen nimi
    def __ask_optional(self, tyyppi):
        palautus = {}

        self.konsoli_io.kirjoita(f"Lisaa lähteen {tyyppi}: ")
        src_value = self.konsoli_io.lue('=> ')
        if src_value.strip() == "":
            return None

        palautus["type"] = tyyppi
        palautus["value"] = src_value
        return palautus


    #Otetaan uusi lähde käsittelyyn ja editoidaan sen arvoja
    #Jos uudeksi arvoksi sijoitetaan tyhjä, se poistetaan
    #Jos avain arvoksi sijoitetaan tyhjä, koko lähde poistetaan
    #Kaikille uusille arvoille suoritetaan oikeustarkastus, lähdettä ei tallenneta jos
    #kaikki REQUIRED kentät ja annetut arvot ole hyväksyttäviä
    #Tehtävänä
    def edit_source(self):
        """ Käyttäjältä kysytään muokattava/poistettava lähde ja sen tiedot """
        loopataan = True

        while loopataan:
            self.konsoli_io.kirjoita("Valitse muokattava/poistettavan lähteen avain.")
            #Listataan valittavan lähteen avaimet ja mahdolliset nimet?
            self.konsoli_io.kirjoita("Tämänhetkiset lähteet:")
            lahteet = self.bib.get_all_entries()    #Saadaan ulos lista entry olioista
            for lahde in lahteet:
                avain = lahde.get_identifier()
                title = lahde.get_value("title")
                if title is not None:
                    self.konsoli_io.kirjoita(f"- Lahde: {avain}; {title}")
                else:
                    self.konsoli_io.kirjoita(f"- Lahde: {avain}")
            syote = self.konsoli_io.lue('=> ').strip()

            for lahde in lahteet:
                if lahde.get_identifier() == syote:
                    self.konsoli_io.kirjoita("Lähde löydetty, aletaan muokkaus/poisto")
                    self.konsoli_io.kirjoita("Atribuutit käydään läpi yksi kerrallaan,")
                    self.konsoli_io.kirjoita("Paina enter skipataksesi atribuutin")
                    self.konsoli_io.kirjoita("Paina'd' symboli poistaaksesi atribuutin")
                    self.konsoli_io.kirjoita("Paina'q' symboli poitsuaksesi muokkauksesta")
                    self.konsoli_io.kirjoita("HUOMIO: Jos poistat key arvon, poistat koko lähteen!")

                    self.__edit_specific_source(lahde)

                    return

            self.konsoli_io.kirjoita("Annetulla avaimella ei löydetty lähdettä, yritä uudestaan")

    def __edit_specific_source(self, lahde):
        """ Editoidaan tiettyä lähdettä """
        old_key = lahde.get_identifier()
        new_key = old_key

        #Kysytään uusi avainarvo, vai poistetaanko koko lähde
        invalid = True
        while invalid:
            self.konsoli_io.kirjoita(f"Muokataan avainta: {old_key}")
            src_value = self.konsoli_io.lue('=> ').strip().upper()

            if src_value == "":
                break
            if src_value== "D":
                self.konsoli_io.kirjoita(f"Lähde '{old_key}' poistettu")
                self.bib.remove(old_key)
                return
            elif src_value == "Q":
                return
            elif any(
                e.get_identifier().lower() == src_value.lower()
                for e in self.bib.get_all_entries()
            ):
                self.konsoli_io.kirjoita("Samanarvoinen avain on jo olemassa, lisää parempi.")
            else:
                new_key = src_value
                lahde.set_identifier(new_key)
                invalid = False

        tyyppi = lahde.get_ref_type()
        required = self.forms.get_required(tyyppi)
        all_fields = lahde.get_value_types()

        poistutaan = False
        self.__edit_required(lahde, required, poistutaan)
        if poistutaan:
            return
        self.__edit_extras(lahde, required, all_fields, poistutaan)
        if poistutaan:
            return
        lisaa = True
        while lisaa:
            self.konsoli_io.kirjoita("Lisää vapaa arvo? Jätä nimi tyhjäksi jos ei.")
            self.konsoli_io.kirjoita("Atribuutin nimi:")
            src_type = self.konsoli_io.lue('=>')
            if src_type.strip() == "":
                lisaa = False
                break
            self.konsoli_io.kirjoita("Atribuutin sisältö:")
            src_value = self.konsoli_io.lue('=>')
            lahde.add_value(src_type, src_value)

        self.konsoli_io.kirjoita("Tallennetaan uusi muokattu lähde.")
        self.bib.remove(old_key)
        self.bib.add(lahde)


    #Kysytään käyttäjältä lähteen atribuutti ja järjestetään ne sen mukaan
    #Jos lähteellä ei ole annettua atribuuttia, pistetään ne listan perälle muuttamatta?
    def sort_sources(self):
        """ Käyttäjä suorittaa lähteiden järjestämisen """
        self.konsoli_io.kirjoita("Anna attribuutti, jonka mukaan järjestetään,")
        self.konsoli_io.kirjoita("esim. title, author, year:")
        attr = self.konsoli_io.lue("=> ").strip()

        # jos käyttäjä syöttää tyhjän, ei järjestetä
        if attr == "":
            self.konsoli_io.kirjoita("Atribuutti ei voi olla tyhjä.")
            return

        # tarkistetaan, löytyykö attribuuttia yhtään
        if all(entry.get_value(attr) is None for entry in self.bib.get_all_entries()):
            self.konsoli_io.kirjoita(f"Atribuuttia '{attr}' ei löydy yhdeltäkään lähteeltä.")
            return

        self.konsoli_io.kirjoita("Järjestetäänkö laskevasti?")
        order = self.konsoli_io.lue("[Y/N]").strip().upper()
        desc = order == "Y"

        # Käytetään bibtex-luokan sort-metodia
        sorted_entries = self.bib.sort(attr, desc)

        self.konsoli_io.kirjoita(f"Lähteet järjestetty attribuutin '{attr}' mukaan:")
        self.konsoli_io.kirjoita("")

        if not sorted_entries:
            self.konsoli_io.kirjoita("Ei yhtään lähdettä.")
            return

        for entry in sorted_entries:
            self.konsoli_io.kirjoita(str(entry))
