from __future__ import annotations

import builtins
import pytest

from prep_test_utils import load_callable

TARGET = load_callable(
    __file__,
    exercise_filename='exercise_01.py',
    solution_filename='exercise_01_solution.py',
    callable_name='count_balance_changes',
)

CASES = [{'name': 'normal', 'args': [[5, -8, 4, -3, 10]], 'expected': 4}, {'name': 'empty', 'args': [[]], 'expected': 0}, {'name': 'single', 'args': [[7]], 'expected': 0}, {'name': 'duplicates', 'args': [[2, 2, -5, -1, 6]], 'expected': 2}, {'name': 'negative_valid', 'args': [[-3, 1, 1, 1]], 'expected': 0}, {'name': 'large_basic', 'args': [[1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2, 1, -2]], 'expected': 1}]


@pytest.mark.parametrize('case', CASES, ids=[case['name'] for case in CASES])
def test_cases(case):
    if 'raises' in case:
        with pytest.raises(getattr(builtins, case['raises'])):
            TARGET(*case['args'])
        return
    assert TARGET(*case['args']) == case['expected']
