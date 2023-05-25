# Definizione della Classe 'Campo'
class Campo:
    def __init__(self, num_righe, num_colonne):
        self.num_righe = num_righe
        self.num_colonne = num_colonne
        self.campo = self.crea_campo()

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

    def posiziona_navi(self, navi):
        for nave in navi:
            colonna = ord(nave.posizione.colonna.upper()) - ord('A') + 1
            riga = nave.posizione.riga
            orientamento = nave.orientamento.upper()

            if orientamento == "Verticale":
                for i in range(nave.lunghezza):
                    if riga + i <= self.num_righe:
                        self.campo[riga + i][colonna] = nave.nome[0]
            elif orientamento == "Orizzontale":
                for i in range(nave.lunghezza):
                    if riga + i <= self.num_colonne:
                        self.campo[riga][colonna + i] = nave.nome[0]

    def aggiorna_campo(self):
        for riga in self.campo:
            print(" ".join(riga))

