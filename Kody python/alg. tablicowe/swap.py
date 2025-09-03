def swap(i1, i2, tab):
    a = tab[i1]
    tab[i1] = tab[i2]
    tab[i2] = a

    return tab

def search(value1,tab):
    for i in range(len(tab)):
        if value1 == tab[i]:
            return i

tab = swap(2, 3, [1,2,3,4,5,6])
print(tab)
print(search(6, [1,2,3,4,5,6]))

print(swap(search(2, tab), search(6,tab), tab))
