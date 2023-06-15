# Definizione della Classe 'Nave' che rappresenta una nave all'interno del gioco
class Nave:
    # Creo il costruttore con i relativi parametri:
    def __init__(self, lunghezza, orientamento, colonna_partenza, riga_partenza, coordinate=None):
        self.lunghezza = lunghezza  # un intero che rappresenta il numero di celle occupate dalla nave sul campo di gioco
        self.orientamento = orientamento  # una stringa che indica l'orientamento della nave che può essere "orizzontale" o "verticale"
        self.colonna_partenza = colonna_partenza  # un intero che rappresenta la colonna di partenza della nave sul campo di gioco
        self.riga_partenza = riga_partenza  # un intero che rappresenta la riga di partenza della nave sul campo di gioco
        # Tengo traccia del numero di volte che una nave viene colpita
        self.colpita = 0
        self.coordinate = coordinate

    # Metodo che controlla se la nave è affondata
    def nave_affondata(self):
        # Restituisco True se la nave è stata colpita un numero di volte uguale alla sua lunghezza
        if self.colpita == self.lunghezza:
            return True
        else:
            return False

    # Parametri:
    #   'riga_sparo', 'colonna_sparo': punto dove il colpo viene sparato
    # Metodo che controlla se la nave è colpita
    def nave_colpita(self, riga_sparo, colonna_sparo):
        # Se il colpo colpisce una delle coordinate occupate dalla nave
        if self.colpo(riga_sparo, colonna_sparo):
            # Rimuovo coordinata dalla lista
            self.coordinate.remove([riga_sparo, colonna_sparo])
            # Incremento di uno il conteggio
            self.colpita += 1
            return True
        # Nave non colpita, restituisco False
        return False

    # Parametri:
    #   'riga_sparo', 'colonna_sparo': punto dove il colpo viene sparato
    # Metodo usato internamente al metodo 'nave_colpita' per verificare se la nave è stata effettivamente colpita
    def colpo(self, riga_sparo, colonna_sparo):
        # Vedo se il colpo specifico colpisce una delle coordinate
        if [riga_sparo, colonna_sparo] in self.coordinate:
            return True
        return False


# Definizione di sottoclassi, dove ogni sottoclasse eredita gli attributi e i metodi della classe 'Nave'
# La funzione 'super()' chiama il costruttore della classe genitore 'Nave
class Portaerei(Nave):
    # Sovrascrivo il costruttore della classe genitore 'Nave' con i parametri della 'Portaerei'
    def __init__(self, orientamento, colonna_partenza, riga_partenza, coordinate):
        super().__init__(5, orientamento, colonna_partenza, riga_partenza, coordinate)


class Corazzata(Nave):
    # Sovrascrivo il costruttore della classe genitore 'Nave' con i parametri della 'Corazzata'
    def __init__(self, orientamento, colonna_partenza, riga_partenza, coordinate):
        super().__init__(4, orientamento, colonna_partenza, riga_partenza, coordinate)


class Sottomarino(Nave):
    # Sovrascrivo il costruttore della classe genitore 'Nave' con i parametri della 'Sottomarino'
    def __init__(self, orientamento, colonna_partenza, riga_partenza, coordinate):
        super().__init__(3, orientamento, colonna_partenza, riga_partenza, coordinate)


class Cacciatorpediniere(Nave):
    # Sovrascrivo il costruttore della classe genitore 'Nave' con i parametri della 'Cacciatorpediniere'
    def __init__(self, orientamento, colonna_partenza, riga_partenza, coordinate):
        super().__init__(2, orientamento, colonna_partenza, riga_partenza, coordinate)


class Sommergibile(Nave):
    # Sovrascrivo il costruttore della classe genitore 'Nave' con i parametri della 'Sommergibile'
    def __init__(self, orientamento, colonna_partenza, riga_partenza, coordinate):
        super().__init__(1, orientamento, colonna_partenza, riga_partenza, coordinate)
