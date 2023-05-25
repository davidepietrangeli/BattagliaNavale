# Definizione della Classe 'Nave'
class Nave:
    def __init__(self, nome, lunghezza, posizione, orientamento):
        self.nome = nome
        self.lunghezza = lunghezza
        self.posizione = posizione
        self.orientamento = orientamento


# Definizione della Classe 'Posizione'
class Posizione:
    def __init__(self, colonna, riga):
        self.colonna = colonna
        self.riga = riga
