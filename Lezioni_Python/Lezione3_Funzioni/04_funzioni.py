import random


# Dichiaro la funzione
def benvenuto():
    print("Ciao Dario")
    numeroCasuale = random.randint(1,100)
    print(f"Oggi il tuo numero fortunato è il {numeroCasuale}")


# eseguo la funzione
benvenuto()

# serverAttivi = []

# # Le funzioni possono avere dei parametri in ingresso
# def descrivi_server(nome, ip):
#     if(ip == "192.168.1.25"):
#         print("Attenzione, questo server non esiste più")
#         return False
#     else:
#         print(f"Server: {nome} - IP: {ip}")
#         return True

# # descrivi_server("WebServer", "192.168.1.20")
# # descrivi_server("DBServer", "192.168.1.10")
# # descrivi_server("BEServer", "192.168.1.25")


# def accendi_server():
#     while len(serverAttivi) <= 3:
#         ip_server = input("Inserisci ip del server: \n")
#         nome_server = input("Inserisci il nome del server: \n")    
#         if descrivi_server(nome_server, ip_server):
#             server = ip_server + " - " + nome_server
#             serverAttivi.append(server)


# accendi_server()


# Funzioni con return

def scrivi_nome(nome):
    descrizione = "Il tuo nome è " + nome
    return descrizione #Questa funzione sta restituendo una stringa

# Se ho una funzione con return sono obbligato a raccogliere quel valore
print(scrivi_nome("Anna"))

def stampa_numero():
    numero_casuale = random.randint(1,20)
    return numero_casuale

def controlla_numero():
    numero_da_controllare = stampa_numero() #raccolgo in una variabile il risultato di una funzione

    if numero_da_controllare >= 10:
        print(f"Ti trovi sopra il 10, il numero è {numero_da_controllare}")
    else:
        print(f"Ti trovi sotto il 10, il numero è {numero_da_controllare}")

controlla_numero()



def lancia_moneta():
    testa_croce = random.randint(1,100)
    print(f"Il numero di controllo è: {testa_croce}")
    if testa_croce % 2 == 0 :
        return True
    else:
        return False

def controlla_moneta():
    if lancia_moneta():
        print("E' uscito testa")
    else:
        print("E' uscito croce")

controlla_moneta()

def saluta_qualcuno(nome="Pippo", cognome="Rossi"):
    return f"Ciao {nome} {cognome}"

print(saluta_qualcuno("Anna", "Verdi"))

def saluta_studente(nome, cognome):
    return f"Nome: {nome} - Cognome: {cognome}"
    
print(saluta_studente("Luisa", "Bianchi"))
print(saluta_studente("Bianchi", "Luisa"))
print(saluta_studente(cognome="Bianchi", nome="Luisa"))

# Parametri variabili
def somma_tutto(*numeri):
    totale = 0
    for n in numeri:
        totale += n
    print(f"{totale}")

# somma_tutto(4,5,6)
somma_tutto( 1,50, 4, 9 ,100,1,)

