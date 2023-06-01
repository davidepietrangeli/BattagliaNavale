# @author PIETRANGELI DAVIDE:
import os

# Faccio l'importazione delle classi nel programma principale
from campo import Campo
from nave import Nave, Posizione
from giocatore import Giocatore

if __name__ == '__main__':

    # Richiesta all'utente dei nomi dei giocatori
    nome_giocatore1 = input("Inserisci il nome del Giocatore 1: ")
    nome_giocatore2 = input("Inserisci il nome del Giocatore 2: ")

    # Creazione degli oggetti Giocatore
    giocatore1 = Giocatore(nome_giocatore1)
    giocatore2 = Giocatore(nome_giocatore2)
    print("Nome Giocatore 1:", giocatore1.nome)
    print("Nome Giocatore 2:", giocatore2.nome)

    # Richiesta all'utente del numero di righe e colonne per il campo da battaglia
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
            # Richiedo all'utente di inserire la posizione della nave, rappresentata da una colonna e una riga
            posizione = input(f"Inserisci la posizione della nave {nome} di lunghezza {lunghezza}:\n(es: A3) ")
            orientamento_valido = False
            # Richiedo all'utente di inserire l'orientamento della nave
            while not orientamento_valido:
                orientamento = input(f"Inserisci l'orientamento della nave {nome}:\n"
                                     f"O: per orientarla orizzontalmente\n"
                                     f"V: per orientarla verticalmente\n"
                                     f"Inserisci la tua scelta (O/V): ")
                orientamento = orientamento.upper()
                # Controllo se l'orientamento è valido
                if orientamento == 'O' or orientamento == 'V':
                    orientamento_valido = True
                else:
                    # Se non è valido chiedo di reinserire l'orientamento
                    print("\nOrientamento non valido.\nInserisci l'orientamento corretto.\n")
            # Estrai colonna e riga delle coordinate della posizione inserita
            colonna = posizione[0].upper()
            riga = int(posizione[1:])
            # Creazione dell'oggetto posizione con la colonna e la riga inserita
            posizione = Posizione(colonna, riga)
            # Creo oggetto 'nave' con i parametri inseriti tra le ()
            nave = Nave(nome, lunghezza, posizione, orientamento)
            # Aggiungo la nave alla lista delle navi del campo1
            navi_campo1.append(nave)
            # Posiziono la nave sul campo1
            campo1.posiziona_navi(navi_campo1)
            # Stampo il campo con la nave posizionata
            print(f"{giocatore1.nome} - Campo:")
            campo1.campo_pieno()
        # Richiedo all'utente se ha finito di posizionare le navi
        risposta = input("Hai finito di posizionare le navi? (S/N): ")
        if risposta.lower() == 's':
            giocatore1_finito = True
    # Richiamo il metodo 'posiziona_navi' utilizzando la lista di navi per assicurarmi il corretto posizionamento
    campo1.posiziona_navi(navi_campo1)
    # Pulizia dello schermo per non far vedere al Giocatore 2 il posizionamento delle navi da parte del Giocatore 1
    os.system('cls' if os.name == 'nt' else 'clear')
    # Stampa campo vuoto Giocatore 2
    print(campo2)
    # Posizionamento delle Navi per il Giocatore 2
    print(f"{giocatore2.nome} - Fase di posizionamento delle Navi da battaglia:")
    giocatore2_finito = False
    navi_campo2 = []
    while not giocatore2_finito:
        for nome, lunghezza in navi:
            # Richiedo all'utente di inserire la posizione della nave, rappresentata da una colonna e una riga
            posizione = input(f"Inserisci la posizione della nave {nome} di lunghezza {lunghezza}:\n(es: A3) ")
            orientamento_valido = False
            # Richiedo all'utente di inserire l'orientamento della nave
            while not orientamento_valido:
                orientamento = input(f"Inserisci l'orientamento della nave {nome}:\n"
                                     f"O: per orientarla orizzontalmente\n"
                                     f"V: per orientarla verticalmente\n"
                                     f"Inserisci la tua scelta (O/V): ")
                orientamento = orientamento.upper()
                # Controllo se l'orientamento è valido
                if orientamento == 'O' or orientamento == 'V':
                    orientamento_valido = True
                else:
                    # Se non è valido chiedo di reinserire l'orientamento
                    print("\nOrientamento non valido.\nInserisci l'orientamento corretto.\n")
            # Estrai colonna e riga delle coordinate della posizione inserita
            colonna = posizione[0].upper()
            riga = int(posizione[1:])
            # Creazione dell'oggetto posizione con la colonna e la riga inserita
            posizione = Posizione(colonna, riga)
            # Creo oggetto 'nave' con i parametri inseriti tra le ()
            nave = Nave(nome, lunghezza, posizione, orientamento)
            # Aggiungo la nave alla lista delle navi del campo2
            navi_campo2.append(nave)
            # Posizione la nave sul campo2
            campo2.posiziona_navi(navi_campo2)
            # Stampo il campo con la nave posizionata
            print(f"{giocatore2.nome} - Campo:")
            campo2.campo_pieno()
        # Richiedo all'utente se ha finito di posizionare le navi
        risposta = input("Hai finito di posizionare le navi? (S/N): ")
        if risposta.lower() == 's':
            giocatore2_finito = True
    # Richiamo il metodo 'posiziona_navi' utilizzando la lista di navi per assicurarmi il corretto posizionamento
    campo2.posiziona_navi(navi_campo2)
    # Pulizia dello schermo per non far vedere al Giocatore 1 il posizionamento delle navi da parte del Giocatore 2
    os.system('cls' if os.name == 'nt' else 'clear')

    # Creo lista vuota per tenere traccia dei colpi sparati
    colpi_sparati = []
    # Creazione campo vuoto per non far vedere le navi all'avversario
    campo_aggiornato = campo1.campo_aggiornato(colpi_sparati)
    # Richiamo del metodo 'svolgi_gioco' per il Giocatore 1
    giocatore1.svolgi_gioco(campo1, campo2)
    # Pulizia dello schermo
    os.system('cls' if os.name == 'nt' else 'clear')
    # Richiamo del metodo 'svolgi_gioco' per il Giocatore 2
    giocatore2.svolgi_gioco(campo2, campo1)
