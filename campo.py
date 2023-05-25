# Definizione della Classe 'Campo'
class Campo:
    def __init__(self, num_righe, num_colonne):
        self.num_righe = num_righe
        self.num_colonne = num_colonne
        self.campo = self.crea_campo()
        self.navi = []

    def crea_campo(self):
        campo = []
        # Aggiunta della prima riga con le lettere delle colonne
        riga_superiore = [' '] + [chr(i) for i in range(ord('A'), ord('A') + self.num_colonne)]
        campo.append(riga_superiore)

        for riga in range(self.num_righe):
            riga_campo = [str(riga + 1)] + [''] * self.num_colonne
            campo.append(riga_campo)
        return campo

    def __str__(self):
        campo_str = ""

        # Calcola la larghezza massima per ciascuna colonna (così da poter mantenere un allineamento corretto)
        colonna_widths = [max(len(riga[colonna]) for riga in self.campo) for colonna in range(self.num_colonne + 1)]

        for riga in self.campo:
            campo_str += " ".join(
                f"{riga[colonna]:<{colonna_widths[colonna]}}" for colonna in range(self.num_colonne + 1)) + "\n"
        return campo_str

    @staticmethod
    def get_lettera_colonna(colonna):
        return chr(ord('A') + colonna - 1)

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

    def campo_vuoto(self):
        campo_copia = [riga.copy() for riga in self.campo]

        for riga in campo_copia[1:]:
            for i in range(1, len(riga)):
                if riga[i] != ' ':
                    riga[i] = ' '

        return '\n'.join([' '.join(riga) for riga in campo_copia])

    def colpisci_campo(self, riga, colonna):
        if self.campo[riga][colonna] == 'O':
            return "Hai già sparato in questa posizione"
        elif self.campo[riga][colonna] == ' ':
            self.campo[riga][colonna] = 'O'
            nave_affondata = self.rimuovi_nave_affondata(riga, colonna)
            if nave_affondata:
                return f"Affondato! Hai affondato la nave {nave_affondata.nome}"
            else:
                return "Colpito"
        else:
            return "Mancato"

    def rimuovi_nave_affondata(self, riga, colonna):
        for nave in self.navi:
            if (nave.posizione.riga == riga and
                    colonna >= nave.posizione.colonna and
                    colonna < nave.posizione.colonna + nave.lunghezza):
                # Verifica se la nave è affondata
                for c in range(nave.posizione.colonna, nave.posizione.colonna + nave.lunghezza):
                    if self.campo[riga][c] == 'N':
                        return None  # La nave non è ancora affondata

                # Rimuovi la nave dal campo e dalla lista delle navi
                for c in range(nave.posizione.colonna, nave.posizione.colonna + nave.lunghezza):
                    self.campo[riga][c] = 'X'
                self.navi.remove(nave)
                return nave

        return None
