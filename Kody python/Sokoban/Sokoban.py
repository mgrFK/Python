MAX_X = int(input("podaj szerokośc mapy (min.7)"))
MAX_Y = int(input("podaj wysokość mapy(min.7)"))
mapa =[]

def showMap():
    for row in mapa:
        print(row)

def createMap(x, y):
    for i in range(x):
        mapaX = []
        for j in range(y):
            mapaX.append(".")
        mapa.append(mapaX)

createMap(MAX_X, MAX_Y)

#ściany
mapa[5][1] = "X"
mapa[4][1] = "X"
mapa[3][2] = "X"
mapa[4][2] = "X"
mapa[1][4] = "X"
mapa[1][5] = "X"
mapa[2][5] = "X"
mapa[3][5] = "X"
mapa[3][4] = "X"

#pudełka
mapa[2][2] = "D"

#cele
mapa[5][2] = "O"

class Gracz():
    x = 6
    y = 6

def updateMap(znak):
    mapa[gracz.x][gracz.y] = znak

gracz = Gracz()
mapa[gracz.x][gracz.y] = "G"
showMap()

X = 0
Y = 0

while True:
    key = input("Podaj ruch gracza, użyj WSAD")
    
    X = gracz.x
    Y = gracz.y
    updateMap(".")
    match key:
        case "W":
            if (X - 1 >= 0 and mapa[X - 1][Y] != "X") or (mapa[X-1][Y] == "D" and mapa[X-2][Y] != "X"):
                gracz.x -= 1
                if mapa[X-1][Y] == "D" and mapa[X-2][Y] != "X":
                    if mapa[X-2][Y] == "O":
                        mapa[X-2][Y] = "D"
                        print("Wygrałeś")
                        break
                    else:
                        mapa[X-2][Y] = "D" 
        case "S": 
            if (X + 1 < MAX_X and mapa[X + 1][Y] != "X") or (mapa[X+1][Y] == "D" and mapa[X+2][Y] != "X"):
                gracz.x +=1
                if mapa[X+1][Y] == "D" and mapa[X+2][Y] != "X":
                    if mapa[X+2][Y] == "O":
                        mapa[X+2][Y] = "D"
                        print("Wygrałeś")
                        break
                    else:
                        mapa[X+2][Y] = "D" 
        case "A": 
            if (Y - 1 >= 0 and mapa[X][Y - 1] != "X") or (mapa[X][Y-1] == "D" and mapa[X][Y-2] != "X"):
                gracz.y -=1
                if mapa[X][Y-1] == "D"and mapa[X][Y-2] != "X":
                    if mapa[X][Y-2] == "O":
                        mapa[X][Y-2] = "D"
                        print("Wygrałeś")
                        break
                    else:
                        mapa[X][Y-2] = "D" 

        case "D": 
            if (Y + 1 < MAX_Y and mapa[X][Y + 1] != "X") or (mapa[X][Y+1] == "D" and mapa[X][Y+2] != "X"):
                gracz.y +=1
                if mapa[X][Y+1] == "D" and mapa[X][Y+2] != "X":
                    if mapa[X][Y+2] == "O":
                        mapa[X][Y+2] = "D"
                        print("Wygrałeś")
                        break
                    else:
                       mapa[X][Y+2] = "D" 
                
    mapa[gracz.x][gracz.y]="G"
    updateMap("G")
    showMap()
