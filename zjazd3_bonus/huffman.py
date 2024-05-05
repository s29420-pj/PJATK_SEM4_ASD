class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def minHeapify(arr, heapSize, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heapSize and arr[left] < arr[smallest]:
        smallest = left

    if right < heapSize and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minHeapify(arr, heapSize, smallest)


def buildMinHeap(arr):
    heapSize = len(arr)

    for i in range((heapSize - 2) // 2, -1, -1):
        minHeapify(arr, heapSize, i)

    return arr


def extractMin(heap):
    minElement = heap.pop(0)
    if heap:
        last_elem = heap.pop()
        heap.insert(0, last_elem)
        minHeapify(heap, len(heap), 0)
    return minElement


def insertMinHeap(heap, element):
    heap.append(element)
    i = len(heap) - 1
    while i != 0 and heap[(i - 1) // 2].freq > heap[i].freq:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2


def huffman(C):
    heap = C[:]
    buildMinHeap(heap)
    n = len(heap)

    for i in range(n - 1):
        z = Node()

        z.left = extractMin(heap)
        z.right = extractMin(heap)

        z.freq = z.left.freq + z.right.freq

        insertMinHeap(heap, z)

    return extractMin(heap)


# Zadanie 1
chars = ['x', 'y', 'z', 'a', 'b']
freqs = [5, 2, 90, 14, 60]
nodes = [Node(chars[i], freqs[i]) for i in range(len(chars))]

huffman_tree = huffman(nodes)

def printCodes(node, prefix=""):
    if node is not None:
        if node.char is not None:
            print(f"{node.char}: {prefix}")
        printCodes(node.left, prefix + "0")
        printCodes(node.right, prefix + "1")


printCodes(huffman_tree)

#zrobic pobranie pliku txt z lorem ipsum, zliczenie znaków i zapis do drugiego pliku