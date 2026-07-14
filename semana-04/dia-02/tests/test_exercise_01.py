from __future__ import annotations

import builtins
import pytest

from prep_test_utils import load_callable

TARGET = load_callable(
    __file__,
    exercise_filename='exercise_01.py',
    solution_filename='exercise_01_solution.py',
    callable_name='count_unique_values',
)

CASES = [{'name': 'normal', 'args': [[1, 2, 2, 3]], 'expected': 3}, {'name': 'empty', 'args': [[]], 'expected': 0}, {'name': 'single', 'args': [[7]], 'expected': 1}, {'name': 'negative_valid', 'args': [[-1, -1, 2]], 'expected': 2}]


@pytest.mark.parametrize('case', CASES, ids=[case['name'] for case in CASES])
def test_cases(case):
    if 'raises' in case:
        with pytest.raises(getattr(builtins, case['raises'])):
            TARGET(*case['args'])
        return
    assert TARGET(*case['args']) == case['expected']
