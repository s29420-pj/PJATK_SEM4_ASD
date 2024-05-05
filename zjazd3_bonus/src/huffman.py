import ast

DEFAULT_ENCODE_INPUT_PATH = "input/exampleFileToEncode.txt"
DEFAULT_DECODE_INPUT_PATH = "input/exampleFileToDecode.txt"
DEFAULT_ENCODE_OUTPUT_PATH = "output/encodedFile.txt"
DEFAULT_DECODE_OUTPUT_PATH = "output/decodedFile.txt"
DEFAULT_HUFFMAN_CODES_PATH = "codes/huffmanCodes_exampleFileToEncode.txt"

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


def createCharFreqFromFile(filePath):
    with open(filePath, 'r') as file:
        text = file.read()

    charFreq = {}
    for char in text:
        if char in charFreq:
            charFreq[char] += 1
        else:
            charFreq[char] = 1

    chars = list(charFreq.keys())
    freqs = list(charFreq.values())

    return chars, freqs


def encodeToFile(inputFilePath, outputFilePath, huffmanCodes):
    with open(inputFilePath, 'r') as inputFile:
        text = inputFile.read()

    encodedText = ''
    for char in text:
        encodedText += huffmanCodes[char]

    with open(outputFilePath, 'w') as outputFile:
        outputFile.write(encodedText)


def printCodes(node, prefix=""):
    if node is not None:
        if node.char is not None:
            print(f"{node.char}: {prefix}")
        printCodes(node.left, prefix + "0")
        printCodes(node.right, prefix + "1")


def getHuffmanCodes(node, prefix=""):
    if node is None:
        return {}

    if node.char is not None:
        return {node.char: prefix}

    codes = {}
    codes.update(getHuffmanCodes(node.left, prefix + "0"))
    codes.update(getHuffmanCodes(node.right, prefix + "1"))
    return codes


def decodeFromFile(inputFilePath, outputFilePath, huffmanCodesFilePath):
    with open(inputFilePath, 'r') as inputFile:
        encodedText = inputFile.read()

    with open(huffmanCodesFilePath, 'r') as huffmanCodesFile:
        huffmanCodesStr = huffmanCodesFile.read()
        huffmanCodes = ast.literal_eval(huffmanCodesStr)

    reversedHuffmanCodes = {v: k for k, v in huffmanCodes.items()}

    decodedText = ''
    tempCode = ''
    for bit in encodedText:
        tempCode += bit
        if tempCode in reversedHuffmanCodes:
            decodedText += reversedHuffmanCodes[tempCode]
            tempCode = ''

    with open(outputFilePath, 'w') as outputFile:
        outputFile.write(decodedText)


def main():
    while True:
        print("1. Encode File")
        print("2. Decode File")
        print("3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            inputFilePath = input(f"Enter the path to the file you want to encode (default: {DEFAULT_ENCODE_INPUT_PATH}): ") or DEFAULT_ENCODE_INPUT_PATH
            outputFilePath = input(f"Enter the path where you want to save the encoded file (default: {DEFAULT_ENCODE_OUTPUT_PATH}): ") or DEFAULT_ENCODE_OUTPUT_PATH
            huffmanCodesFilePath = input(f"Enter the path where you want to save the Huffman codes dictionary (default: {DEFAULT_HUFFMAN_CODES_PATH}): ") or DEFAULT_HUFFMAN_CODES_PATH

            chars, freqs = createCharFreqFromFile(inputFilePath)
            nodes = [Node(chars[i], freqs[i]) for i in range(len(chars))]
            huffmanTree = huffman(nodes)
            huffmanCodes = getHuffmanCodes(huffmanTree)
            encodeToFile(inputFilePath, outputFilePath, huffmanCodes)

            with open(huffmanCodesFilePath, 'w') as huffmanCodesFile:
                huffmanCodesFile.write(str(huffmanCodes))

        elif choice == "2":
            inputFilePath = input(f"Enter the path to the file you want to decode (default: {DEFAULT_DECODE_INPUT_PATH}): ") or DEFAULT_DECODE_INPUT_PATH
            outputFilePath = input(f":Enter the path where you want to save the decoded file (default: {DEFAULT_DECODE_OUTPUT_PATH}): ") or DEFAULT_DECODE_OUTPUT_PATH
            huffmanCodesFilePath = input(f"Enter the path to the file with the Huffman codes dictionary (default: {DEFAULT_HUFFMAN_CODES_PATH}): ") or DEFAULT_HUFFMAN_CODES_PATH

            decodeFromFile(inputFilePath, outputFilePath, huffmanCodesFilePath)

        elif choice == "3":
            break

        else:
            print("Unknown option. Please try again.")

if __name__ == "__main__":
    main()