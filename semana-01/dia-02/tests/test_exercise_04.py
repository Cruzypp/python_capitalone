from __future__ import annotations

import builtins
import pytest

from prep_test_utils import load_callable

TARGET = load_callable(
    __file__,
    exercise_filename='exercise_04.py',
    solution_filename='exercise_04_solution.py',
    callable_name='duplicate_transaction_ids',
)

CASES = [{'name': 'normal', 'args': [['t1', 't2', 't1', 't3', 't2', 't2']], 'expected': ['t1', 't2']}, {'name': 'empty', 'args': [[]], 'expected': []}, {'name': 'single', 'args': [['t1']], 'expected': []}, {'name': 'duplicates', 'args': [['a', 'a', 'a']], 'expected': ['a']}, {'name': 'large_basic', 'args': [['x', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', 'x']], 'expected': ['x']}]


@pytest.mark.parametrize('case', CASES, ids=[case['name'] for case in CASES])
def test_cases(case):
    if 'raises' in case:
        with pytest.raises(getattr(builtins, case['raises'])):
            TARGET(*case['args'])
        return
    assert TARGET(*case['args']) == case['expected']
