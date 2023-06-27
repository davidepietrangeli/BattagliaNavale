# Import della libreria 'sys' per interagire con il sistema operativo e l'interprete
import sys
# Import dei file contenuti nel progetto globale
import tipo_nave
import utile


# Funzione che crea il campo di gioco e svolge il posizionamento delle navi su di esso
# Restituisce il campo di gioco con la lista delle navi
def crea_campo(righe, colonne, tipo_lista):
    # Creo il campo di gioco come una matrice di righe x colonne inizializzata con zeri
    campo = [[0] * colonne for _ in range(righe)]
    # Creo lista vuota che conterrà le istanze delle navi posizionate
    lista_navi = []
    # Per ogni valore 'i' in 'tipo_lista' la funzione richiede all'utente l'inserimento delle coordinate e dell'orientamento
    for i in tipo_lista:
        # Stampo un messaggio all'utente specifico per il tipo di nave
        utile.messaggio_utente(i)
        inserimento_corretto = False
        prove = 0
        # Gestisco gli eventuali errori
        while not inserimento_corretto:
            try:
                # Inserimento di riga e colonna che associo all'attributo 'input_val'
                input_val = input(f'\nInserisci riga e colonna (es. 1 2): ')
                # Funzione 'map' che mi separa i due valori di 'input_val' e me li salva nell'attributo 'riga_partenza' e 'colonna_partenza'
                riga_partenza, colonna_partenza = map(int, input_val.split())
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

            # Chiamo la funzione 'controllo_posizionamento_orizzontale_nave' per controllare se è possibile posizionare la nave
            if orientamento == 'o':
                error, coordinate = controllo_posizionamento_orizzontale_nave(righe, colonne, campo, riga_partenza, colonna_partenza, i)
                if not error:
                    inserimento_corretto = True
            # Chiamo la funzione 'controllo_posizionamento_verticale_nave' per controllare se è possibile posizionare la nave
            else:
                error, coordinate = controllo_posizionamento_verticale_nave(righe, colonne, campo, riga_partenza, colonna_partenza, i)
                if not error:
                    inserimento_corretto = True

            # Chiamo la funzione 'stampa_campo' per visualizzare il campo di gioco
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
        if i == 6:
            nave = tipo_nave.Portaerei(orientamento, colonna_partenza, riga_partenza, coordinate)
        elif i == 5:
            nave = tipo_nave.Corazzata(orientamento, colonna_partenza, riga_partenza, coordinate)
        elif i == 4:
            nave = tipo_nave.Sottomarino(orientamento, colonna_partenza, riga_partenza, coordinate)
        elif i == 3:
            nave = tipo_nave.Cacciatorpediniere(orientamento, colonna_partenza, riga_partenza, coordinate)
        elif i == 2:
            nave = tipo_nave.Sommergibile(orientamento, colonna_partenza, riga_partenza, coordinate)
        # Aggiungo l'istanza della nave alla lista 'lista_navi'
        lista_navi.append(nave)
    return lista_navi


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


# Funzione che verifica se è possibile posizionare una nave in modo orizzontale sul campo di gioco
# Restituisco il valore di 'error' e la lista 'coordinate'
# Parametri:
#   'righe': input dato dall'utente per il numero di righe del campo di gioco
#   'colonne': input dato dall'utente per il numero di colonne del campo di gioco
#   'campo': campo di gioco
#   'riga_partenza': il punto di partenza della riga
#   'colonna_partenza': il punto di partenza della colonna
#   'lunghezza': lunghezza della nave
#   'return': parametro logico che è True se vi è un errore, altrimenti è False
def controllo_posizionamento_orizzontale_nave(righe, colonne, campo, riga_partenza, colonna_partenza, lunghezza):
    error = False
    # Eseguo un controllo per verificare che la colonna di partenza sommata alla lunghezza della nave -1 sia all'interno del campo
    if colonna_partenza + lunghezza - 1 <= colonne:
        i = colonna_partenza - 1
        # Eseguo ciclo while che continua fintanto che 'i' è minore della condizione impostata precedentemente e non si è verificato nessun errore
        while i < colonna_partenza + lunghezza - 1 and not error:
            # Verifico se la posizione corrente del campo nella riga 'riga_partenza - 1' e nella colonna 'i' è uguale a 1
            if campo[riga_partenza - 1][i] == 1:
                print("\u001b[31m\n\nErrore! Posizione già occupata da una nave\033[0m")
                error = True
                continue
            # Eseguo controllo per verificare che la 'riga_partenza' è uguale a 1
            if riga_partenza == 1:
                # Eseguo controllo per verificare se la posizione corrente nella riga 'riga_partenza' nella colonna 'i' è uguale a 1
                if campo[riga_partenza][i] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            # Eseguo un controllo per verificare se 'riga_partenza' è uguale al numero di righe nel campo
            if riga_partenza == righe:
                # Eseguo controllo per verificare se la posizione corrente nella riga 'riga_partenza - 2' e nella colonna 'i' è uguale a 1
                if campo[riga_partenza - 2][i] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            # Eseguo un controllo per verificare se 'riga_partenza' non è né 1 né uguale al numero di righe nel campo
            if 1 < riga_partenza < righe:
                # Verifico se la posizione corrente nella riga 'riga_partenza' e nella colonna 'i' è uguale a 1 oppure se la posizione nella riga 'riga_partenza - 2' e nella colonna 'i' è uguale a 1
                if campo[riga_partenza][i] == 1 or campo[riga_partenza - 2][i] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            # Eseguo un controllo per verificare se 'colonna_partenza' non è uguale a 1
            if colonna_partenza != 1:
                # Verifico se la posizione nella riga 'riga_partenza - 1' e nella colonna 'colonna_partenza - 2' è uguale a 1
                if campo[riga_partenza - 1][colonna_partenza - 2] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            # Eseguo un controllo per verificare se 'colonna_partenza + lunghezza - 2' non è uguale all'ultima colonna '(colonne - 1)' nel campo
            if colonna_partenza + lunghezza - 2 != colonne - 1:
                # Verifico se la posizione nella riga 'riga_partenza - 1' e nella colonna 'colonna_partenza + lunghezza - 1' è uguale a 1
                if campo[riga_partenza - 1][colonna_partenza + lunghezza - 1] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            #  Incremento il valore di 'i' di 1 per passare alla colonna successiva
            i = i + 1
        # Dopo il ciclo while eseguo un controllo per verificare se 'error' è ancora 'False', ovvero se non si è verificato alcun errore
        if not error:
            # Posizione valida quindi creo lista vuota 'coordinate' per memorizzare le coordinate della nave
            coordinate = []
            for i in range(colonna_partenza - 1, colonna_partenza + lunghezza - 1):
                # Imposto il valore della posizione corrispondente nel campo a 1 per indicare la presenza di una nave
                campo[riga_partenza - 1][i] = 1
                # Aggiungo le coordinate alla lista
                coordinate.append([riga_partenza, i + 1])
            return error, coordinate
    else:
        error = True
        print("\u001b[31m\n\nErrore! La nave è fuori dal campo\033[0m")
    return error, None


# Funzione che verifica se è possibile posizionare una nave in modo verticale sul campo di gioco
# Restituisco il valore di 'error' e la lista 'coordinate'
# Parametri:
#   'righe': input dato dall'utente per il numero di righe del campo di gioco
#   'colonne': input dato dall'utente per il numero di colonne del campo di gioco
#   'campo': campo di gioco
#   'riga_partenza': il punto di partenza della riga
#   'colonna_partenza': il punto di partenza della colonna
#   'lunghezza': lunghezza della nave
#   'return': parametro logico che è True se vi è un errore, altrimenti è False
def controllo_posizionamento_verticale_nave(righe, colonne, campo, riga_partenza, colonna_partenza, lunghezza):
    error = False
    # Eseguo un controllo per verificare che la riga di partenza sommata alla lunghezza della nave -1 sia all'interno del campo
    if riga_partenza + lunghezza - 1 <= righe:
        i = riga_partenza - 1
        # Eseguo ciclo while che continua fintanto che 'i' è minore della condizione impostata precedentemente e non si è verificato nessun errore
        while i < riga_partenza + lunghezza - 1 and not error:
            # Verifico se la posizione corrente del campo nella riga 'i' e nella colonna 'colonna_partenza - 1' è uguale a 1
            if campo[i][colonna_partenza - 1] == 1:
                print("\u001b[31m\n\nErrore! Posizione già occupata da una nave\033[0m")
                error = True
                continue
            # Eseguo controllo per verificare che la 'colonna_partenza' è uguale a 1
            if colonna_partenza == 1:
                # Eseguo controllo per verificare se la posizione corrente nella riga 'i' nella colonna 'colonna_partenza' è uguale a 1
                if campo[i][colonna_partenza] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            # Eseguo un controllo per verificare se 'colonna_partenza' è uguale al numero di colonne nel campo
            if colonna_partenza == colonne:
                # Eseguo controllo per verificare se la posizione corrente nella riga 'i' e nella colonna 'colonna_partenza - 2' è uguale a 1
                if campo[i][colonna_partenza - 2] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            # Eseguo un controllo per verificare se 'colonna_partenza' non è né 1 né uguale al numero di colonne nel campo
            if 1 < colonna_partenza < colonne:
                # Verifico se la posizione corrente nella riga 'i' e nella colonna 'colonna_partenza' è uguale a 1 oppure se la posizione nella riga 'i' e nella colonna 'colonna_partenza - 2' è uguale a 1
                if campo[i][colonna_partenza] == 1 or campo[i][colonna_partenza - 2] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            # Eseguo un controllo per verificare se 'riga_partenza' non è uguale a 1
            if riga_partenza != 1:
                # Verifico se la posizione nella riga 'riga_partenza - 2' e nella colonna 'colonna_partenza - 1' è uguale a 1
                if campo[riga_partenza - 2][colonna_partenza - 1] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            # Eseguo un controllo per verificare se 'riga_partenza + lunghezza - 2' non è uguale all'ultima riga '(righe - 1)' nel campo
            if riga_partenza + lunghezza - 2 != righe - 1:
                # Verifico se la posizione nella riga 'riga_partenza + lunghezza - 1' e nella colonna 'colonna_partenza - 1' è uguale a 1
                if campo[riga_partenza + lunghezza - 1][colonna_partenza - 1] == 1:
                    print("\u001b[31m\n\nErrore! La nave è adiacente\033[0m")
                    error = True
                    continue
            #  Incremento il valore di 'i' di 1 per passare alla riga successiva
            i = i + 1
        # Dopo il ciclo while eseguo un controllo per verificare se 'error' è ancora 'False', ovvero se non si è verificato alcun errore
        if not error:
            # Posizione valida quindi creo lista vuota 'coordinate' per memorizzare le coordinate della nave
            coordinate = []
            # Eseguo ciclo for nel range dalla riga di partenza diminuita di 1 alla riga di partenza sommata alla lunghezza della nave diminuita di 1
            for i in range(riga_partenza - 1, riga_partenza + lunghezza - 1):
                # Imposto il valore della posizione corrispondente nel campo a 1 per indicare la presenza di una nave
                campo[i][colonna_partenza - 1] = 1
                # Aggiungo le coordinate alla lista
                coordinate.append([i + 1, colonna_partenza])
            return error, coordinate
    else:
        print("\u001b[31m\n\nErrore! La nave è fuori dal campo\033[0m")
        error = True
    return error, None
