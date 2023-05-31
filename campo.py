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
            # Il primo elemento della lista è il numero della riga incrementato di 1 convertito in stringa
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
    def aggiorna_campo(self):
        # Itera attraverso ogni riga nella griglia del campo (self.campo)
        for riga in self.campo:
            # Per ogni riga stampa gli elementi separati da uno spazio
            print(" ".join(riga))

    # Parametri: 'colpi_sparati': Una lista contenente le coordinate dei colpi sparati nel campo di gioco
    # Metodo che restituisce una stringa che rappresenta il campo di gioco aggiornato
    def campo_vuoto(self, colpi_sparati):
        # Crea una copia del campo di gioco
        campo_copia = [riga.copy() for riga in self.campo]
        # Itera attraverso ogni riga, esclusa la prima
        for riga in campo_copia[1:]:
            # Per ogni cella controlla se contiene una nave vedendo se vi è un carattere diverso dallo spazio
            # Controlla se le coordinate non sono presenti nella lista colpi_sparati
            for i in range(1, len(riga)):
                if riga[i] != ' ' and (riga, i) not in colpi_sparati:
                    riga[i] = ' '
                elif (riga, i) in colpi_sparati:
                    riga[i] = 'O'
        # Il metodo restituisce una stringa che rappresenta il campo di gioco aggiornato
        # Dove le navi non colpite sono indicate come spazi vuoti (' ')
        # I colpi sparati ma mancati sono indicati: ('O')
        return '\n'.join([' '.join(riga) for riga in campo_copia])

    # Parametri: 'riga': La riga del campo di gioco in cui si desidera sparare
    #            'colonna': La colonna del campo di gioco in cui si desidera sparare
    # Metodo che restituisce una stringa che rappresenta l'esito del colpo sparato
    def colpisci_campo(self, riga, colonna):
        # Controllo il contenuto della cella corrispondente alla riga e alla colonna specificata nel campo di gioco
        if self.campo[riga][colonna] == 'M':
            # Se la cella contiene 'M' viene restituito colpo mancato
            return "Colpo mancato"
        else:
            # Altrimenti, se la cella contiene una nave, il colpo viene segnato come a segno
            self.campo[riga][colonna] = 'X'
            # Tramite il metodo 'aggiungi_segnalazione' viene aggiunta la segnalazione 'X'
            self.aggiungi_segnalazione([(riga, colonna, 'X')])
            # Verifico che la nave sia stata affondata tramite il metodo 'rimuovi_nave_affondata'
            nave_affondata = self.rimuovi_nave_affondata(riga, colonna)
            # Se la nave è stata affondata
            if nave_affondata:
                # Viene aggiornato il campo di gioco chiamando il metodo 'aggiorna_campo'
                self.aggiorna_campo()
                # Viene restituita una stringa che indica che la nave è stata affondata, fornendo il nome della nave
                return f"Affondato! Hai affondato la nave {nave_affondata.nome}"
            else:
                # Se la nave non è stata affondata viene restituita la stringa "Colpito!"
                return "Colpito!"

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
                # Chiamo il metodo 'aggiorna_campo' per aggiornare il campo dopo aver rimosso la nave affondata
                self.aggiorna_campo()
                return nave
        # Restituisco None se non è stata trovata alcuna nave
        return None

    # Parametri: 'colpi_sparati': una lista di tuple rappresentanti le coordinate dei colpi sparati
    # Metodo che aggiunge un punto dove viene sparato il colpo nel campo di gioco
    def aggiungi_segnalazione(self, colpi_sparati):
        # Creo uno copia del campo di gioco
        campo_copia = [riga.copy() for riga in self.campo]
        # Itero attraverso la copia del campo, escludendo la prima riga
        for riga in campo_copia[1:]:
            # Itero per ciascuna riga attraverso le colonne escludendo la prima
            for i in range(1, len(riga)):
                # Se la posizione non è vuota (diversa da uno spazio) e il colpo non è presente tra i colpi sparati
                if riga[i] != ' ' and (riga, i) not in colpi_sparati:
                    # Sostituisco la posizione con uno spazio vuoto
                    riga[i] = ' '
                # Se il colpo è presente tra i colpi sparati viene effettuato un controllo aggiuntivo
                elif (riga, i) in colpi_sparati:
                    # Se la posizione contiene 'M' o 'X' la segnalazione rimane invariata
                    if riga[i] == 'M' or riga[i] == 'X':
                        continue
                    # Altrimenti se la cella è vuota, non contiene una nave, quindi nave mancata
                    elif riga[i] == ' ':
                        # Aggiungo 'O' che sta per nave mancata
                        riga[i] = 'O'
                    # Altrimenti se la cella non è vuota
                    else:
                        # Aggiungo 'X' che sta per nave colpita
                        riga[i] = 'X'
        self.campo = campo_copia
