# Lista Comandi Github

## cd - Change Directory
Da utilizzare con percorsi assoluti o relativi
- `~` rappresenta la mia home directory
- `/` root directory
Tutte le volte che uso questi due simboli sto navigando con un percorso assoluto.

Spiegazione dei simboli o opzioni per i comandi:
- `.` directory corrente
- `..` directory genitore
- `~` home directory 
- `/` root directory
- `-` directory precedente

### Tipi di File 
Quando lancio il comando `ls -l` ottengo vari risultati
- drwxrwxrwx 1 root ....

Primo Carattere
- `d` = directory
- `-` = file generici
- `l` = link, puntano ad un altro file
- `s` = socket 
- `p` = pipe
- `b` = block file
- `c` = character file

Permessi `rwxrwxrwx`. Si dividono in 3 parti da 3 caratteri
- i primi 3 per lo user
- i secondi 3 per il gruppo
- i terzi per gli special 

Nomenclature
- `r` readable
- `w` writable
- `x` executable

Quando incontro un `-` vuol dire che quel particolare permesso non è disponibile per quella categoria.

Esempio: `rwxrw-r--` --> l'utente può fare tutto, il gruppo solo leggere/scrivere e non eseguire, gli special solo leggere


## Comando Copia `cp`

```linux
cp source destinazione
```

ATT: anche cp può essere un comando distruttivo poiché posso mandarlo in sovrascrittura

Per chiedere la sovrascrittura lanciare `cp -i src dest`
Per evitarla completamente lanciare `cp -n src dest`

Copiare una cartella
`cp -r srcFolder destFolder`


## Comando Rimuovi `rm`
```linux
rm source
```
ATT: il comando rm è un comando distruttivo, attento ad utilizzarlo

Come rimuovere una cartella
```linux
rm -r srcFolder
```


## Comando Sposta, Muovi `mv`
`mv src dest`
Può essere utilizzato anche per rinominare un file `mv src dest/nuovoNome`.
Anche in questo caso `-i` ,  `-v` , `-n` funzionano
Il `-r` non serve col il move per spostare una cartella

Esempio:
```linux
mv ./Downloads/Videos/ ./
```
## Creare un file `touch dest/nomeFile`
# Comandi Linux: Creare più file (touch)

## File vuoti multipli

| Obiettivo                                 | Comando                                      | Risultato                                          |
|-------------------------------------------|----------------------------------------------|----------------------------------------------------|
| Più file sullo stesso livello             | `touch file1.txt file2.txt file3.js`        | Crea 3 file vuoti nella cartella corrente          |
| Serie con numeri                          | `touch esercizio{1,2,3}.js`                 | `esercizio1.js`, `esercizio2.js`, `esercizio3.js`  |
| Serie numerata con zeri                   | `touch soluzione_{01..05}.py`               | `soluzione_01.py` … `soluzione_05.py`              |

## Creazione multipla **in cartella specifica**

| Obiettivo                                 | Comando                                      | Note                                               |
|-------------------------------------------|----------------------------------------------|----------------------------------------------------|
| File in cartella esistente                | `touch /percorso/cartella/*.txt`             | Crea file nella cartella specifica                 |
| File con cartella (crea cartella se manca)| `mkdir -p lezioni/esercizi && touch lezioni/esercizi/es{1..3}.js` | Crea struttura + file |
| File multipli in sottocartella            | `touch corso/lezioni/esercizio{1,2,3}.py`   | Crea file dentro `corso/lezioni/`                  |

## Esempi pronti da copiare

```bash
# File base
touch file1.txt file2.txt file3.js

# Serie numerate
touch esercizio{1,2,3}.js
touch soluzione_{01..05}.py

# In cartelle specifiche
touch corso/lezioni/esercizio{1,2,3}.py
touch progetto/js/componente{1..4}.js

# Struttura completa (cartelle + file)
mkdir -p corso/{lezioni,esercizi}/soluzioni
touch corso/lezioni/lez_{01..10}.md
touch corso/esercizi/es_{01..10}.py
touch corso/esercizi/soluzioni/sol_{01..10}.py
```

## Creare una cartella `mkdir dest/nomeDir`
```bash
# Più cartelle sullo stesso livello
mkdir cartella1 cartella2 cartella3

# Serie con numeri
mkdir progetto{1,2,3}

# Serie numerata con zeri
mkdir lezione_{01..10}

# Cartelle e sottocartelle (crea genitore se manca)
mkdir -p genitore/figlio1 genitore/figlio2

# Struttura corso con brace expansion
mkdir -p corso/{lezioni,esercizi,soluzioni}
```


# Lettura file di testo 
- `less nomefile.txt`
- `more nomefile.txt`
- `head` per leggere la parte iniziale di un testo
- `tail` per leggere la parte finale di un testo

Per poter scorrere facilmente il testo utilizza:
- `spazio` per scendere giù di una pagina
- `B` per salire
- `Enter` scende giù di 1 riga
- `q` chiude, quit


# Scrittura file di testo
- opzione 1: utilizzo degli stdInput stdOutput stdError
```linux
ls ./ > mioFile.txt (scrive tutto l'output che va a buon fine)
ls ./prova 2> mioFile.txt (scrive solo l'output di errore)
ls ./ &> mioFile.txt (scrive tutto)
cat > mioFile.txt (scrive tutto ciò che io digito come input: ctrl+c per terminare)
``` 

