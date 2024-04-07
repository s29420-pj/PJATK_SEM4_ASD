arr = [2, 5, 1, 23, 3, 89, 56, 76, 12, 5, 5, 6, 2, 42, 56, 100, 4234, 245, 235, 12, 455]

def maxHeapify(arr, heapSize, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heapSize and arr[left] > arr[largest]:
        largest = left

    if right < heapSize and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, heapSize, largest)


def buildMaxHeap(arr):
    heapSize = len(arr)

    for i in range((heapSize - 2) // 2, -1, -1):
        maxHeapify(arr, heapSize, i)

    return arr


def heapSort(arr):
    buildMaxHeap(arr)
    heapSize = len(arr)

    for i in range((heapSize - 1), 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapSize -= 1
        maxHeapify(arr, heapSize, 0)

    print(arr)


heapSort(arr)