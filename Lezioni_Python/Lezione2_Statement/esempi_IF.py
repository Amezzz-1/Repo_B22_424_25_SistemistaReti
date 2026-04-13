#Es1. Puoi accedere al club se sei maggiorenne e hai un doc valido

#Es2. Username e password. Chiedi all'utente entrambi i dati. Se sono user == "admin" e pass == "1234" l'utente può accedere

#Es3. Dato un certo numero verifica se si trova tra 20 e 100 oppure se si trova tra 50 e 200

#Es4. Numeri pari e dispari. Verifica se un numero fornito da un utente è pari o dispari

#Es. Gioco dei dadi. Lancia 2 dadi (numero casuale tra 1 e un numero scelto dall'utente. Faccio scegliere all'utente il numero di facce del dado). Se i due numeri sono uguali l'utente vince, altrimenti perde.

from random import Random

facce = int(input("Di quante facce saranno i tuoi dadi ?\n"))

dado1 = Random.randint(1, facce)
dado2 = Random.randint(1, facce)

if dado1 == dado2:
    print("Hai vinto !")
else:
    print("Hai perso !")

