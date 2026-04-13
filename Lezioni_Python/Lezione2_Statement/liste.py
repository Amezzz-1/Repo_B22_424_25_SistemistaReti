# Le liste (alt: array) sono dei contenitori di elementi simili tra loro
# Le liste sono oggetti 0-based

mia_lista = []

numeri = [8, 4, 5, 2, 12, 123]
parole = ["Ciao", "Addio", "Buongiorno", "In bocca al lupo"]

array_misto = ["Dario", "Mennillo", 37, True, False] #inutile, perché non c'è corrispondenza chiave-value. 

#                  0       1        2        3         4
nomi_Studenti = ["Anna", "Laura", "Marco", "Luisa", "Laura"]
print(len(nomi_Studenti))

prima_pos = nomi_Studenti[0]
print(f"In prima posizione si trova {prima_pos}")

#                                   5       -  1 = 4
ultima_pos = nomi_Studenti[len(nomi_Studenti)- 1]
print(f"In ultima posizione c'è {ultima_pos}")

print(f"In seconda posizione si trova {nomi_Studenti[1]}")

print("Ciao",nomi_Studenti)

#Utilizzo un for-in (foreach)
for nome in nomi_Studenti:
    print("Ciao", nome)

print("===== STAMPO CON UN RANGE sugli indici====")
for i in range(len(nomi_Studenti)):
    print("Ciao", nomi_Studenti[i])

# Aggiorno gli elementi
nomi_Studenti[3] = "Pasquale"
print(nomi_Studenti)

#Ricerca con un filtro
counter = 0

for n in range(len(nomi_Studenti)):
    if nomi_Studenti[n] == "Laura":
        nomi_Studenti[n] = "Maria"

print(nomi_Studenti)

# Metodi delle liste
colori = ["rosso", "giallo", "verde", "blue", "viola"]

colori.append("rosa") #Aggancia al fondo
colori.insert(0, "nero") #con insert devo specificare la posizione
colori.insert(2, "viola")


print("Questi sono i colori\n", colori)
nuovoColore = input("Aggiungi un colore: \t")
colori.append(nuovoColore)
print(colori)