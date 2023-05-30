# Definizione della Classe 'Nave' che rappresenta una nave all'interno del gioco
class Nave:
    def __init__(self, nome, lunghezza, posizione, orientamento):
        self.nome = nome  # nome della nave
        self.lunghezza = lunghezza  # numero di celle occupate dalla nave sul campo di gioco
        self.posizione = posizione  # rappresenta la posizione iniziale della nave sul campo di gioco
        self.orientamento = orientamento  # orientamento della nave che può essere "orizzontale" o "verticale"


# Definizione della Classe 'Posizione' che rappresenta una posizione sul campo di gioco
class Posizione:
    def __init__(self, colonna, riga):
        self.colonna = colonna  # colonna della posizione rappresentata da una lettera maiuscola da 'A' a 'Z'
        self.riga = riga  # la riga della posizione rappresentata da un numero intero

# Queste due classi sono utilizzate per definire le caratteristiche e la posizione delle navi all'interno del gioco.
