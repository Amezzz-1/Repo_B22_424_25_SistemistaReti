import math
import random

# OPERATORI MATEMATICI 

num1 = 6 #Integer
num2 = 9.3 #Float

somma = num1 + num2
prodotto = num1 * num2
differenza = num1 - num2
quoziente = num1 / num2

print("==== Stampo i risultati ====")
print(f"Somma: {somma}")
print(f"Prodotto: {prodotto}")
print(f"Differenza: {differenza}")
print(f"Quoziente: {quoziente}")
print("============================")

# Occhio alla precisione della macchina. Perché mi mette un 4 dopo 15 cifre ?
calcolo = 0.1 + 0.2
print(calcolo)
print(round(calcolo,2))

calcolo2 = 6 / 9.3
print(calcolo2)
print(round(calcolo2, 7))

# Operatore Modulo o Resto della divisione (%)
mod1 = 4 % 2
print(f"Il resto di questa divisione vale: {mod1}")

mod2 = 4 % 3
print(mod2)

mod3 = 6 % 8
print(mod3)

mod4 = 255 % 3
print(mod4)

# Altri Operatori
# += Auto Incremento
miaVar = 1
# Voglio incrementare la miaVar di 5 
# miaVar = miaVar + 5
miaVar += 5
print(miaVar)

miaVar *= 3
print(miaVar)

miaVar /= 6
print(miaVar)

miaVar -= 1
print(miaVar)

# Elevamento a potenza
mioNum = 6

potenza1 = mioNum ** 2
print(f"La potenza di {mioNum} elevato a 2 vale {potenza1}")

radice1 = 9 ** 0.5
print(f"La radice di 9 vale {radice1}")

potenza2 = pow(5, 2) #pow() è una funziona matematica built-in
print(potenza2) 

radice2 = math.sqrt(81) #math è una libreria che va obbligatoriamente importata. Di solito tutti gli import avvengono in alto nella pagina o quantomeno prima di utilizzarli
print(radice2)

piGreco = math.pi
print(piGreco)

arrCeil = math.ceil(5.2) #6 Arrotonda all'intero superiore
arrFloor = math.floor(5.2)#5 Arrotonda all'intero inferiore

print(arrCeil)
print(arrFloor)

#Importo la libreria random per generare un numero casuale
numCas = random.random() #Estrare un float casuale tra 0.0 (compreso) e 1.0 (non compreso)
print(numCas)

numCas2 = random.randint(1,10) #Estrare un int casuale tra 1 e 10 (inclusi)
print(numCas2)

lancioDado = math.ceil( random.random() * 6 )
lancioDado = random.randint(1,6)
print(lancioDado)

# COSTANTI (di solito vengono denominate in MAIUSC )
PI_GRECO = 3.14
IVA = 0.22
C = 300000
MINUTI_IN_ORA = 60

#input (raccoglie un input utente)

nomeUtente = input("Come ti chiami ? ")
print(f"Ciao {nomeUtente}, benvenuto al corso di Sistemista Reti")

