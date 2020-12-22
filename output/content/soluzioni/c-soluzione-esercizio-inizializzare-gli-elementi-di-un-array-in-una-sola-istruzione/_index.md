---
title: "[c] soluzione esercizio: Inizializzare gli elementi di un array in una sola istruzione"
date: "2020-12-22T07:36:04.662145+00:00"
summary: ""
type: "soluzione"

url: "/soluzioni/c-inizializzare-gli-elementi-di-un-array-in-una-sola-istruzione"



tags: 

- "c"

- "esercizio"

- "vettori"












---


soluzione di [Inizializzare gli elementi di un array in una sola istruzione](/esercizi/trovare-il-massimo-di-un-vettore):


Inizializzare un array usando il minor numero di righe di codice

### soluzione



## 

### codice sorgente completo
<details>
<summary>Clicca per vedere il codice!</summary>

```C
#include <stdio.h>

int main()
{
	int values[5] = {1,2,3,5,4};

	int max_value = values[0];

	for (int i =0; i < 5;i++){
		if(values[i] > max_value) {
			max_value = values[i];
		}
	}

	printf("max value = %d\n",max_value);

	return 0;
}
```

</details>



### soluzioni in altri linguaggi



*	[[c++] soluzione esercizio: Inizializzare gli elementi di un array in una sola istruzione](/soluzioni/c++-inizializzare-gli-elementi-di-un-array-in-una-sola-istruzione)







### altri [esercizi sui vettori](/category/esercizi-sui-vettori)

* [Massimo valore in un vettore](/esercizi/trovare-il-massimo-di-un-vettore)


### altri [esercizi sugli array](/category/esercizi-sugli-array)




