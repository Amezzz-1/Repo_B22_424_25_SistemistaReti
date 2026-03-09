# Commento
# In python dichiaro una variabile senza necessità di dichiararne il tipo
# Tipi di dato: String, Number (Integer, Float), Boolean (True, False)

# nomeVariabile = valore
mioNome = "Dario" #Questa è una String
mioCognome = "Mennillo"
numeroFortunato = 1000 #Questo è un Number (Integer)
presenza = True #Questo è un Boolean
piGreco = 3.14 #Questo è un Number(Float)

#Concatenazione tra stringhe
#Con print() stampo nel terminale di VSCode
# 1° Modo
print("Ciao, mi chiamo", mioNome, mioCognome)

# 2° Modo
print("Ciao, mi chiamo " + mioNome + " " + mioCognome)

# 3° Modo - concatenazione con formattazione
print(f"Ciao, mi chiamo {mioNome} {mioCognome}. Il mio numero fortunato è il {numeroFortunato}. Il pi greco vale {piGreco}")