---
title: "[python] soluzione esercizio: Massimo valore in un vettore"
date: "2020-12-22T07:19:17.986489+00:00"
summary: ""
type: "soluzione"

url: "/soluzioni/python-massimo-valore-in-un-vettore"



tags: 

- "python"

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

```python


valori = [1,2,3,5,3]

massimo = valori[0]

for i in range(1,len(valori)):
	if valori[i] > massimo:
		massimo = valori[i]

print(f"il massimo vale {massimo}")
```

</details>



### soluzioni in altri linguaggi



*	[[c] soluzione esercizio: Massimo valore in un vettore](/soluzioni/c-massimo-valore-in-un-vettore)





*	[[c++] soluzione esercizio: Massimo valore in un vettore](/soluzioni/c++-massimo-valore-in-un-vettore)





### altri [esercizi sui vettori](/category/esercizi-sui-vettori)

* [Massimo valore in un vettore](/esercizi/trovare-il-massimo-di-un-vettore)




