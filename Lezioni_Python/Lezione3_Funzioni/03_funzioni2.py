def descrivi_persona(nome, eta, citta):
    print(f"Mi chiamo {nome}, ho {eta} anni e vivo a {citta}")
#test

# descrivi_persona("Napoli", "Dario", 36) #La posizione dei parametri è fondamentale

#posso passare i parametri in ordine differente solo ridefinendoli
descrivi_persona(citta="Napoli", nome="Dario", eta=36)


#posso definire una funzione con dei parametri di default
def descrivi_studente(nome="Paolo", corso="Sistemista", citta="Torino"):
    print(f"Ciao, mi chiamo {nome}, abito a {citta} e frequento il corso di {corso}")

descrivi_studente()
descrivi_studente("Anna", "WEB", "Milano")


#Funzioni con parametri variabili (accettano un numero variabile di parametri)

def somma_tutti(*numeri):
    totale = 0
    for num in numeri:
        totale += num
    
    return totale



print("La somma dei numeri vale: ", somma_tutti(1,5,6,3,23,22,44,7))
print("La somma dei numeri vale: ", somma_tutti(1,5,6,))

def saluta_qualcuno(*nomi):
    for nome in nomi:
        print(f"Ciao {nome}")

saluta_qualcuno("Marta", "Mario", "Francesca")