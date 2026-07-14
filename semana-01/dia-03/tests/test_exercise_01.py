from __future__ import annotations

import builtins
import pytest

from prep_test_utils import load_callable

TARGET = load_callable(
    __file__,
    exercise_filename='exercise_01.py',
    solution_filename='exercise_01_solution.py',
    callable_name='pair_with_target_spend',
)

CASES = [{'name': 'normal', 'args': [[1, 2, 4, 7, 11], 9], 'expected': True}, {'name': 'empty', 'args': [[], 5], 'expected': False}, {'name': 'single', 'args': [[5], 5], 'expected': False}, {'name': 'duplicates', 'args': [[3, 3, 4], 6], 'expected': True}, {'name': 'negative_valid', 'args': [[-5, -1, 4, 8], 3], 'expected': True}]


@pytest.mark.parametrize('case', CASES, ids=[case['name'] for case in CASES])
def test_cases(case):
    if 'raises' in case:
        with pytest.raises(getattr(builtins, case['raises'])):
            TARGET(*case['args'])
        return
    assert TARGET(*case['args']) == case['expected']
