from __future__ import annotations

import builtins
import pytest

from prep_test_utils import load_callable

TARGET = load_callable(
    __file__,
    exercise_filename='exercise_04.py',
    solution_filename='exercise_04_solution.py',
    callable_name='summarize_card_swipes',
)

CASES = [{'name': 'normal', 'args': [['GROCERY', 'GROCERY', 'FUEL', 'FUEL', 'FUEL', 'TRAVEL']], 'expected': 'GROCERY:2|FUEL:3|TRAVEL:1'}, {'name': 'empty', 'args': [[]], 'expected': ''}, {'name': 'single', 'args': [['DINING']], 'expected': 'DINING:1'}, {'name': 'duplicates', 'args': [['A', 'A', 'A']], 'expected': 'A:3'}, {'name': 'large_basic', 'args': [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']], 'expected': 'X:50|Y:25'}]


@pytest.mark.parametrize('case', CASES, ids=[case['name'] for case in CASES])
def test_cases(case):
    if 'raises' in case:
        with pytest.raises(getattr(builtins, case['raises'])):
            TARGET(*case['args'])
        return
    assert TARGET(*case['args']) == case['expected']
