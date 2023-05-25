# @author PIETRANGELI DAVIDE:
import os

from campo import Campo
from nave import Nave, Posizione
from giocatore import Giocatore

if __name__ == '__main__':

    # Richiesta dei nomi dei giocatori all'utente
    nome_giocatore1 = input("Inserisci il nome del Giocatore 1: ")
    nome_giocatore2 = input("Inserisci il nome del Giocatore 2: ")

    # Creazione degli oggetti Giocatore
    giocatore1 = Giocatore(nome_giocatore1)
    giocatore2 = Giocatore(nome_giocatore2)
    print("Nome Giocatore 1:", giocatore1.nome)
    print("Nome Giocatore 2:", giocatore2.nome)

    # Richiesta del numero di righe e colonne per il campo da battaglia
    num_righe = int(input("Inserisci il numero di righe (min.5 max.10): "))
    num_colonne = int(input("Inserisci il numero di colonne (min.5 max.10): "))

    # Creazione del campo da battaglia
    campo1 = Campo(num_righe, num_colonne)
    campo2 = Campo(num_righe, num_colonne)
    print(campo1)

    # Creazione Navi da battaglia
    navi = [
        ("Portaerei", 5),
        ("Corazzata", 4),
        ("Sottomarino", 3),
        ("Cacciatorpediniere", 2),
        ("Sommergibile", 1)
    ]

    # Posizionamento delle Navi per il Giocatore 1
    print(f"{giocatore1.nome} - Fase di posizionamento delle Navi da battaglia:")
    giocatore1_finito = False
    navi_campo1 = []

    while not giocatore1_finito:
        for nome, lunghezza in navi:
            posizione = input(f"Inserisci la posizione della nave {nome} di lunghezza {lunghezza}:\n(es: A3) ")

            orientamento_valido = False

            while not orientamento_valido:
                orientamento = input(f"Inserisci l'orientamento della nave {nome}:\n"
                                     f"O: per orientarla orizzontalmente\n"
                                     f"V: per orientarla verticalmente\n"
                                     f"Inserisci la tua scelta (O/V): ")
                orientamento = orientamento.upper()

                if orientamento == 'O' or orientamento == 'V':
                    orientamento_valido = True
                else:
                    print("\nOrientamento non valido.\nInserisci l'orientamento corretto.\n")

            # Estrai colonna e riga delle coordinate
            colonna = posizione[0].upper()
            riga = int(posizione[1:])

            # Creazione e posizionamento della Nave
            posizione = Posizione(colonna, riga)
            nave = Nave(nome, lunghezza, posizione, orientamento)

            navi_campo1.append(nave)

            # Stampa il campo con la nave posizionata
            campo1.posiziona_navi(navi_campo1)
            print(f"{giocatore1.nome} - Campo:")
            campo1.aggiorna_campo()

        risposta = input("Hai finito di posizionare le navi? (S/N): ")
        if risposta.lower() == 's':
            giocatore1_finito = True

    campo1.posiziona_navi(navi_campo1)

    # Pulizia dello schermo
    os.system('cls' if os.name == 'nt' else 'clear')

    # Stampa campo vuoto Giocatore 2
    print(campo2)

    # Posizionamento delle Navi per il Giocatore 2
    print(f"{giocatore2.nome} - Fase di posizionamento delle Navi da battaglia:")
    giocatore2_finito = False
    navi_campo2 = []

    while not giocatore2_finito:
        for nome, lunghezza in navi:
            posizione = input(f"Inserisci la posizione della nave {nome} di lunghezza {lunghezza}:\n(es: A3) ")

            orientamento_valido = False

            while not orientamento_valido:
                orientamento = input(f"Inserisci l'orientamento della nave {nome}:\n"
                                     f"O: per orientarla orizzontalmente\n"
                                     f"V: per orientarla verticalmente\n"
                                     f"Inserisci la tua scelta (O/V): ")
                orientamento = orientamento.upper()

                if orientamento == 'O' or orientamento == 'V':
                    orientamento_valido = True
                else:
                    print("\nOrientamento non valido.\nInserisci l'orientamento corretto.\n")

            # Estrai colonna e riga delle coordinate
            colonna = posizione[0].upper()
            riga = int(posizione[1:])

            # Creazione e posizionamento della Nave
            posizione = Posizione(colonna, riga)
            nave = Nave(nome, lunghezza, posizione, orientamento)

            navi_campo2.append(nave)

            # Stampa il campo con la nave posizionata
            campo2.posiziona_navi(navi_campo2)
            print(f"{giocatore2.nome} - Campo:")
            campo2.aggiorna_campo()

        risposta = input("Hai finito di posizionare le navi? (S/N): ")
        if risposta.lower() == 's':
            giocatore2_finito = True

    campo2.posiziona_navi(navi_campo2)

    # Pulizia dello schermo
    os.system('cls' if os.name == 'nt' else 'clear')

    # Creazione campo vuoto per non far vedere le navi all'avversario
    campo_vuoto = campo1.campo_vuoto()

    # Gioco
    while True:
        # Turno del Giocatore 1
        print(f"{giocatore1.nome} è il tuo turno")
        print("Campo:")
        campo1.aggiorna_campo()
        print("Campo dell'avversario:")
        print(campo2.campo_vuoto())

        # Sparo del Giocatore 1
        print(f"{giocatore1.nome}, Spara un colpo")
        riga_sparo = int(input("Inserisci la riga dove sparare: ")) - 1
        colonna_sparo = int(input("Inserisci la colonna dove sparare: ")) - 1
        colonna_sparo_lettera = campo2.get_lettera_colonna(colonna_sparo)

        risultato_sparo = campo2.colpisci_campo(riga_sparo, colonna_sparo_lettera)
        print(risultato_sparo)

        if risultato_sparo == "M":
            print("Colpo mancato!")
            # Passa al turno dell'avversario
            break
        elif risultato_sparo == "H":
            print("Colpo a segno!")
            nave_affondata = campo2.rimuovi_nave_affondata(riga_sparo, colonna_sparo_lettera)
            if nave_affondata is not None:
                print(f"Nave {nave_affondata.nome} affondata!")
        else:
            print("Errore: colpo non valido")

        # Richiedi all'utente di premere "Invio" per continuare
        input("Premi Invio per passare al turno dell'avversario")

        # Pulizia dello schermo
        os.system('cls' if os.name == 'nt' else 'clear')

        # Turno del Giocatore 2
        print(f"{giocatore2.nome} è il tuo turno")
        print("Campo:")
        campo1.aggiorna_campo()
        print("Campo dell'avversario")
        print(campo1.campo_vuoto())

        # Sparo del Giocatore 2
        print(f"{giocatore2.nome}, Spara un colpo")
        riga_sparo = int(input("Inserisci la riga dove sparare: ")) - 1
        colonna_sparo = int(input("Inserisci la colonna dove sparare: ")) - 1
        colonna_sparo_lettera = campo1.get_lettera_colonna(colonna_sparo)
        risultato_sparo = campo1.colpisci_campo(riga_sparo, colonna_sparo_lettera)
        print(risultato_sparo)

        if risultato_sparo == "M":
            print("Colpo mancato!")
            # Passa al turno dell'avversario
            break
        elif risultato_sparo == "H":
            print("Colpo a segno!")
            nave_affondata = campo1.rimuovi_nave_affondata(riga_sparo, colonna_sparo_lettera)
            if nave_affondata is not None:
                print(f"Nave {nave_affondata.nome} affondata!")

        # Richiedi all'utente di premere "Invio" per continuare
        input("Premi Invio per passare al turno dell'avversario")

        # Pulizia dello schermo
        os.system('cls' if os.name == 'nt' else 'clear')
