# @author PIETRANGELI DAVIDE:
# Import del modulo 'os' per interagire con il sistema operativo in modo tale da pulire lo schermo del terminale
import os
# Import dei file contenuti nel progetto globale
import campo
import inputs
import giocatore
import utile

# Chiamo la funzione 'inizializza_parser()' del modulo 'inputs' per inizializzare un parser degli argomenti della riga di comando
args = inputs.inizializza_parser()
# Chiamo la funzione 'controllo_parser()' del modulo 'inputs' per controllare e gestire gli argomenti passati al programma in base alle regole definite nel parser
inputs.controllo_parser(args)

# Chiamo la funzione 'crea_nave_tipo_lista()' del modulo 'utile' per creare una lista di tipi di navi in base agli argomenti passati al programma
tipo_lista = utile.crea_nave_tipo_lista(args.portaerei, args.corazzata, args.sottomarino, args.cacciatorpediniere, args.sommergibile)

#  Chiamo la funzione 'crea_campo()' del modulo 'campo' per creare il campo di gioco per il giocatore 1
lista_navi1 = campo.crea_campo(args.righe, args.colonne, tipo_lista)
input('\n\nPremi INVIO e passa il computer al prossimo giocatore:')
# Eseguo il comando 'cls' per pulire il terminale in modo da nascondere il posizionamento delle navi
os.system('cls' if os.name == 'nt' else 'clear')

#  Chiamo la funzione 'crea_campo()' del modulo 'campo' per creare il campo di gioco per il giocatore 1
lista_navi2 = campo.crea_campo(args.righe, args.colonne, tipo_lista)
input('\n\nPremi INVIO e passa il computer al prossimo giocatore per iniziare il gioco:')
# Eseguo il comando 'cls' per pulire il terminale in modo da nascondere il posizionamento delle navi
os.system('cls' if os.name == 'nt' else 'clear')

# Crea una lista bidimensionale di dimensioni 'args.righe' x 'args.colonne' contenente il carattere '-' come valore iniziale
# Questa lista rappresenta il campo di battaglia del giocatore 1
campo_battaglia1 = [['-'] * args.colonne for x in range(args.righe)]
# Questa lista rappresenta il campo di battaglia del giocatore 2
campo_battaglia2 = [['-'] * args.colonne for x in range(args.righe)]
# Chiamo la funzione 'inizio_gioco()' del modulo 'giocatore', passando i parametri necessari per avviare il gioco
# Questa funzione gestirà il flusso del gioco e le azioni dei giocatori
giocatore.inizio_gioco(lista_navi1, lista_navi2, args.righe, args.colonne, args.opzioni, campo_battaglia1, campo_battaglia2)
