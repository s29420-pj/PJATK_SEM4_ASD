X = list("abrakadabra")
Y = list("karamba")

def lcsLength(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for i in range(n + 1)] for j in range(m + 1)]
    b = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = '\\'
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = '|'
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = '-'

    return c, b

def minCharsToCompleteAlphabet(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    c, b = lcsLength(word, alphabet)
    length = c[len(word)][len(alphabet)]

    return len(alphabet) - length

print(lcsLength(X, Y))
print(minCharsToCompleteAlphabet(Y))