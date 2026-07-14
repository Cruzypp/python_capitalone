from __future__ import annotations

import builtins
import pytest

from prep_test_utils import load_callable

TARGET = load_callable(
    __file__,
    exercise_filename='exercise_01.py',
    solution_filename='exercise_01_solution.py',
    callable_name='first_repeated_customer',
)

CASES = [{'name': 'normal', 'args': [['c1', 'c2', 'c3', 'c2', 'c4']], 'expected': 'c2'}, {'name': 'empty', 'args': [[]], 'expected': None}, {'name': 'single', 'args': [['c1']], 'expected': None}, {'name': 'duplicates', 'args': [['x', 'x']], 'expected': 'x'}, {'name': 'large_basic', 'args': [['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14', 'c15', 'c16', 'c17', 'c18', 'c19', 'c20', 'c21', 'c22', 'c23', 'c24', 'c25', 'c26', 'c27', 'c28', 'c29', 'c30', 'c31', 'c32', 'c33', 'c34', 'c35', 'c36', 'c37', 'c38', 'c39', 'c40', 'c41', 'c42', 'c43', 'c44', 'c45', 'c46', 'c47', 'c48', 'c49', 'c20']], 'expected': 'c20'}]


@pytest.mark.parametrize('case', CASES, ids=[case['name'] for case in CASES])
def test_cases(case):
    if 'raises' in case:
        with pytest.raises(getattr(builtins, case['raises'])):
            TARGET(*case['args'])
        return
    assert TARGET(*case['args']) == case['expected']
