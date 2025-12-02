from tests.test_console import StubIO
from bibtex import Bibtex, Fields
from console import Console
from app import App


class AppLibrary:
    def __init__(self):
        self._io = StubIO([])
        self._bib = Bibtex()
        self._fields = Fields()
        self._console = Console(self._bib, self._io, self._fields)
        self._app = App(self._console)

    def input(self, value):
        self._io.lisaa_syote(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def run_application(self):
        self._app.run()
