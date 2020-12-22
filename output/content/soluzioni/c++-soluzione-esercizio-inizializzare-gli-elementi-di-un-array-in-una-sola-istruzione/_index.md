---
title: "[c++] soluzione esercizio: Inizializzare gli elementi di un array in una sola istruzione"
date: "2020-12-22T07:36:04.662145+00:00"
summary: ""
type: "soluzione"

url: "/soluzioni/c++-inizializzare-gli-elementi-di-un-array-in-una-sola-istruzione"



tags: 

- "c++"

- "esercizio"

- "vettori"

- "std::iostream"

- "fondamenti del linguaggio"

- "Esercizi sugli array"












---


soluzione di [Inizializzare gli elementi di un array in una sola istruzione](/esercizi/trovare-il-massimo-di-un-vettore):


Inizializzare un array usando il minor numero di righe di codice

### soluzione



## 

L'inizializzazione in C++, dalla versione C++11, consente di inizializzare tutti gli elementi di un array semplicemente utilizzando l'[inizializzatore uniforme](https://en.cppreference.com/w/cpp/language/initialization). Senza questa inizializzazione **non siamo garantiti del fatto che gli elementi dell'array verranno inizializzati a 0**.


### codice sorgente completo
<details>
<summary>Clicca per vedere il codice!</summary>

```cpp
#include <iostream>
using namespace std;
int main() {
  int pippo[3] = {0};
}
```

</details>



### soluzioni in altri linguaggi





*	[[c] soluzione esercizio: Inizializzare gli elementi di un array in una sola istruzione](/soluzioni/c-inizializzare-gli-elementi-di-un-array-in-una-sola-istruzione)





### altri [esercizi sui vettori](/category/esercizi-sui-vettori)

* [Massimo valore in un vettore](/esercizi/trovare-il-massimo-di-un-vettore)


### altri [esercizi sugli array](/category/esercizi-sugli-array)




