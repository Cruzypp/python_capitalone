# Capital One Python Interview Prep

Programa intensivo de cuatro semanas para prepararte para una entrevista de Software Engineer de entrada en Capital One Mexico, con enfoque en Python 3.12, algoritmos, estructuras de datos, debugging, technical cases, comunicacion tecnica en ingles y behavioral interviews para un programa tipo Technology Development Program de 18 meses.

## Objetivo del programa
- Practicar evaluaciones de programacion tipo CodeSignal.
- Reforzar problemas Easy y Medium con contexto bancario y financiero.
- Mejorar lectura de codigo, cambios seguros y debugging.
- Preparar entrevistas tecnicas, technical cases y behavioral interviews.

## Recomendacion de ritmo
- Trabaja dos horas por dia.
- Dias 1 al 5: leccion y ejercicios.
- Dia 6: simulacion semanal.
- Dia 7: descanso o revision libre.

## Crear un entorno virtual
macOS o Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Windows CMD:

```bat
python -m venv .venv
.venv\Scriptsctivate.bat
pip install -r requirements.txt
```

## Ejecutar tests
Todos los tests contra ejercicios:

```bash
pytest
```

Todos los tests contra soluciones:

```bash
INTERVIEW_PREP_TARGET=solution pytest
```

Tests de un dia especifico:

```bash
pytest semana-01/dia-01/tests
INTERVIEW_PREP_TARGET=solution pytest semana-01/dia-01/tests
```

Windows PowerShell:

```powershell
$env:INTERVIEW_PREP_TARGET = "solution"
pytest semana-01/dia-01/tests
Remove-Item Env:INTERVIEW_PREP_TARGET
```

## Como trabajar una leccion
1. Lee el `README.md` del dia.
2. Estudia `docs/lesson.md`, `docs/examples.md` y `docs/complexity.md`.
3. Resuelve los cuatro ejercicios en `exercises/` sin abrir `solutions/`.
4. Ejecuta `pytest semana-XX/dia-XX/tests`.
5. Solo al final compara con `solutions/`.
6. Registra tu progreso en `progress.md`.

## Como evitar ver soluciones antes de tiempo
- Trabaja siempre desde `exercises/` o `assessment/`.
- Usa los tests como senal de avance, no las soluciones.
- Abre `solutions/` solo despues de escribir y probar tu intento.

## Reglas para simulaciones
- Usa un temporizador real.
- No abras internet ni soluciones durante la simulacion.
- Haz aclaraciones antes de programar.
- Reserva de 5 a 10 minutos para pruebas manuales y complejidad.
- Llena `self-evaluation.md` y `results.md` al terminar.

## Calendario de cuatro semanas
| Semana | Dia | Tema |
|---|---|---|
| 1 | 1 | Listas, strings, recorridos e indices |
| 1 | 2 | Diccionarios, sets y frecuencias |
| 1 | 3 | Two pointers y sliding window |
| 1 | 4 | Sorting, key functions e intervalos |
| 1 | 5 | Matrices y simulacion |
| 1 | 6 | CodeSignal style weekly simulation |
| 2 | 1 | Stack, queue y deque |
| 2 | 2 | Heap y top K |
| 2 | 3 | Binary search y busqueda sobre respuestas |
| 2 | 4 | Programacion orientada a objetos |
| 2 | 5 | Sistema pequeno de cuentas y transacciones |
| 2 | 6 | Mock technical interview |
| 3 | 1 | Lectura de codigo y flujo |
| 3 | 2 | Debugging clasico |
| 3 | 3 | Modificacion segura de codigo |
| 3 | 4 | Technical case: transacciones duplicadas |
| 3 | 5 | Technical case: alertas de fraude |
| 3 | 6 | Mock technical case |
| 4 | 1 | Repaso arrays, strings, dicts y sets |
| 4 | 2 | Repaso patterns principales |
| 4 | 3 | Repaso OOP, debugging y cambios |
| 4 | 4 | Behavioral interview y STAR |
| 4 | 5 | Comunicacion tecnica en ingles |
| 4 | 6 | Power Day completo |
