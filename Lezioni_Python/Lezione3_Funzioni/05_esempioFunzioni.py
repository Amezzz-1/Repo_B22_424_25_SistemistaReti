# Crea uno script per la gestione del magazzino.
# Funz1: aggiungi_prodotto(magazzino, nome, quant)
# Funz2: rimuovi_prodotto(magazzino, nome, quant)
# Funz3: stampa_magazzino(magazzino)
# ATT: lavora con un unico magazzino (String)

magazzinoPrincipale = "Immaginazione e Lavoro"
prodotti = []

def aggiungi_prodotto(magazzino, nome, quantita):
    quantitaTotale = 0
    if magazzino == magazzinoPrincipale:
        prodotti.append(f"{nome} x {quantita}")
        quantitaTotale += quantita
    else:
        print("Magazzino non individuato")

def stampa_magazzino():
    print(f"Magazzino: {magazzinoPrincipale}")

    if len(prodotti) > 0:
        for p in prodotti:
            print(p)
    else:
        print("Mi spiace, non ci sono prodotti in questo magazzino")


def rimuovi_prodotto(nomeProd):
    if len(nomeProd) >= 4:
        for p in prodotti:
            if p.startswith(nomeProd):
                prodotti.remove(p)
            else:
                print("Mi spiace, nonc'è un prodotto con questo nome")
    else:
        print("Ci sono poche lettere per far avvenire la ricerca")



aggiungi_prodotto("Immaginazione e Lavoro", "Pc", 1)
aggiungi_prodotto("Immaginazione e Lavoro", "Scrivania", 2)
aggiungi_prodotto("Immaginazione e Lavoro", "Mouse", 10)

rimuovi_prodotto("Mo")

stampa_magazzino()