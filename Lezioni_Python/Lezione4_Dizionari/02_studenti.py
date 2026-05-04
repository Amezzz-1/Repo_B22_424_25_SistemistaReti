# studenti è una lista di dizionari
studenti = [
    {"nome": "Mandeep", "eta": 29, "corso": "Sistemista Reti", "promosso": True},
    {"nome": "Alessandro", "eta": 27, "corso": "Sistemista Reti", "promosso": True},
    {"nome": "Karen", "eta": 22, "corso": "Sistemista Reti", "promosso": True},
    {"nome": "Amedeo", "eta": 25, "corso": "Sistemista Reti", "promosso": False},
    {"nome": "Dario", "eta": 26, "corso": "Sistemista Reti", "promosso": False}
]

for studente in studenti:
    promozione = ""
    if(studente["promosso"]):
        promozione = "Promosso"
    else:
        promozione = "Bocciato"

    print(f"Studente: {studente['nome']} , età: {studente['eta']} , valutazione: {promozione}")


# Dizionari Annidati
# rete è un dizionari di dizionari
rete = {
    "server1": {
        "ip": "192.168.1.2",
        "nome": "Server Back End",
        "os": "Ubuntu",
        "attivo": True
    },
    "server2": {
        "ip": "192.168.1.3",
        "nome": "Server Front End",
        "os": "Windows",
        "attivo": False
    },
    "server3":{
        "ip": "192.168.1.5",
        "os": "Ubuntu",
        "attivo": True,
        "proxy": {
            "navigazione": "limitata",
            "numero": 10,
            "versione": 2
        },
        "macchineConnesse": [
            {"MAC": "0001012jj", "nome": "macchina1", "aula": 3}, #0
            {"MAC": "0001013kk", "nome": "macchina2", "aula": 3}, #1
            {"MAC": "0001012ll", "nome": "macchina3", "aula": 3}, #2
        ]
    }
}

# Accedere alle sotto-proprietà
print(rete["server2"]["ip"])
print(rete["server2"]["os"])
print(rete["server3"]["attivo"])
print(rete["server3"]["proxy"]["versione"])
print(rete["server3"]["macchineConnesse"][2]["MAC"])

# Stampa tutte le macchine Connesse
for macchina in rete["server3"]["macchineConnesse"]:
    print(macchina["MAC"])