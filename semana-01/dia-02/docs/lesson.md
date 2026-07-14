# Diccionarios, sets y frecuencias

## 1. Objetivo de la leccion
Practicar membership tests y conteos para reemplazar busquedas repetidas.

## 2. Conceptos fundamentales
- Diccionarios
- Sets
- Frecuencias
- Busqueda rapida
- Deteccion de duplicados

## 3. Sintaxis importante de Python
- Usa type hints de Python 3.12 para documentar entradas y salidas.
- Prefiere estructuras del lenguaje antes de crear helpers innecesarios.
- Si necesitas validacion, hazla al inicio y falla de forma explicita.
- Usa slicing, `enumerate`, `dict.get`, comprensiones y desempaquetado cuando mejoren la lectura.

## 4. Estructuras de datos relevantes
- Elige la estructura por la operacion dominante.
- Si consultas membership muchas veces, piensa primero en `set` o `dict`.
- Si el orden importa, dilo en voz alta durante la entrevista.

## 5. Patrones comunes
- Empieza con un ejemplo manual y detecta el estado minimo que debes mantener.
- Compara una solucion brute force contra una optimizada para justificar el cambio.
- Revisa si ordenar o preprocesar simplifica el recorrido principal.

## 6. Errores frecuentes
- Olvidar entradas vacias o de un solo elemento.
- Actualizar el estado en el orden incorrecto.
- Mezclar claridad con optimizacion prematura.

## 7. Casos limite
- Entrada vacia.
- Un solo elemento.
- Valores repetidos o todos iguales.
- Valores negativos cuando sean validos.

## 8. Complejidad temporal y espacial
Explica el costo dominante en terminos del numero de elementos, la estructura auxiliar usada y cualquier ordenamiento o busqueda adicional.

## 9. Como identificar cuando utilizar el patron
- Si el problema repite la misma consulta, busca una estructura que la abarate.
- Si puedes mover punteros solo hacia adelante, probablemente hay un patron lineal util.
- Si el requerimiento es mejor que O(n^2), piensa en memoria extra o en ordenar primero.

## 10. Como explicarlo durante una entrevista
- Restate the problem in one sentence.
- Nombra la estructura de datos y por que evita trabajo repetido.
- Cierra con Big O y un caso limite importante.

## Technical vocabulary in English
- Time complexity
- Space complexity
- Average constant-time lookup
- Edge case
- Brute-force approach
- Optimized approach

I am using a dictionary because it provides average O(1) lookup.
The time complexity is O(n), and the space complexity is O(n).
Before coding, I would like to clarify how duplicated values should be handled.
