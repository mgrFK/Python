def insertionSort(arr):
    n = len(arr)  # n = długość tablicy
      
    if n <= 1:
        return  # tablica o tej długości jest już posortowana
 
    for i in range(1, n):  # rozpocznij iteracje od drugiego elementu
        key = arr[i]  # przechowuj obecny element jako key, który ma być włożony w odpowiednim miejscu
        j = i-1
        while j >= 0 and key < arr[j]:  # przesuń dalej element większy od key
            arr[j+1] = arr[j]  # zamień element z prawym
            j -= 1
        arr[j+1] = key  # włóż key we właściwe miejsce
  
# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)
