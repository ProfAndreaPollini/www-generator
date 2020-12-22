---
title: "[c++] soluzione esercizio: Massimo valore in un vettore"
date: "2020-12-22T07:19:17.986489+00:00"
summary: ""
type: "soluzione"

url: "/soluzioni/c++-massimo-valore-in-un-vettore"



tags: 

- "c++"

- "esercizio"

- "vettori"












---


soluzione di [Massimo valore in un vettore](/esercizi/trovare-il-massimo-di-un-vettore):


Trovare il valore massimo in un vettore di elementi.

### soluzione



## 

### codice sorgente completo
<details>
<summary>Clicca per vedere il codice!</summary>

```C++
#include <iostream>


int main()
{
	int values[5] = {1,2,3,5,4};

	int max_value = values[0];

	for (int i =0; i < 5;i++){
		if(values[i] > max_value) {
			max_value = values[i];
		}
	}

	std::cout << "max value = "<< max_value << std::endl;

	return 0;
}
```

</details>



### soluzioni in altri linguaggi



*	[[c] soluzione esercizio: Massimo valore in un vettore](/soluzioni/c-massimo-valore-in-un-vettore)



*	[[python] soluzione esercizio: Massimo valore in un vettore](/soluzioni/python-massimo-valore-in-un-vettore)







### altri [esercizi sui vettori](/category/esercizi-sui-vettori)

* [Massimo valore in un vettore](/esercizi/trovare-il-massimo-di-un-vettore)




