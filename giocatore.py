import tipo_nave
import sys
import campo
import utile


def sparo(lista_navi, righe, colonne, campo_battaglia, giocatore, fine_gioco):
    colpo = False
    campo.stampa_campo(campo_battaglia, righe, colonne)
    riga_sparo, colonna_sparo = utile.scegli_controlla_punto_sparo(righe, colonne, campo_battaglia)
    for i in lista_navi:
        if tipo_nave.Nave.nave_colpita(i, riga_sparo, colonna_sparo):
            colpo = True
            campo_battaglia[riga_sparo - 1][colonna_sparo - 1] = 'X'
            if tipo_nave.Nave.nave_affondata(i):
                if vittoria(lista_navi):
                    print(f'\nIl giocatore {giocatore} ha vinto la partita')
                    fine_gioco = True
                else:
                    print('\nHai colpito e affondato una nave!')
            else:
                print('\nNave colpita!')
    if not colpo:
        print('\nNave mancata!')
        campo_battaglia[riga_sparo - 1][colonna_sparo - 1] = 'O'
    return colpo, fine_gioco, giocatore


def inizio_gioco(lista_navi1, lista_navi2, righe, colonne, opzioni, campo_battaglia1, campo_battaglia2):
    print("\n\n\n\n\n\nGiocatore 1 inizia il gioco!")
    colpo, fine_gioco, giocatore = sparo(lista_navi2, righe, colonne, campo_battaglia2, 1, fine_gioco=False)
    while not fine_gioco:
        colpo, fine_gioco, giocatore = cambio_giocatore(colpo, giocatore, lista_navi1, lista_navi2, righe, colonne, opzioni, campo_battaglia1, campo_battaglia2, fine_gioco)
    sys.exit()


def cambio_giocatore(colpo, giocatore, lista_navi1, lista_navi2, righe, colonne, opzioni, campo_battaglia1, campo_battaglia2, fine_gioco):
    if giocatore == 1:
        if colpo and opzioni == 0:
            print('\nSpara ancora!')
            colpo, fine_gioco, giocatore = sparo(lista_navi2, righe, colonne, campo_battaglia2, giocatore, fine_gioco)
        else:
            player = 2
            print(f'\nPassa il computer a {player}')
            colpo, fine_gioco, giocatore = sparo(lista_navi1, righe, colonne, campo_battaglia1, giocatore, fine_gioco)
    else:
        if colpo and opzioni == 0:
            print(f'\nSpara ancora!')
            colpo, fine_gioco, player = sparo(lista_navi1, righe, colonne, campo_battaglia1, giocatore, fine_gioco)
        else:
            player = 1
            print(f'\nPassa il computer a {player}')
            colpo, fine_gioco, giocatore = sparo(lista_navi2, righe, colonne, campo_battaglia2, giocatore, fine_gioco)
    return colpo, fine_gioco, giocatore


def vittoria(lista_navi):
    j = 0
    viva = False
    while j < len(lista_navi) and not viva:
        if not (tipo_nave.Nave.nave_affondata(lista_navi[j])):
            viva = True
        j = j + 1
    return not viva
