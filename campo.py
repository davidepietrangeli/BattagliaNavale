# Import della libreria 'sys' per interagire con il sistema operativo e l'interprete
import sys
# Import dei file contenuti nel progetto globale
import tipo_nave
import utile


# Metodo che crea il campo di gioco e svolge il posizionamento delle navi su di esso
def crea_campo(righe, colonne, tipo_lista):
    # Creo il campo di gioco come una matrice di righe x colonne inizializzata con zeri
    campo = [[0] * colonne for _ in range(righe)]
    # Creo lista vuota che conterrà le istanze delle navi posizionate
    lista_navi = []
    # Per ogni valore 'i' in 'tipo_lista' il metodo richiede all'utente l'inserimento delle coordinate e dell'orientamento
    for i in tipo_lista:
        # Stampo un messaggio all'utente specifico per il tipo di nave
        utile.messaggio_utente(i)
        inserimento_corretto = False
        prove = 0
        # Gestisco gli eventuali errori
        while not inserimento_corretto:
            try:
                riga_partenza = int(input(f'\nInserisci riga. Un numero da 1 a {righe}: '))
                colonna_partenza = int(input(f'\nInserisci colonna. Un numero da 1 a {colonne}: '))
            except ValueError:
                print(f'\u001b[31m\nRiga e/o colonna non valida, riprova ancora!\033[0m')
                continue
            if not utile.controlla_punto_partenza(righe, colonne, riga_partenza, colonna_partenza):
                print('\u001b[31m\nErrore! Il punto di partenza dato non è valido. Prova ancora!\033[0m')
                continue
            orientamento = input('\nInserisci orientamento. Deve essere ''o'' per orizzontale o ''v'' per verticale: \033[0m')
            if not utile.controllo_orientamento(orientamento):
                print(
                    '\u001b[31m\nErrore! Orientamento dato non valido. Prova ancora ponendo attenzione sulla correttezza lessicale'
                    'la tua scelta\033[0m')
                continue

            # Chiamo il metodo 'controllo_posizionamento_orizzontale_nave' per controllare se è possibile posizionare la nave
            if orientamento == 'o':
                error, coordinate = controllo_posizionamento_orizzontale_nave(righe, colonne, campo, riga_partenza, colonna_partenza, i)
                if not error:
                    inserimento_corretto = True
            # Chiamo il metodo 'controllo_posizionamento_verticale_nave' per controllare se è possibile posizionare la nave
            else:
                error, coordinate = controllo_posizionamento_verticale_nave(righe, colonne, campo, riga_partenza, colonna_partenza, i)
                if not error:
                    inserimento_corretto = True

            # Chiamo il metodo 'stampa_campo' per visualizzare il campo di gioco
            stampa_campo(campo, righe, colonne)

            # Creo una condizione per la quale l'errore non può verificarsi più di tre volte
            if not inserimento_corretto:
                prove += 1
                if prove > 3:
                    print("\n"*30)
                    print("\u001b[31mTroppi tentativi. Ricomincia il gioco"
                          "campo\033[0m")
                    sys.exit()

        # Creo l'istanza della nave corrispondente, in base al valore di 'i'
        if i == 5:
            nave = tipo_nave.Portaerei(orientamento, colonna_partenza, riga_partenza, coordinate)
        elif i == 4:
            nave = tipo_nave.Corazzata(orientamento, colonna_partenza, riga_partenza, coordinate)
        elif i == 3:
            nave = tipo_nave.Sottomarino(orientamento, colonna_partenza, riga_partenza, coordinate)
        elif i == 2:
            nave = tipo_nave.Cacciatorpediniere(orientamento, colonna_partenza, riga_partenza, coordinate)
        elif i == 1:
            nave = tipo_nave.Sommergibile(orientamento, colonna_partenza, riga_partenza, coordinate)
        # Aggiungo l'istanza della nave alla lista 'lista_navi'
        lista_navi.append(nave)
    return campo, lista_navi
# Metodo che restituisce il campo di gioco con la lista delle navi


# Metodo che stampa il campo di gioco rappresentato dalla matrice 'campo_gioco' con le dimensione specificate da 'righe' e 'colonne'
def stampa_campo(campo_gioco, righe, colonne):
    # Stampo l'intestazione del campo che va da 1 a 'colonne'
    # Tramite la funzione 'join' concateno gli elementi di una lista in una stringa separata da spazi
    print("\n  " + " ".join(str(x) for x in range(1, colonne + 1)))
    # Itero su ogni riga del campo per stampare la riga corrispondente
    for r in range(righe):
        print(str(r + 1) + " " + " ".join(str(c) for c in campo_gioco[r]))
    # Stampo riga vuota per migliorare la leggibilità del campo
    print()


# Metodo che verifica se è possibile posizionare una nave in modo orizzontale sul campo di gioco
def controllo_posizionamento_orizzontale_nave(righe, colonne, campo, riga_partenza, colonna_partenza, lunghezza):
    error = False
    if colonna_partenza + lunghezza - 1 <= colonne:
        i = colonna_partenza - 1
        while i < colonna_partenza + lunghezza - 1 and not error:
            if campo[riga_partenza - 1][i] == 1:
                print("\u001b[31m\n\nErrore! Posizione già occupata da una nave\033[0m")
                error = True
                continue
            if riga_partenza == 1:
                if campo[riga_partenza][i] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            if riga_partenza == righe:
                if campo[riga_partenza - 2][i] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            if 1 < riga_partenza < righe:
                if campo[riga_partenza][i] == 1 or campo[riga_partenza - 2][i] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            if colonna_partenza != 1:
                if campo[riga_partenza - 1][colonna_partenza - 2] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            if colonna_partenza + lunghezza - 2 != colonne - 1:
                if campo[riga_partenza - 1][colonna_partenza + lunghezza - 1] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            i = i + 1
        if not error:
            coordinate = []
            for i in range(colonna_partenza - 1, colonna_partenza + lunghezza - 1):
                campo[riga_partenza - 1][i] = 1
                coordinate.append([riga_partenza, i + 1])
            return error, coordinate
    else:
        error = True
        print("\u001b[31m\n\nErrore! La nave è fuori dal campo\033[0m")
    return error, None


# Metodo che verifica se è possibile posizionare una nave in modo verticale sul campo di gioco
def controllo_posizionamento_verticale_nave(righe, colonne, campo, riga_partenza, colonna_partenza, lunghezza):
    error = False
    if riga_partenza + lunghezza - 1 <= righe:
        i = riga_partenza - 1
        while i < riga_partenza + lunghezza - 1 and not error:
            if campo[i][colonna_partenza - 1] == 1:
                print("\u001b[31m\n\nErrore! Posizione già occupata da una nave\033[0m")
                error = True
                continue
            if colonna_partenza == 1:
                if campo[i][colonna_partenza] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            if colonna_partenza == colonne:
                if campo[i][colonna_partenza - 2] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            if 1 < colonna_partenza < colonne:
                if campo[i][colonna_partenza] == 1 or campo[i][colonna_partenza - 2] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            if riga_partenza != 1:
                if campo[riga_partenza - 2][colonna_partenza - 1] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            if riga_partenza + lunghezza - 2 != righe - 1:
                if campo[riga_partenza + lunghezza - 1][colonna_partenza - 1] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            i = i + 1
        if not error:
            coordinate = []
            for i in range(riga_partenza - 1, riga_partenza + lunghezza - 1):
                campo[i][colonna_partenza - 1] = 1
                coordinate.append([i + 1, colonna_partenza])
            return error, coordinate
    else:
        print("\u001b[31m\n\nErrore! La nave è fuori dal campo\033[0m")
        error = True
    return error, None
