from __future__ import annotations

import builtins
import pytest

from prep_test_utils import load_callable

TARGET = load_callable(
    __file__,
    exercise_filename='exercise_02.py',
    solution_filename='exercise_02_solution.py',
    callable_name='shortest_notes_window',
)

CASES = [{'name': 'normal', 'args': ['ABCADEB', 'CDE'], 'expected': 'CADE'}, {'name': 'empty', 'args': ['', 'A'], 'expected': ''}, {'name': 'single', 'args': ['A', 'A'], 'expected': 'A'}, {'name': 'duplicates', 'args': ['AAABBC', 'ABC'], 'expected': 'ABBC'}, {'name': 'impossible', 'args': ['ABC', 'Z'], 'expected': ''}]


@pytest.mark.parametrize('case', CASES, ids=[case['name'] for case in CASES])
def test_cases(case):
    if 'raises' in case:
        with pytest.raises(getattr(builtins, case['raises'])):
            TARGET(*case['args'])
        return
    assert TARGET(*case['args']) == case['expected']
