alfabet = ["a","b","c","d","e","f","g",
           "h","i","j","k","l","m","n",
           "o","p","r","s","t","u","w",
           "x","y","z"]
lenAlfa = len(alfabet)
msgToCode = "ala ma kota zxw"
msgCoded = ""
k = int(input("Podaj k "))
k = k%lenAlfa

for i in range(len(msgToCode)):
    for j in range(lenAlfa):
        if j+k >= lenAlfa:
            if msgToCode[i] == alfabet[j]:
                msgCoded += alfabet[j+k-lenAlfa]
                break
        else:
            if msgToCode[i] == alfabet[j]:
                msgCoded += alfabet[j+k]
                break
        if msgToCode[i] == " ":
            msgCoded += "-"
            break

print(msgToCode)
print(msgCoded)

    
