# I dizionari sono delle strutture che permettono di registrare dei dati in formato coppia (chiave - valore). Possiamo accedere ai dizionare attraverso la chiave

# Liste
studenti = ["Marizio", "Alessandro", "Mandeep", "Angelica", "Karen"]

studente = {
    "nome": "Mandeep",
    "età": 29,
    "corso": "Sistemista Reti",
    "presenza": True
}

# Accedo al valore richiamando la chiave
print("Il nome dello studente è: " + studente["nome"])
print(f"Età: {studente["età"]}")
print(f"Corso Attuale: {studente["corso"]}")
print(f"Presenza: {studente["presenza"]}")
# print(f"Chiave non esistente: {studente["cognome"]}") #ERRORE: la chiave non esiste
print(studente)

# Metodo di richiamo indiretto
print(studente.get("nome"))
print(studente.get("cognome")) #NONE
# Posso gestire la non esistenza di una chiave attraverso il secondo paramentro passato al metodo get
print(studente.get("cognome", "cognome non inserito"))

# Aggiungo una chiave con un valore
studente["citta"] = "Torino"

# Cambio il valore di una chiave
studente["presenza"] = False

# Rimuovo una chiave
studente.pop("corso")

# Controllo se esiste una chiave
if "nome" in studente:
    print(f"La chiave cercata esiste e vale {studente["nome"]}")

print(studente)

# Iterazione sulle chiavi
for key in studente: #fornisce la lista delle chiavi
    print(key)

# Iterazione sui valori
for val in studente.values(): #fornisce la lista dei valori
    print(val)

# Iterazione su chiavi e valori
for key, val in studente.items(): #fornisce la lista delle coppie
    print(f"{key} : {val}")


