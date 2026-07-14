from __future__ import annotations

import builtins
import pytest

from prep_test_utils import load_callable

TARGET = load_callable(
    __file__,
    exercise_filename='exercise_04.py',
    solution_filename='exercise_04_solution.py',
    callable_name='ids_above_threshold',
)

CASES = [{'name': 'normal', 'args': [[('a', 10), ('b', 5), ('c', 20)], 9], 'expected': ['a', 'c']}, {'name': 'empty', 'args': [[], 3], 'expected': []}, {'name': 'single', 'args': [[('x', 1)], 1], 'expected': []}, {'name': 'negative_valid', 'args': [[('a', -1), ('b', 2)], 0], 'expected': ['b']}]


@pytest.mark.parametrize('case', CASES, ids=[case['name'] for case in CASES])
def test_cases(case):
    if 'raises' in case:
        with pytest.raises(getattr(builtins, case['raises'])):
            TARGET(*case['args'])
        return
    assert TARGET(*case['args']) == case['expected']
