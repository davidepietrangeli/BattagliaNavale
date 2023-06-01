import os


# Definizione della Classe 'Giocatore' che rappresenta un giocatore all'interno del gioco
class Giocatore:
    def __init__(self, nome):
        self.nome = nome  # nome del giocatore
        self.navi_affondate = []  # lista vuota che tiene traccia delle navi affondate dal giocatore durante il gioco

    # Metodo che viene utilizzato per gestire l'intero processo di gioco tra due giocatori
    # Il metodo non restituisce nulla, ma viene eseguito fino a quando non avviene la vittoria di uno dei giocatori
    #  Parametri: 'campo1': oggetto di tipo Campo che rappresenta il campo di gioco del primo giocatore
    #             'campo2': oggetto di tipo Campo che rappresenta il campo di gioco del secondo giocatore.
    def svolgi_gioco(self, campo1, campo2, colpi_sparati_giocatore1, colpi_sparati_giocatore2):
        # Viene controllato il turno attuale del giocatore
        turno_giocatore1 = True
        while True:
            if turno_giocatore1:
                # Turno del Giocatore 1
                print(f"{self.nome} è il tuo turno")
                print("Campo:")
                # Aggiorna e mostra il campo dopo ogni turno del Giocatore 1
                campo1.campo_pieno()
                print("Campo dell'avversario:")
                # Aggiorna e mostra il campo del Giocatore 2 con i colpi sparati dal Giocatore 1
                campo2.segno_colpo(colpi_sparati_giocatore1)
                print(campo2)
                # Sparo del Giocatore 1 (DA MODIFICARE)
                print(f"{self.nome}, Spara un colpo")
                # Richiedo all'utente la posizione dove si vuole sparare
                posizione_sparo = input("Inserisci la posizione dove sparare (es: A3): ")
                # Assegno alla variabile la colonna del punto di sparo
                colonna_sparo = posizione_sparo[0].upper()
                # Estraggo la sotto stringa per convertirla in un intero assegnato alla variabile
                riga_sparo = int(posizione_sparo[1:])
                # Viene controllato se la colonna inserita è valida e viene calcolata la colonna corrispondente
                if len(colonna_sparo) == 1 and 'A' <= colonna_sparo <= 'Z':
                    colonna_sparo = ord(colonna_sparo) - ord('A') + 1
                    # Viene effettuato il colpo sparato, utilizzando il metodo 'colpisci_campo' della classe Campo
                    risultato_sparo = campo2.colpisci_campo(riga_sparo, colonna_sparo)
                    print(risultato_sparo)
                    # Se il colpo è "Colpo mancato", si passato il turno al Giocatore 2
                    if risultato_sparo == "Colpo mancato":
                        print("Colpo mancato!")
                        turno_giocatore1 = False
                    # Se il colpo ha affondato una nave, viene rimossa la nave dal campo dell'avversario
                    elif risultato_sparo.startswith("Affondato!"):
                        nave_affondata = campo2.rimuovi_nave_affondata(riga_sparo, colonna_sparo)
                        print(risultato_sparo)
                        if nave_affondata:
                            print(f"Nave {nave_affondata.nome} affondata!")
                            # Controlla se tutte le navi del Giocatore 2 sono state affondate
                            if campo2.navi_rimaste() == 0:
                                print(f"Tutte le navi di {campo2.giocatore.nome} sono state affondate!")
                                print(f"Vittoria per {campo1.giocatore.nome}!")
                                # Termina il gioco
                                return
                        else:
                            print("Colpito!")
                    # Aggiunge il colpo sparato alla lista dei colpi sparati dal Giocatore 1
                    colpi_sparati_giocatore1.append((riga_sparo, colonna_sparo))
                    # Segna il colpo nel campo2 utilizzando il metodo 'segno_colpo'
                    campo2.segno_colpo(colpi_sparati_giocatore1)
                    # Richiede all'utente di premere "Invio" per passare al turno dell'avversario
                    input("Premi Invio per passare al turno dell'avversario")
                    # Pulizia dello schermo
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print("Inserisci una lettera valida per la colonna.")
            else:
                # Turno del Giocatore 2, vengono eseguite le stesse operazioni svolte dal Giocatore 1
                print(f"{self.nome} è il tuo turno")
                print("Campo:")
                campo2.campo_pieno()  # Aggiorna il campo dopo ogni turno del Giocatore 1
                print("Campo dell'avversario:")
                campo1.segno_colpo(colpi_sparati_giocatore2)
                print(campo1)
                # Sparo del Giocatore 2
                print(f"{self.nome}, Spara un colpo")
                # Richiedo all'utente la posizione dove si vuole sparare
                posizione_sparo = input("Inserisci la posizione dove sparare (es: A3): ")
                # Assegno alla variabile la colonna del punto di sparo
                colonna_sparo = posizione_sparo[0].upper()
                # Estraggo la sotto stringa per convertirla in un intero assegnato alla variabile
                riga_sparo = int(posizione_sparo[1:])
                # Viene controllato se la colonna inserita è valida e viene calcolata la colonna corrispondente
                if len(colonna_sparo) == 1 and 'A' <= colonna_sparo <= 'Z':
                    colonna_sparo = ord(colonna_sparo) - ord('A') + 1
                    # Viene effettuato il colpo sparato, utilizzando il metodo 'colpisci_campo' della classe Campo
                    risultato_sparo = campo1.colpisci_campo(riga_sparo, colonna_sparo)
                    print(risultato_sparo)
                    if risultato_sparo == "Colpo mancato":
                        print("Colpo mancato!")
                        turno_giocatore1 = True  # Passa al turno del giocatore 1
                    elif risultato_sparo.startswith("Affondato!"):
                        nave_affondata = campo1.rimuovi_nave_affondata(riga_sparo, colonna_sparo)
                        print(risultato_sparo)
                        if nave_affondata:
                            print(f"Nave {nave_affondata.nome} affondata!")
                            # Controlla se tutte le navi del Giocatore 1 sono state affondate
                            if campo1.navi_rimaste() == 0:
                                print(f"Tutte le navi di {campo1.giocatore.nome} sono state affondate!")
                                print(f"Vittoria per {campo2.giocatore.nome}!")
                                return  # Termina il gioco
                        else:
                            print("Colpito!")
                    # Aggiunge il colpo sparato alla lista dei colpi sparati dal Giocatore 1
                    colpi_sparati_giocatore2.append((riga_sparo, colonna_sparo))
                    # Segna il colpo nel campo1 utilizzando il metodo 'segno_colpo'
                    campo1.segno_colpo(riga_sparo, colonna_sparo, colpi_sparati_giocatore2)
                    # Richiede all'utente di premere "Invio" per passare al turno dell'avversario
                    input("Premi Invio per passare al turno dell'avversario")
                    # Pulizia dello schermo
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print("Inserisci una lettera valida per la colonna.")
