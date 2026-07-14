# Python Cheatsheet

## Listas
- `append`, `pop`, `sort`, slicing `values[a:b:c]`
- `enumerate(values)` si necesitas indice y valor

## Strings
- `split`, `join`, slicing, `startswith`, `endswith`
- Son inmutables

## Diccionarios
- `mapping[key]`, `mapping.get(key, default)`, `items()`
- Lookup promedio O(1)

## Sets
- `add`, `discard`, membership con `in`

## Counter
- `from collections import Counter`
- `Counter(values)`

## defaultdict
- `from collections import defaultdict`
- Inicializacion automatica de listas o contadores

## deque
- `from collections import deque`
- `append`, `appendleft`, `popleft`

## heapq
- `heappush`, `heappop`, `heapify`

## Sorting
- `sorted(values, key=lambda item: item[1])`

## Comprensiones
- `[x * 2 for x in values if x > 0]`
- `{k: len(v) for k, v in groups.items()}`

## Type hints
- `list[int]`, `dict[str, int]`, `tuple[int, int] | None`

## Dataclasses
- `from dataclasses import dataclass`

## Excepciones
- `raise ValueError("message")`
