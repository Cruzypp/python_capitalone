from __future__ import annotations

import builtins
import pytest

from prep_test_utils import load_callable

TARGET = load_callable(
    __file__,
    exercise_filename='exercise_02.py',
    solution_filename='exercise_02_solution.py',
    callable_name='first_index_of_max',
)

CASES = [{'name': 'normal', 'args': [[3, 1, 5, 5]], 'expected': 2}, {'name': 'empty', 'args': [[]], 'expected': -1}, {'name': 'single', 'args': [[4]], 'expected': 0}, {'name': 'negative_valid', 'args': [[-3, -1, -2]], 'expected': 1}]


@pytest.mark.parametrize('case', CASES, ids=[case['name'] for case in CASES])
def test_cases(case):
    if 'raises' in case:
        with pytest.raises(getattr(builtins, case['raises'])):
            TARGET(*case['args'])
        return
    assert TARGET(*case['args']) == case['expected']
