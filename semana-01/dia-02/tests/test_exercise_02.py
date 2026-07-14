from __future__ import annotations

import builtins
import pytest

from prep_test_utils import load_callable

TARGET = load_callable(
    __file__,
    exercise_filename='exercise_02.py',
    solution_filename='exercise_02_solution.py',
    callable_name='build_reward_frequency',
)

CASES = [{'name': 'normal', 'args': [['cashback', 'miles', 'cashback']], 'expected': {'cashback': 2, 'miles': 1}}, {'name': 'empty', 'args': [[]], 'expected': {}}, {'name': 'single', 'args': [['travel']], 'expected': {'travel': 1}}, {'name': 'duplicates', 'args': [['a', 'a', 'a']], 'expected': {'a': 3}}, {'name': 'large_basic', 'args': [['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q']], 'expected': {'p': 100, 'q': 50}}]


@pytest.mark.parametrize('case', CASES, ids=[case['name'] for case in CASES])
def test_cases(case):
    if 'raises' in case:
        with pytest.raises(getattr(builtins, case['raises'])):
            TARGET(*case['args'])
        return
    assert TARGET(*case['args']) == case['expected']
