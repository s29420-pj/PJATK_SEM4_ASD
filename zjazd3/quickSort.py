import time

# 1. Zaimplementuj QuickSort w wersja Lomuto z prezentacji, z wykładu
# 2. Napisz drugą wersję funkcji podziału A[(p+r)//2] <-> A[r]
# 3. Zmierz czas działania dla obu funkcji

arrOne = [2, 5, 1, 23, 3, 89, 56, 76, 12, 5, 5, 6, 2, 42, 56, 100, 4234, 245, 235, 12, 455]
arrTwo = [2, 5, 1, 23, 3, 89, 56, 76, 12, 5, 5, 6, 2, 42, 56, 100, 4234, 245, 235, 12, 455]

def partitionOne(arr, p, r):
    pivot = arr[r]
    smaller = p

    for j in range(p, r):
        if arr[j] <= pivot:
            arr[smaller], arr[j] = arr[j], arr[smaller]
            smaller += 1

    arr[smaller], arr[r] = arr[r], arr[smaller]
    return smaller

def quickSortOne(arr, p, r):
    if p < r:
        q = partitionOne(arr, p, r)
        quickSortOne(arr, p, q - 1)
        quickSortOne(arr, q + 1, r)

    return arr

def partitionTwo(arr, p, r):
    arr[(p + r) // 2], arr[r] = arr[r], arr[(p + r) // 2]
    pivot = arr[r]
    smaller = p

    for j in range(p, r):
        if arr[j] <= pivot:
            arr[smaller], arr[j] = arr[j], arr[smaller]
            smaller += 1

    arr[smaller], arr[r] = arr[r], arr[smaller]
    return smaller

def quickSortTwo(arr, p, r):
    if p < r:
        q = partitionTwo(arr, p, r)
        quickSortTwo(arr, p, q - 1)
        quickSortTwo(arr, q + 1, r)

    return arr

start_time_quickSortOne = time.time()
print(quickSortOne(arrOne, 0, len(arrOne) - 1))
end_time_quickSortOne = time.time()
print("Elapsed Time for quickSortOne: ")
print(end_time_quickSortOne - start_time_quickSortOne)
print()

start_time_quickSortTwo = time.time()
print(quickSortTwo(arrTwo, 0, len(arrTwo) - 1))
end_time_quickSortTwo = time.time()
print("Elapsed Time for quickSortTwo: ")
print(end_time_quickSortTwo - start_time_quickSortTwo)