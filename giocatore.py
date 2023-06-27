# Import della libreria 'sys' per interagire con il sistema operativo e l'interprete
import sys
# Import dei file contenuti nel progetto globale
import tipo_nave
import campo
import utile


# Parametri:
#   'lista_navi1, 'lista_navi2': le liste che rappresentano le navi del giocatore 1 e 2
#   'righe', 'colonne': il numero di righe e colonne del campo di battaglia
#   'opzioni': la variabile opzionale di gioco che può essere o 1 o 0
#   'campo_battaglia1', 'campo_battaglia2': i campi di battaglia del giocatore 1 e 2
# Funzione che gestisce l'inizio di gioco e l'iterazione dei turni tra i due giocatori
def inizio_gioco(lista_navi1, lista_navi2, righe, colonne, opzioni, campo_battaglia1, campo_battaglia2):
    print("\n\n\n\n\n\nGiocatore 1 inizia il gioco!")
    # Chiamo il metodo 'sparo' con i parametri corrispondenti per consentire al Giocatore 1 di effettuare un colpo sul campo di battaglia del Giocatore 2
    colpo, fine_gioco, giocatore = sparo(lista_navi2, righe, colonne, campo_battaglia2, 1, fine_gioco=False)
    # Entro in un ciclo while che continua finché 'fine_gioco' è False
    while not fine_gioco:
        # Chiamo il metodo 'cambio_giocatore' con i parametri corrispondenti per gestire il cambio del giocatore corrente
        colpo, fine_gioco, giocatore = cambio_giocatore(colpo, giocatore, lista_navi1, lista_navi2, righe, colonne, opzioni, campo_battaglia1, campo_battaglia2, fine_gioco)
    sys.exit()


# Parametri:
#   'colpo': parametro che rappresenta l'esito del colpo sparato
#   'giocatore': identificatore del giocatore corrente
#   'lista_navi1, 'lista_navi2': le liste che rappresentano le navi del giocatore 1 e 2
#   'righe', 'colonne': il numero di righe e colonne del campo di battaglia
#   'opzioni': la variabile opzionale di gioco che può essere o 1 o 0
#   'campo_battaglia1', 'campo_battaglia2': i campi di battaglia del giocatore 1 e 2
#   'fine_gioco': una variabile booleana impostata a False, che viene passata True solo quando vi è la vittoria di un giocatore
# Funzione che gestisce il cambio turno tra i giocatori
# Restituisce una tupla sull'esito del colpo, se il gioco è terminato e l'identificazione del giocatore corrente
def cambio_giocatore(colpo, giocatore, lista_navi1, lista_navi2, righe, colonne, opzioni, campo_battaglia1, campo_battaglia2, fine_gioco):
    if giocatore == 1:
        if colpo and opzioni == 0:
            print('\nSpara ancora!')
            #  Chiamo il metodo 'sparo' per consentire al giocatore corrente di effettuare un colpo
            colpo, fine_gioco, giocatore = sparo(lista_navi2, righe, colonne, campo_battaglia2, giocatore, fine_gioco)
        else:
            # Se le condizioni non sono state soddisfatte, significa che è il turno del giocatore 2
            giocatore = 2
            print(f'\n\n\n\n\n\n\n\n\n\nPassa il computer al giocatore {giocatore}')
            #  Chiamo il metodo 'sparo' per consentire al giocatore 2 di effettuare un colpo
            colpo, fine_gioco, giocatore = sparo(lista_navi1, righe, colonne, campo_battaglia1, giocatore, fine_gioco)
    else:
        if colpo and opzioni == 0:
            print(f'\nSpara ancora!')
            colpo, fine_gioco, player = sparo(lista_navi1, righe, colonne, campo_battaglia1, giocatore, fine_gioco)
        else:
            # Se le condizioni non sono state soddisfatte, significa che è il turno del giocatore 1
            giocatore = 1
            print(f'\n\n\n\n\n\n\n\n\n\nPassa il computer al giocatore {giocatore}')
            #  Chiamo il metodo 'sparo' per consentire al giocatore 1 di effettuare un colpo
            colpo, fine_gioco, giocatore = sparo(lista_navi2, righe, colonne, campo_battaglia2, giocatore, fine_gioco)
    return colpo, fine_gioco, giocatore


# Parametri:
#   'lista_navi': una lista che rappresenta le navi presenti nel gioco
#   'righe', 'colonne': il numero di righe e colonne del campo di battaglia
#   'campo_battaglia': il campo, in forma matriciale, in cui si svolge il gioco
#   'giocatore': l'identificatore del giocatore che sta effettuando lo sparo
#   'fine_gioco': una variabile booleana che indica se il gioco è terminato
# Funzione che permette per il giocatore di sparare un colpo
# Restituisce una tupla sull'esito del colpo, se il gioco è terminato e l'identificazione del giocatore corrente
def sparo(lista_navi, righe, colonne, campo_battaglia, giocatore, fine_gioco):
    colpo = False
    # Stampo il campo di battaglia utilizzando il metodo 'stampa_campo' del modulo 'campo' con il campo di battaglia e le dimensioni fornite
    campo.stampa_campo(campo_battaglia, righe, colonne)
    # Utilizzo il metodo 'scegli_controlla_punto_sparo' del modulo 'utile' per ottenere le coordinate di un punto di sparo valido
    riga_sparo, colonna_sparo = utile.scegli_controlla_punto_sparo(righe, colonne, campo_battaglia)
    for i in lista_navi:
        # Per ogni nave, verifico se la nave è stata colpita utilizzando il metodo 'nave_colpita'
        if tipo_nave.Nave.nave_colpita(i, riga_sparo, colonna_sparo):
            colpo = True
            # Segno il punto di colpo nel campo di battaglia impostando l'elemento corrispondente a 'X'
            campo_battaglia[riga_sparo - 1][colonna_sparo - 1] = 'X'
            # Verifico se la nave è stata affondata utilizzando la funzione 'nave_affondata' della classe 'Nave'
            if tipo_nave.Nave.nave_affondata(i):
                #  Se la nave è affondata, verifico anche se la vittoria è stata raggiunta chiamando la funzione 'vittoria'
                if vittoria(lista_navi):
                    print(f'\n\n\n\n\n\n\n\n\n\n\nCOMPLIMENTI!'
                          f'\n\nIl giocatore {giocatore} ha vinto la partita! :)')
                    fine_gioco = True
                else:
                    print('\nHai colpito e affondato una nave!')
            else:
                print('\nNave colpita!')
    if not colpo:
        print('\nNave mancata!')
        # Segno il punto nel campo di battaglia impostando l'elemento corrispondente a 'O'
        campo_battaglia[riga_sparo - 1][colonna_sparo - 1] = 'O'
    return colpo, fine_gioco, giocatore


# Parametri:
#   'lista_navi': una lista che rappresenta le navi presenti nel gioco
# Funzione che sancisce la vittoria di un giocatore
# Restituisce il valore negato di 'viva'
# Se tutte le navi sono affondate, 'viva = False' e quindi il metodo restituirà 'True' che indicherà la vittoria
def vittoria(lista_navi):
    j = 0
    viva = False
    while j < len(lista_navi) and not viva:
        # Verifico se la nave nella posizione 'j' non è affondata utilizzando il metodo 'nave_affondata'
        if not (tipo_nave.Nave.nave_affondata(lista_navi[j])):
            # Se la nave non è affondata imposta il valore 'viva' a True
            viva = True
        j = j + 1
    return not viva
