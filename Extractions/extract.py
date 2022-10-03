# sistema per estrazioni e creazione di un calendario: import random
import random

numero_alunni = 20          #CHANGE THIS VALUE TO BASED ON YOUR CLASS, IF YOU ARE IN 22 PUT 22, IF 15 PUT 15 ECC...

nomi_alunni = {
    1 : "Name",                     #CHANGE THE NAMES TO YOUR CLASSMATES' ONES
    2 : "Name",
    3 : "Name",
    4 : "Name",
    5 : "Name",
    6 : "Name",
    7 : "Name",
    8 : "Name",
    9 : "Name",
    10 : "Name",
    11 : "Name",
    12 : "Name",
    13 : "Name",
    14 : "Name",
    15 : "Name",
    16 : "Name",
    17 : "Name",
    18 : "Name",
    19 : "Name",
    20 :"Name"
}

giorni = [
       "gg/mm"  ,   "gg/mm" ,   "gg/mm" ,   "gg/mm"  ,   "gg/mm"    #YOU CAN PUT AS MANY DAYS  AS YOU WANT
]

###################### DO NOT EDIT ######################
estratti = []

max=(numero_alunni // len(giorni)) 

if numero_alunni % len(giorni) !=0:
    max+=1

for i in range(len(giorni)):
    print(f"\n\nsettimana del {giorni[i]}, gli estratti sono:\n")
    for j in range(max):
        if len(estratti)==numero_alunni:
            break
        n=random.randint(1,numero_alunni)
        while n  in estratti:
            n=random.randint(1,numero_alunni)
        estratti.append(n)
        print(f"|numero {n}, {nomi_alunni[n]}" , end="|\t")
    print("\n----------")
#######################################################