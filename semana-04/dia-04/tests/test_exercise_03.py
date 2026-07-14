from __future__ import annotations

import builtins
import pytest

from prep_test_utils import load_callable

TARGET = load_callable(
    __file__,
    exercise_filename='exercise_03.py',
    solution_filename='exercise_03_solution.py',
    callable_name='sum_values_seen_once',
)

CASES = [{'name': 'normal', 'args': [[1, 2, 2, 3]], 'expected': 4}, {'name': 'empty', 'args': [[]], 'expected': 0}, {'name': 'single', 'args': [[9]], 'expected': 9}, {'name': 'negative_valid', 'args': [[-1, 2, -1, 3]], 'expected': 5}]


@pytest.mark.parametrize('case', CASES, ids=[case['name'] for case in CASES])
def test_cases(case):
    if 'raises' in case:
        with pytest.raises(getattr(builtins, case['raises'])):
            TARGET(*case['args'])
        return
    assert TARGET(*case['args']) == case['expected']
