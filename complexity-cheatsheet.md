# Complexity Cheatsheet

## Complejidades comunes
- O(1): acceso por indice en lista, lookup promedio en dict/set
- O(log n): binary search, push/pop en heap
- O(n): recorrido lineal
- O(n log n): sorting
- O(n^2): comparaciones por pares

## List
- Acceso por indice: O(1)
- Buscar elemento: O(n)
- Insertar al final: amortizado O(1)

## Dict y Set
- Lookup e insercion promedio: O(1)

## Sorting
- `sorted` y `list.sort`: O(n log n)

## Heap
- Push/pop: O(log n)
- Obtener minimo: O(1)

## Matrices
- Recorrer filas y columnas: O(rows * cols)

## BFS
- O(V + E)

## Binary search
- O(log n) si el espacio de busqueda es monotono

## Como justificar Big O
- Hago un solo recorrido sobre la lista, asi que el tiempo es O(n).
- Uso un diccionario para frecuencias, por eso agrego O(n) espacio extra.
- Ordeno primero y luego hago un barrido; el costo dominante es O(n log n).
