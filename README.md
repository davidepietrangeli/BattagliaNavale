# Battaglia Navale
 Programma che implementa il gioco della bataglia navale nella versione user vs user. Progetto eseguito per l'esame di Programmazione dell'Università Campus Bio-Medico di Roma.
 
 # Come iniziare il gioco
 ## Guida al gioco
 Il programma permette di giocare nella configurazione a 2 giocatori seguendo le regole di base del gioco.
 
 Per configurare il proprio campo di gioco, che consiste in una matrice vuota dove posizionare un numero predeterminato di navi caratterizzate da lunghezze differenti, applicare le seguenti regole:
 - la lunghezza della nave corrisponde ad un numero intero presente nel quadrato della matrice
 - ogni nave può essere posizionata orizzontalmente o verticalmente, interamente all'interno del campo di battaglia
 - due navi non possono essere adiacenti, ci deve essere sempre uno spazio tra una nave e l'altra
 
 Il gioco ha due modalità di alternanza del turno tra i due giocatori:
 - alternanza sistematica (un colpo per ognuno)
 - nel caso in cui si colpisce una nave avversario, l'utente può proseguire nello sparo finchè non manca una nave
 
 La grandezza del campo di gioco, il numero delle navi di ogni tipo e il modo di alternanza dei turni sono dei parametri che il programma deve inizialmente configurare e saranno gli stessi per entrambi i giocatori.
 
 Ogni giocatore, in accordo con l'alternanza dei turni di gioco, dovrà comunicare le coordinate di ogni colpo sparato e il programma comunicherà il risultato: mancata/colpita/affondata, fino a che il gioco non termina e viene proclamato il vincitore quando tutte le navi dell'avversario sono state affondate.
 
 ## Guida all'esecuzione
 Per eseguire lo script seguire i seguenti passaggi:
 
 - Inserire le righe (-r) e le colonne (-c) del campo di gioco, che devono essere un numero intero tra un minimo di 1 ad un massimo di 99. Se non indicati questi valori, il campo di gioco avrà una grandrezza paro a 9X9

```shell
Esempio di esecuzione del programma sul terminle del PC: 
python battaglianavale.py -r 6 -c 6
In questo modo il campo di gioco sarà una matrice 6X6
```
 
 - Scegliere il numero di ogni tipologia di nave: Portaerei (-s1) minimo 0 massimo 2, Corazzata (-s2) minimo 0 massimo 3, Sottomarino (-s3) minimo 0 massimo 4, Cacciatorpediniere (-s4) minimo 0 massimo 5, Sommergibile (-s5)  minimo 0 massimo 6. Se non indicato ogni tipologia di nave sarà pari a 1

```shell
Esempio di esecuzione del programma sul terminle del PC: 
python battaglianavale.py -s1 1 -s2 2 -s3 3 -s4 4 -s5 5
In questo modo il gioco avrà 1 Portaerei, 2 Corazzate, 3 Sottomarini, 4 Cacciatorpedinieri e 5 Sommergibili
```
 
 - Scegliere la variante di gioco che si vuole: 0 se dopo aver colpito una nave si continua il turno, 1 altrimenti. Se non indicato il programma sarà eseguito con il parametro 0

```shell
Esempio di esecuzione del programma sul terminle del PC: 
python battaglianavale.py -o 1
In questo modo dopo un colpo si passa il turno all'avversario
```
 
 # Autore
 Codice scritto da:
 Davide Pietrangeli
 -  

