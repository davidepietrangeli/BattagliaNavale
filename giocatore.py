import os


# Definizione della Classe 'Giocatore'
class Giocatore:
    def __init__(self, nome):
        self.nome = nome
        self.navi_affondate = []

    def svolgi_gioco(self, campo1, campo2):
        colpi_sparati = []  # Inizialmente non ci sono colpi sparati

        # Gioco
        turno_giocatore1 = True

        while True:
            if turno_giocatore1:
                # Turno del Giocatore 1
                print(f"{self.nome} è il tuo turno")
                print("Campo:")
                campo1.aggiorna_campo()
                print("Campo dell'avversario:")
                print(campo2.campo_vuoto(colpi_sparati))

                # Sparo del Giocatore 1
                print(f"{self.nome}, Spara un colpo")
                riga_sparo = int(input("Inserisci la riga dove sparare: ")) - 1
                colonna_input = input("Inserisci la colonna dove sparare: ").upper()
                if len(colonna_input) == 1 and 'A' <= colonna_input <= 'Z':
                    colonna_sparo = ord(colonna_input) - ord('A')
                    risultato_sparo = campo2.colpisci_campo(riga_sparo, colonna_sparo)
                    print(risultato_sparo)

                    if risultato_sparo == "Mancato":
                        print("Colpo mancato!")
                        turno_giocatore1 = False  # Passa al turno del giocatore 2
                    elif risultato_sparo == "Colpito!":
                        nave_affondata = campo2.rimuovi_nave_affondata(riga_sparo, colonna_sparo)
                        if nave_affondata is not None:
                            print(f"Nave {nave_affondata.nome} affondata!")
                    else:
                        print("Errore: colpo non valido")

                    # Aggiungi il colpo sparato alla lista dei colpi sparati
                    colpi_sparati.append((riga_sparo, colonna_sparo))

                    # Richiedi all'utente di premere "Invio" per continuare
                    input("Premi Invio per passare al turno dell'avversario")

                    # Pulizia dello schermo
                    os.system('cls' if os.name == 'nt' else 'clear')

                else:
                    print("Inserisci una lettera valida per la colonna.")

            else:
                # Turno del Giocatore 2
                print(f"{self.nome} è il tuo turno")
                print("Campo:")
                campo2.aggiorna_campo()
                print("Campo dell'avversario")
                print(campo1.campo_vuoto(colpi_sparati))

                # Sparo del Giocatore 2
                print(f"{self.nome}, Spara un colpo")
                riga_sparo = int(input("Inserisci la riga dove sparare: ")) - 1
                colonna_input = input("Inserisci la colonna dove sparare: ").upper()
                if len(colonna_input) == 1 and 'A' <= colonna_input <= 'Z':
                    colonna_sparo = ord(colonna_input) - ord('A')
                    risultato_sparo = campo1.colpisci_campo(riga_sparo, colonna_sparo)
                    print(risultato_sparo)

                    if risultato_sparo == "Mancato":
                        print("Colpo mancato!")
                        turno_giocatore1 = False  # Passa al turno del giocatore 2
                    elif risultato_sparo == "Colpito!":
                        nave_affondata = campo1.rimuovi_nave_affondata(riga_sparo, colonna_sparo)
                        if nave_affondata is not None:
                            print(f"Nave {nave_affondata.nome} affondata!")
                    else:
                        print("Errore: colpo non valido")

                    # Aggiungi il colpo sparato alla lista dei colpi sparati
                    colpi_sparati.append((riga_sparo, colonna_sparo))

                    # Richiedi all'utente di premere "Invio" per continuare
                    input("Premi Invio per passare al turno dell'avversario")

                    # Pulizia dello schermo
                    os.system('cls' if os.name == 'nt' else 'clear')

                else:
                    print("Inserisci una lettera valida per la colonna.")
