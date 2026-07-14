from __future__ import annotations

import builtins
import pytest

from prep_test_utils import load_callable

TARGET = load_callable(
    __file__,
    exercise_filename='exercise_04.py',
    solution_filename='exercise_04_solution.py',
    callable_name='count_close_transfers',
)

CASES = [{'name': 'normal', 'args': [[10, 11, 13, 17], 2], 'expected': 2}, {'name': 'empty', 'args': [[], 2], 'expected': 0}, {'name': 'single', 'args': [[5], 2], 'expected': 0}, {'name': 'duplicates', 'args': [[4, 4, 4], 0], 'expected': 3}, {'name': 'negative_valid', 'args': [[-3, -2, 1], 1], 'expected': 1}]


@pytest.mark.parametrize('case', CASES, ids=[case['name'] for case in CASES])
def test_cases(case):
    if 'raises' in case:
        with pytest.raises(getattr(builtins, case['raises'])):
            TARGET(*case['args'])
        return
    assert TARGET(*case['args']) == case['expected']
