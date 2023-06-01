# Definizione della Classe 'Campo' che rappresenta il campo di gioco in cui vengono posizionate le navi
class Campo:
    # Metodo che si occupa di creare la rappresentazione iniziale del campo di gioco come una matrice
    def __init__(self, num_righe, num_colonne):
        self.num_righe = num_righe  # numero delle righe del campo, memorizzato come oggetto della classe Campo
        self.num_colonne = num_colonne  # numero delle colonne del campo, memorizzato come oggetto della classe Campo
        # Richiama il metodo 'crea_campo' per inizializzare il campo di gioco con una matrice vuota
        self.campo = self.crea_campo()
        # Viene inizializzata la lista navi come un elenco vuoto che conterrà le navi posizionate nel campo
        self.navi = []
        # Ogni volta che una nave viene posizionata, viene aggiunta a questa lista. Questa lista può essere utilizzata
        # per verificare lo stato delle navi nel campo, contare il numero di navi rimaste o rimuovere una nave affondata

    # Metodo che restituisce una rappresentazione testuale del campo di gioco
    def crea_campo(self):
        # Viene inizializzata una lista vuota chiamata campo, che conterrà tutte le righe del campo di gioco
        campo = []
        # Viene creata la prima riga del campo, che contiene le lettere delle colonne
        # Viene aggiunto uno spazio vuoto come primo elemento della lista
        riga_superiore = [' '] + [chr(i) for i in range(ord('A'), ord('A') + self.num_colonne)]
        # La lista 'riga_superiore' viene aggiunta come prima riga alla lista 'campo'
        campo.append(riga_superiore)
        # Viene eseguito un ciclo for per ogni riga del campo
        for riga in range(self.num_righe):
            # Il primo elemento della lista è il numero della riga incrementato di uno convertito in stringa
            # Gli altri elementi della lista sono stringhe vuote rappresentanti le caselle vuote del campo
            riga_campo = [str(riga + 1)] + [''] * self.num_colonne
            # La lista 'riga_campo' viene aggiunta alla lista 'campo'
            campo.append(riga_campo)
        #  la lista campo che rappresenta il campo di gioco completo viene restituita come risultato del metodo
        return campo

    # Metodo che viene chiamato senza la creazione di un'istanza dell'oggetto
    def __str__(self):
        # Viene inizializzata una stringa vuota chiamata che conterrà la rappresentazione del campo di gioco
        campo_str = ""
        # Viene calcolata la larghezza massima per ciascuna colonna del campo di gioco
        # Viene creata una lista chiamata 'colonna_widths' che ha la lunghezza max di ogni elemento per ogni colonna
        colonna_widths = [max(len(riga[colonna]) for riga in self.campo) for colonna in range(self.num_colonne + 1)]
        # Viene eseguito un ciclo for per ogni riga nel campo di gioco
        for riga in self.campo:
            campo_str += " ".join(
                f"{riga[colonna]:<{colonna_widths[colonna]}}" for colonna in range(self.num_colonne + 1)) + "\n"
        # la stringa che rappresenta il campo di gioco formattato correttamente viene restituita come risultato
        return campo_str

    @staticmethod
    # Metodo che prende il parametro colonna, che rappresenta un numero intero
    def get_lettera_colonna(colonna):
        # Viene utilizzata la funzione 'chr' per convertire un numero intero in un carattere
        # Viene restituita la lettera ottenuta convertendo il valore in un carattere
        return chr(ord('A') + colonna - 1)
    # Ad esempio, se si passa colonna = 1, il metodo restituirà 'A'

    # Parametri: 'navi': Una lista di oggetti 'Nave' che rappresentano le navi da posizionare nel campo di gioco
    # Metodo per posizionare le navi di un giocatore sul campo di gioco
    def posiziona_navi(self, navi):
        # Griglia vuota rappresentata come una lista di liste, inizializzando ogni elemento con uno spazio vuoto
        griglia = [[' ' for _ in range(self.num_colonne + 1)] for _ in range(self.num_righe + 1)]
        # Inserisce gli indici delle colonne nella prima riga
        griglia[0] = [' '] + [chr(i) for i in range(ord('A'), ord('A') + self.num_colonne)]
        # Inserisce gli indici delle righe nella prima colonna
        for i in range(1, self.num_righe + 1):
            griglia[i][0] = str(i)
        # Per ogni nave presente nella lista navi, ho le informazioni sulla posizione, la lunghezza e l'orientamento
        for nave in navi:
            colonna = ord(nave.posizione.colonna.upper()) - ord('A') + 1
            riga = nave.posizione.riga
            orientamento = nave.orientamento.upper()
            # Se l'orientamento è verticale ("V"), vengono impostati i simboli delle navi nelle celle corrispondenti
            if orientamento == "V":
                for i in range(nave.lunghezza):
                    if riga + i <= self.num_righe:
                        griglia[riga + i][colonna] = nave.nome[0]
            # # Se l'orientamento è orizzontale ("O"), vengono impostati i simboli delle navi nelle celle corrispondenti
            elif orientamento == "O":
                for i in range(nave.lunghezza):
                    if colonna + i <= self.num_colonne:
                        griglia[riga][colonna + i] = nave.nome[0]
        # Infine, la griglia creata viene assegnata all'attributo 'campo' dell'oggetto 'Campo'.
        self.campo = griglia
    # Il metodo modifica lo stato interno dell'oggetto 'Campo' impostando il campo con le posizioni delle navi

    # Metodo che stampa il campo di gioco mostrando la disposizione delle navi e i colpi sparati
    def campo_pieno(self):
        # Itera attraverso ogni riga nella griglia del campo (self.campo)
        for riga in self.campo:
            # Per ogni riga stampa gli elementi separati da uno spazio
            print(" ".join(riga))

    # Parametri: 'riga_sparo': La riga del campo di gioco in cui si desidera sparare
    #            'colonna_sparo': La colonna del campo di gioco in cui si desidera sparare
    # Metodo che analizza la posizione dove viene sparato il colpo
    def colpisci_campo(self, riga_sparo, colonna_sparo):
        # Verifico se c'è una cella vuota, in tal caso la nave non si trova in quella posizione
        if self.campo[riga_sparo][colonna_sparo] == ' ':
            # Segna la cella con 'O' per indicare colpo mancato
            self.campo[riga_sparo][colonna_sparo] = 'O'
            # Restituisce la stringa "Colpo Mancato"
            return "Colpo Mancato"
        else:
            # Altrimenti c'è una nave nella cella e la segno con 'X'
            self.campo[riga_sparo][colonna_sparo] = 'X'
            # Controllo se la nave colpita è affondata richiamando il metodo 'rimuovi_nave_affondata'
            nave_affondata = self.rimuovi_nave_affondata(riga_sparo, colonna_sparo)
            # Se la nave è affondata
            if nave_affondata:
                # Viene aggiornato il campo di gioco chiamando il metodo 'campo_pieno'
                self.campo_pieno()
                # Restituisce una stringa che indica che la nave è stata affondata, fornendo il nome della nave
                return f"Affondato! Hai affondato la nave {nave_affondata.nome}"
            else:
                # La nave è stata colpita ma non affondata
                return "Colpito"
    # Restituisce una stringa che rappresenta l'esito del colpo sparato

    # Parametri: 'riga': La riga del campo di gioco in cui è stato colpito un segmento della nave
    #            'colonna': La colonna del campo di gioco in cui è stato colpito un segmento della nave
    # Metodo che rimuove l'oggetto nave dal campo di gioco quando viene affondata
    def rimuovi_nave_affondata(self, riga, colonna):
        # Iterazione attraverso la lista delle navi presenti sul campo di gioco
        for nave in self.navi:
            # Controllo se il colpo colpisce un segmento della nave sulla stessa riga e nell'intervallo delle colonne
            if (nave.posizione.riga == riga and
                    colonna >= nave.posizione.colonna and
                    colonna < nave.posizione.colonna + nave.lunghezza):
                # Verifico se la nave è affondata
                for c in range(nave.posizione.colonna, nave.posizione.colonna + nave.lunghezza):
                    # Verifico ogni segmento della Nave
                    if (riga, c) not in nave.posizionate:
                        # Restituisco False se c'è ancora una posizione della nave che non è stata colpita
                        return False
                for c in range(nave.posizione.colonna, nave.posizione.colonna + nave.lunghezza):
                    # Se affondata, rimuovo tutti i segmenti della nave e li sostituisco con 'X'
                    self.campo[riga][c] = 'X'
                # Rimuovo la nave della lista delle navi presenti nel campo di gioco
                self.navi.remove(nave)
                # Chiamo il metodo 'campo_pieno' per aggiornare il campo dopo aver rimosso la nave affondata
                self.campo_pieno()
                return nave
        # Restituisco None se non è stata trovata alcuna nave
        return None

    # Parametri: 'colpi_sparati_giocatore1': una lista di posizioni di colpi sparati dal Giocatore 1
    # Metodo che aggiorna il campo di gioco contrassegnando i colpi sparati dal Giocatore 1
    def segno_colpo1(self, colpi_sparati_giocatore1):
        for posizione in colpi_sparati_giocatore1:
            riga, colonna, _ = posizione
            self.colpisci_campo(riga, colonna)

    # Parametri: 'colpi_sparati_giocatore2': una lista di posizioni di colpi sparati dal Giocatore 2
    # Metodo che aggiorna il campo di gioco contrassegnando i colpi sparati dal Giocatore 2
    def segno_colpo2(self, colpi_sparati_giocatore2):
        for posizione in colpi_sparati_giocatore2:
            riga, colonna, _ = posizione
            self.colpisci_campo(riga, colonna)

    # Metodo che stampa il campo di gioco con solo i colpi sparati del Giocatore1
    def campo1_solo_colpi(self, colpi_sparati_giocatore2):
        # Itero attraverso ogni riga nella griglia del campo (self.campo)
        for riga in self.campo:
            # Creo una lista vuota per la riga modificata
            riga_modificata = []
            # Per ogni elemento nella riga
            for elemento in riga:
                # Se l'elemento è 'O' (colpo mancato) o 'X' (colpo su nave), lascio l'elemento invariato
                # Altrimenti, sostituisco l'elemento con uno spazio vuoto
                riga_modificata.append(elemento if elemento in colpi_sparati_giocatore2 else ' ')
            # Stampo gli elementi della riga modificata separati da uno spazio
            print(" ".join(riga_modificata))

    # Metodo che stampa il campo di gioco con solo i colpi sparati del Giocatore2
    def campo2_solo_colpi(self, colpi_sparati_giocatore1):
        # Itero attraverso ogni riga nella griglia del campo (self.campo)
        for riga in self.campo:
            # Creo una lista vuota per la riga modificata
            riga_modificata = []
            # Per ogni elemento nella riga
            for elemento in riga:
                # Se l'elemento è 'O' (colpo mancato) o 'X' (colpo su nave), lascio l'elemento invariato
                # Altrimenti, sostituisco l'elemento con uno spazio vuoto
                riga_modificata.append(elemento if elemento in colpi_sparati_giocatore1 else ' ')
            # Stampo gli elementi della riga modificata separati da uno spazio
            print(" ".join(riga_modificata))
