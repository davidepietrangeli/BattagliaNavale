# Definizione della Classe 'Campo' che rappresenta il campo di gioco in cui vengono posizionate le navi
class Campo:
    def __init__(self, num_righe, num_colonne):
        self.num_righe = num_righe  # numero delle righe del campo, memorizzato come oggetto della classe Campo
        self.num_colonne = num_colonne  # numero delle colonne del campo, memorizzato come oggetto della classe Campo
        # Richiama il metodo 'crea_campo' per inizializzare il campo di gioco con una matrice vuota
        self.campo = self.crea_campo()
        # Viene inizializzata la lista navi come un elenco vuoto che conterrà le navi posizionate nel campo
        self.navi = []
        # Ogni volta che una nave viene posizionata, viene aggiunta a questa lista. Questa lista può essere utilizzata
        # per verificare lo stato delle navi nel campo, contare il numero di navi rimaste o rimuovere una nave affondata

    # Metodo che si occupa di creare la rappresentazione iniziale del campo di gioco come una matrice
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

    # Metodo che restituisce una rappresentazione testuale del campo di gioco
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

    # Metodo che viene chiamato senza la creazione di un'istanza dell'oggetto
    @staticmethod
    # Metodo che prende il parametro colonna, che rappresenta un numero intero
    def get_lettera_colonna(colonna):
        # Viene utilizzata la funzione 'chr' per convertire un numero intero in un carattere
        # Viene restituita la lettera ottenuta convertendo il valore in un carattere
        return chr(ord('A') + colonna - 1)
    # Ad esempio, se si passa colonna = 1, il metodo restituirà 'A'
    
    def posiziona_navi(self, navi):
        griglia = [[' ' for _ in range(self.num_colonne + 1)] for _ in range(self.num_righe + 1)]

        # Inserisci gli indici delle colonne nella prima riga
        griglia[0] = [' '] + [chr(i) for i in range(ord('A'), ord('A') + self.num_colonne)]

        # Inserisci gli indici delle righe nella prima colonna
        for i in range(1, self.num_righe + 1):
            griglia[i][0] = str(i)

        for nave in navi:
            colonna = ord(nave.posizione.colonna.upper()) - ord('A') + 1
            riga = nave.posizione.riga
            orientamento = nave.orientamento.upper()

            if orientamento == "V":
                for i in range(nave.lunghezza):
                    if riga + i <= self.num_righe:
                        griglia[riga + i][colonna] = nave.nome[0]
            elif orientamento == "O":
                for i in range(nave.lunghezza):
                    if colonna + i <= self.num_colonne:
                        griglia[riga][colonna + i] = nave.nome[0]

        self.campo = griglia

    def aggiorna_campo(self):
        for riga in self.campo:
            print(" ".join(riga))

    def campo_vuoto(self, colpi_sparati):
        campo_copia = [riga.copy() for riga in self.campo]

        for riga in campo_copia[1:]:
            for i in range(1, len(riga)):
                if riga[i] != ' ' and (riga, i) not in colpi_sparati:
                    riga[i] = ' '
                elif (riga, i) in colpi_sparati:
                    riga[i] = '.'

        return '\n'.join([' '.join(riga) for riga in campo_copia])

    def colpisci_campo(self, riga, colonna):
        if self.campo[riga][colonna] == 'M':
            return "Colpo mancato"
        elif self.campo[riga][colonna] == 'O':
            return "Hai già sparato in questa posizione"
        else:
            self.campo[riga][colonna] = 'X'  # Segna il colpo a segno con 'X'
            self.aggiungi_segnalazione([(riga, colonna, 'X')])  # Aggiungi il colpo sparato
            nave_affondata = self.rimuovi_nave_affondata(riga, colonna)
            if nave_affondata:
                self.aggiorna_campo()  # Aggiorna il campo dopo aver affondato una nave
                return f"Affondato! Hai affondato la nave {nave_affondata.nome}"
            else:
                return "Colpito!"

    def rimuovi_nave_affondata(self, riga, colonna):
        for nave in self.navi:
            if (nave.posizione.riga == riga and
                    colonna >= nave.posizione.colonna and
                    colonna < nave.posizione.colonna + nave.lunghezza):
                # Verifica se la nave è affondata
                for c in range(nave.posizione.colonna, nave.posizione.colonna + nave.lunghezza):
                    if self.campo[riga][c] == 'N':
                        return False  # La nave non è ancora affondata

                # Rimuovi la nave dal campo e dalla lista delle navi
                for c in range(nave.posizione.colonna, nave.posizione.colonna + nave.lunghezza):
                    self.campo[riga][c] = 'X'
                self.navi.remove(nave)
                self.aggiorna_campo()  # Aggiorna il campo dopo aver rimosso la nave affondata
                return nave

        return None

    def aggiungi_segnalazione(self, colpi_sparati):
        campo_copia = [riga.copy() for riga in self.campo]

        for riga in campo_copia[1:]:
            for i in range(1, len(riga)):
                if riga[i] != ' ' and (riga, i) not in colpi_sparati:
                    riga[i] = ' '
                elif (riga, i) in colpi_sparati:
                    if riga[i] == 'M' or riga[i] == 'X':
                        continue  # Mantieni visibile il segno "M" o "X"
                    riga[i] = '.'

        self.campo = campo_copia
