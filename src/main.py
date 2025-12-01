from console import Console, KonsoliIO
from bibtex import Bibtex
from app import App

if __name__ == "__main__":
    io = KonsoliIO()
    bibtex = Bibtex()
    console = Console(bibtex, io)
    app = App(console)
    app.run()
