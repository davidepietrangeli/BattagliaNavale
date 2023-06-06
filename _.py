import sys
import tipo_nave
import utile

def crea_campo(righe, colonne, tipo_lista):
    campo = [[0] * colonne for r in range(righe)]
    lista_navi = []
        for i in tipo_lista:
            inserimento_corretto = False
            prove = 0

            while not inserimento_corretto:
                try:
                    riga_partenza = int(input(f'\nInserisci riga. Un numero da 1 a {righe}: '))
                    colonna_partenza = int(input(f'\nInserisci colonna. un numero da 1 a {colonne}: '))
                except ValueError:
                    print(f'\u001b[31m\nRiga e/o colonna non valida, riprova ancora!\033[0m')
                    continue
                if not Utile.controllo_punto_partenza(righe, colonne, riga_partenza, colonna_partenza):
                    print('\u001b[31m\nErrore! Il punto di partenza dato non è valido. Prova ancora!\033[0m')
                    continue

                orientamento = input('\nInserisci orientamento. Deve essere orizzontale o verticale: \033[0m')
                if not Utile.controllo_orientamento(orientamento):
                    print(
                        '\u001b[31m\nErrore! Orientamento dato non valido. Prova ancora ponendo attenzione sulla correttezza lessicale'
                        'la tua scelta\033[0m')
                    continue

                if orientamento == 'orizzontale':
                    errore, coordinate = controllo_posizionamento_orizzontale_nave(righe, colonne, campo, riga_partenza, colonna_partenza, i)
                    if not error:
                        inserimento_corretto = True

                else:
                    error, coordinate = controllo_posizionamento_verticale_nave(righe, colonne, campo, riga_partenza, colonna_partenza, i)
                    if not error:
                        inserimento_corretto = True
                stampa_campo(campo, righe, colonne)
                if not inserimento_corretto:
                    prove += 1
                    if prove > 3:
                        print("\n"*30)
                        print("\u001b[31mTroppi tentativi. Ricomincia il gioco"
                              "field\033[0m")
                        sys.exit()


        if i == 5:
            nave = tipo_nave.Portaerei(orientamento, riga_partenza, colonna_partenza, coordinate)
        elif i == 4:
            nave = tipo_nave.Corazzata(orientamento, riga_partenza, colonna_partenza, coordinate)
        elif i == 3:
            nave = tipo_nave.Sottomarino(orientamento, riga_partenza, colonna_partenza, coordinate)
        elif i == 2:
            nave = tipo_nave.Cacciatorpediniere(orientamento, riga_partenza, colonna_partenza, coordinate)
        elif i == 1:
            nave = tipo_nave.Sommergibile(orientamento, riga_partenza, colonna_partenza, coordinate)
        lista_navi.append(nave)
    return campo, lista_navi

def stampa_campo(campo_gioco, righe, colonne):
    print("\n  " + " ".join(str(x) for x in range(1, colonne + 1)))
    for r in range(righe):
        print(str(r + 1) + " " + " ".join(str(c) for c in campo_gioco[r]))
    print()

def controllo_posizionamento_orizzontale_nave(righe, colonne, campo, riga_partenza, colonna_partenza, lunghezza):
    error = False
    if colonna_partenza + lunghezza -1 <= colonne:
        i = colonna_partenza - 1
        while i < colonna_partenza + lunghezza - 1 and not error:
            if campo[colonna_partenza - 1][i] == 1:
                print("\u001b[31m\n\nErrore! Posizione già occupata da una nave\033[0m")
                error = True
                continue
            if riga_partenza == 1:
                if campo[riga_partenza][i] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            if riga_partenza == righe:
                if campo[riga_partenza -2][i] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            if 1 < riga_partenza < righe:
                if campo[riga_partenza][i] == 1 or campo[riga_partenza -2][i] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            if colonna_partenza != 1:
                if campo[riga_partenza -1][colonna_partenza -2] == 1:
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
            for i in range(colonna_partenza -1, colonna_partenza + lunghezza - 1):
                campo[riga_partenza - 1][i] = 1
                coordinate.append([riga_partenza, i + 1])
            return error, coordinate
    else
        error = True
        print("\u001b[31m\n\nErrore! La nave è fuori dal campo\033[0m")
    return error, None

def controllo_posizionamento_verticale_nave(righe, colonne, campo, riga_partenza, colonna_partenza, lunghezza):
    error = False
    if riga_partenza + lunghezza -1 <= righe:
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
                if campo[i][colonna_partenza -2] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            if 1 < colonna_partenza < colonne:
                if campo[i][colonna_partenza] == 1 or campo[i][colonna_partenza -2] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            if riga_partenza != 1:
                if campo[riga_partenza -2][colonna_partenza - 1] == 1:
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
            for i in range(riga_partenza -1, riga_partenza + lunghezza - 1):
                campo[i][colonna_partenza - 1] = 1
                coordinate.append([i + 1, colonna_partenza ])
            return error, coordinate
    else
        error = True
        print("\u001b[31m\n\nErrore! La nave è fuori dal campo\033[0m")
    return error, None
