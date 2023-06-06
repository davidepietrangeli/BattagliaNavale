# Definizione della Classe 'Nave' che rappresenta una nave all'interno del gioco
class Nave:
    def __init__(self, lunghezza, orientamento, colonna_partenza, riga_partenza, coordinate=None):
        self.lunghezza = lunghezza  # numero di celle occupate dalla nave sul campo di gioco
        self.orientamento = orientamento  # orientamento della nave che può essere "orizzontale" o "verticale"
        self.colonna_partenza = colonna_partenza
        self.riga_partenza = riga_partenza
        self.colpita = 0

        if coordinate is None:
            self.coordinate = []
        else:
            self.coordinate = coordinate

    # Metodo che controlla se la nave è affondata
    def nave_affondata(self):
        if self.colpita == self.lunghezza:
            return True
        else:
            return False

    # Metodo che controlla se la nave è colpita
    def nave_colpita(self, riga_sparo, colonna_sparo):
        if self.colpo(riga_sparo, colonna_sparo):
            self.coordinate.remove([riga_sparo, colonna_sparo])
            self.colpita += 1
            return True
        return False

    # Metodo che controlla il colpo
    def colpo(self, riga_sparo, colonna_sparo):
        if [riga_sparo, colonna_sparo] in self.coordinate:
            return True
        return False


# Definizione di sottoclassi
class Portaerei(Nave):
    def __init__(self, orientamento, colonna_partenza, riga_partenza, coordinate):
        super().__init__(5, orientamento, colonna_partenza, riga_partenza, coordinate)


class Corazzata(Nave):
    def __init__(self, orientamento, colonna_partenza, riga_partenza, coordinate):
        super().__init__(4, orientamento, colonna_partenza, riga_partenza, coordinate)


class Sottomarino(Nave):
    def __init__(self, orientamento, colonna_partenza, riga_partenza, coordinate):
        super().__init__(3, orientamento, colonna_partenza, riga_partenza, coordinate)


class Cacciatorpediniere(Nave):
    def __init__(self, orientamento, colonna_partenza, riga_partenza, coordinate):
        super().__init__(2, orientamento, colonna_partenza, riga_partenza, coordinate)


class Sommergibile(Nave):
    def __init__(self, orientamento, colonna_partenza, riga_partenza, coordinate):
        super().__init__(1, orientamento, colonna_partenza, riga_partenza, coordinate)
