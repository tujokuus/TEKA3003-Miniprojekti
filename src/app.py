class App: # pylint: disable=too-few-public-methods
    def __init__(self, console):
        self._console = console

    def run(self):
        # Aktivoidaan konsoli (kysytään käyttäjältä uusi tiedosto)
        self._console.activate()
