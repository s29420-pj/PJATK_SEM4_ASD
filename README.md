## Zjazd 1:

W pliku znajdują się definicje pięciu funkcji: f1, f2, ... , f5 oraz pomiar sprawdzający, czy rzeczywisty czas działania funkcji f1(n) (wyliczony w zmiennej Tn) dla różnych wartości n (równych 2000, 4000, 8000, 16000, 32000) zmienia się zgodnie z przebiegiem funkcji liniowej (Fn = n). Otrzymane wyniki interpretujemy następująco: funkcja Fn dobrze opisuje prawdziwy czas Tn funkcji f1, jeżeli ilorazy Fn/Tn są mniej więcej takie same dla wszystkich wartości n.
Wykonać podobne pomiary dla pozostałych funkcji, dobierając odpowiednie funkcje Fn. Aby dobrać odpowiednią funkcję Fn trzeba przeanalizować kod; np. jeżeli mamy 4 zagnieżdżone pętle, każda długości n, to można się spodziewać, że czas ich działania będzie się zmieniał jak funkcja n4.
Jako rozwiązanie przesłać kod programu wykonującego pomiary z dołączonymi wynikami wygenerowanymi przez ten program dla wszyskich pięciu funkcji. Wyniki te można dołączyć np. jako komentarz na końcu kodu programu.

## Zjazd 2:

Zaimplementuj algorytm sortowania przez kopcowanie z prezentacji (0.5 pkt)

## Zjazd 3:

1. Zaimplementuj QuickSort w wersja Lomuto z prezentacji, z wykładu
2. Napisz drugą wersję funkcji podziału A[(p+r)//2] <-> A[r]
3. Zmierz czas działania dla obu funkcji
