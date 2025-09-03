tekst = "ala ma kota"
szukana = "ma"
ile_slow = 0

for i in range(len(tekst) - len(szukana)+1):
    spr_id = 0
    for j in range(len(szukana)):
        if szukana[j] == tekst[i+j]:
            spr_id += 1
        else:
            break
    if spr_id == len(szukana):
        print("znaleziono na indeksie",i)
        ile_slow += 1    

if(ile_slow == 0):
    print("W podanym tekscie nie ma wyrazu", szukana)
else:
    print("znaleziono łącznie",ile_slow, "słowa")
        
