paths = [
    #A B C D E
    [0,2,0,0,1],#A
    [2,0,1,3,2],#B
    [0,1,0,2,1],#C
    [0,3,2,0,3],#D
    [1,2,1,3,0] #E
    ]

def check_visited(visited):
    licznik = 0
    for i in range(len(visited)):
        if visited[i]==1:
            licznik += 1
    if licznik == len(visited):
        return True
    else:
        return False

def nn(paths):
    visited = [1,0,0,0,0]
    actual = 0
    suma = 0
    indeks = 0

    while check_visited(visited) != True:
        val_min = 10
        #znajdź najkrótszą ścieżkę z aktualnego do nieodwiedzonego
        for i in range(len(paths[actual])):
            if val_min > paths[actual][i] and paths[actual][i] > 0 and visited[i]==0:
                val_min = paths[actual][i]
                indeks = i
            
        #dodaj ścieżkę do rozwiązania
        suma += val_min
        actual = indeks
        visited[indeks] = 1
    print(suma, visited)
    
nn(paths)
