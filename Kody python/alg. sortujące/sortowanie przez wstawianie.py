tab = [4,2,4,1,2,3,6]

     #[1,4,2,4,6,2,3]
def sortuj():
    sortedTab = []
    for i in range(len(tab)):
        minV = min(tab[i:])
        for j in range(i,len(tab)):
            if tab[j] == minV:
                temp = tab[i]
                tab[i] = tab[j]
                tab[j] = temp  
                #sortedTab.append(minV)
                break

    print(tab)


def wstawianie():
    tabS = tab
    for j in range(len(tab)):
        for i in range(len(tabS)):
            if tab[j] < tabS[i]:
                temp = tab[i]
                tab[i] = tab[j]
                tab[j] = temp

    print(tab)

print(tab)
wstawianie()


Posortuj w jeden sposób jedną tablicę,
potem drugą drugim sposobem
a na koniec połaczcie i posortujcie dowolnym














 







