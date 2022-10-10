def contaParola():
    a=""
    while True:
        a+=input()+" "
        if "b" in a:
            break
        
    print(f"il numero di parole conteggiate è {52+len(a)}")

contaParola()