toSort = [5,13,5,24,6,13]
afterSort = [5,5,13,24]

def sortTab(toSort):
    afterSort = toSort
    for i in range(len(toSort)): # tablica do posortowania
        for j in range(len(afterSort)):
            if afterSort[j] > toSort[i]:   # porównaj wynik z wartością do włożenia
                temp = afterSort[j]
                afterSort[j] = toSort[i]
                afterSort[i] = temp
    print(afterSort)

sortTab(toSort)
