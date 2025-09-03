txt = "ala ma kota, a kot ma ale"
toSearch = "kot"

words = txt.split(" ")
print(words)
counter = 0
for i in range(len(txt)-len(toSearch)):
    if(toSearch[0]==txt[i]):
        counter+=1
        for j in range(1,len(toSearch)):
            if(toSearch[j]==txt[i+j]):
                counter+=1
    else:
        counter = 0
        
    if(counter==len(toSearch)):
        print("Słowo znaleziono na miejscu",i, i+1, i+2)
            
        
        

'''
for word in words:
    if(word == toSearch):
        print("Słowo znaleziono")
        break
    else:
        print("Słowa nie ma w txt")
        '''