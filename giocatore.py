import os


# Definizione della Classe 'Giocatore' che rappresenta un giocatore all'interno del gioco
class Giocatore:
    def __init__(self, nome):
        self.nome = nome  # nome del giocatore
        self.navi_affondate = []  # lista vuota che tiene traccia delle navi affondate dal giocatore durante il gioco

    # Metodo che viene utilizzato per gestire l'intero processo di gioco tra due giocatori
    # Il metodo non restituisce nulla, ma viene eseguito fino a quando non avviene la vittoria di uno dei giocatori
    #  Parametri: 'giocatore1': viene passato il nome del giocatore1
    #             'giocatore2': viene passato il nome del giocatore2
    #             'campo1': oggetto di tipo Campo che rappresenta il campo di gioco del primo giocatore
    #             'campo2': oggetto di tipo Campo che rappresenta il campo di gioco del secondo giocatore
    #             'colpi_sparati_giocatore1': parametro passato con la lista dei colpi sparati dal primo giocatore
    #             'colpi_sparati_giocatore2': parametro passato con la lista dei colpi sparati dal secondo giocatore
    def svolgi_gioco(self, giocatore1, giocatore2, campo1, campo2, colpi_sparati_giocatore1, colpi_sparati_giocatore2):
        # Viene controllato il turno attuale del giocatore
        turno_giocatore1 = True
        while True:
            if turno_giocatore1:
                # Turno del Giocatore 1
                print(f"{giocatore1.nome} è il tuo turno")
                print("Questo è il tuo Campo:")
                # Aggiorna e mostra il campo dopo ogni turno del Giocatore 1
                campo1.campo_pieno()
                print("Campo dell'avversario:")
                # Aggiorna e mostra il campo del Giocatore 2 con i colpi sparati dal Giocatore 1
                campo2.campo2_solo_colpi(colpi_sparati_giocatore1)
                # Sparo del Giocatore 1
                print(f"{giocatore1.nome}, Spara un colpo")
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
                    # Aggiungo la posizione di sparo ai colpi sparati dal Giocatore 1
                    colpi_sparati_giocatore1.append((riga_sparo, colonna_sparo, risultato_sparo))
                    print(risultato_sparo)
                    # Se il colpo è "Colpo mancato", si passa il turno al Giocatore 2
                    if risultato_sparo == "Nave Mancata :(":
                        turno_giocatore1 = False
                        # Aggiorna e mostra il campo del Giocatore 2 con i colpi sparati dal Giocatore 1
                        campo2.campo2_solo_colpi(colpi_sparati_giocatore1)
                    elif risultato_sparo == "Hai colpito una nave!":
                        # Aggiorna e mostra il campo del Giocatore 2 con i colpi sparati dal Giocatore 1
                        campo2.campo2_solo_colpi(colpi_sparati_giocatore1)
                        turno_giocatore1 = True
                        # Controllo se la nave colpita è affondata richiamando il metodo 'rimuovi_nave_affondata'
                        nave_affondata = campo2.rimuovi_nave_affondata(riga_sparo, colonna_sparo)
                        if nave_affondata:
                            print(f"Nave {nave_affondata.nome} affondata!")
                            # Controlla se tutte le navi del Giocatore 2 sono state affondate
                            if len(campo2.navi) == 0:
                                print(f"Tutte le navi di {campo2.giocatore.nome} sono state affondate!")
                                print(f"Vittoria per {campo1.giocatore.nome}!")
                                # Termina il gioco
                                return
                            # Aggiorna e mostra il campo del Giocatore 2 con i colpi sparati dal Giocatore 1
                            campo2.campo2_solo_colpi(colpi_sparati_giocatore1)
                            turno_giocatore1 = True
                    # Segna il colpo nel campo2 utilizzando il metodo 'segno_colpo'
                    campo2.segno_colpo1(colpi_sparati_giocatore1)
                    # Richiede all'utente di premere "Invio" per passare al turno successivo
                    input("Premi INVIO per passare al turno successivo")
                    # Pulizia dello schermo
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print("Inserisci una lettera valida per la colonna.")
            else:
                # Turno del Giocatore 2
                print(f"{giocatore2.nome} è il tuo turno")
                print("Questo è il tuo Campo:")
                # Aggiorna e mostra il campo dopo ogni turno del Giocatore 2
                campo2.campo_pieno()
                print("Campo dell'avversario:")
                # Aggiorna e mostra il campo del Giocatore 1 con i colpi sparati dal Giocatore 2
                campo1.campo1_solo_colpi(colpi_sparati_giocatore2)
                # Sparo del Giocatore 2
                print(f"{giocatore2.nome}, Spara un colpo")
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
                    # Aggiungo la posizione di sparo ai colpi sparati dal Giocatore 2
                    colpi_sparati_giocatore2.append((riga_sparo, colonna_sparo, risultato_sparo))
                    print(risultato_sparo)
                    # Se il colpo è "Colpo mancato", si passa il turno al Giocatore 1
                    if risultato_sparo == "Nave Mancata :(":
                        turno_giocatore1 = True
                        # Aggiorna e mostra il campo del Giocatore 1 con i colpi sparati dal Giocatore 2
                        campo1.campo1_solo_colpi(colpi_sparati_giocatore2)
                    elif risultato_sparo == "Hai colpito una nave!":
                        # Aggiorna e mostra il campo del Giocatore 1 con i colpi sparati dal Giocatore 2
                        campo1.campo1_solo_colpi(colpi_sparati_giocatore2)
                        turno_giocatore1 = False
                        # Controllo se la nave colpita è affondata richiamando il metodo 'rimuovi_nave_affondata'
                        nave_affondata = campo1.rimuovi_nave_affondata(riga_sparo, colonna_sparo)
                        if nave_affondata:
                            print(f"Nave {nave_affondata.nome} affondata!")
                            # Controlla se tutte le navi del Giocatore 1 sono state affondate
                            if len(campo1.navi) == 0:
                                print(f"Tutte le navi di {campo1.giocatore.nome} sono state affondate!")
                                print(f"Vittoria per {campo2.giocatore.nome}!")
                                # Termina il gioco
                                return
                            # Aggiorna e mostra il campo del Giocatore 1 con i colpi sparati dal Giocatore 2
                            campo1.campo1_solo_colpi(colpi_sparati_giocatore2)
                            turno_giocatore1 = False
                    # Segna il colpo nel campo1 utilizzando il metodo 'segno_colpo'
                    campo1.segno_colpo2(colpi_sparati_giocatore2)
                    # Richiede all'utente di premere "Invio" per passare al turno successivo
                    input("Premi INVIO per passare al turno successivo")
                    # Pulizia dello schermo
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print("Inserisci una lettera valida per la colonna.")
