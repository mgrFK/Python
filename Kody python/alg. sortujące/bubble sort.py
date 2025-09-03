def bubble_sort(arr):

    # zewnętrzna pętla do przechodzenia po elementach tablicy
    for n in range(len(arr) - 1, 0, -1):

        # wewnętrzna pętla do porównań
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # zamiana elementów
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


# przykładowa tablica do posortowania
arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:")
print(arr)

bubble_sort(arr)

print("Sorted list is:")
print(arr)
