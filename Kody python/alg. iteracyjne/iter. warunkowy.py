import random 
 
liczba = 0
licznik = 0

while(liczba != 10):
    liczba = random.randint(0, 200)
    licznik += 1

if licznik < 100:
    print("super", licznik)
elif licznik <130:
    print("not bad", licznik)
else:
    print("try next time", licznik)
    
