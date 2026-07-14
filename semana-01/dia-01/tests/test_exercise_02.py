from __future__ import annotations

import builtins
import pytest

from prep_test_utils import load_callable

TARGET = load_callable(
    __file__,
    exercise_filename='exercise_02.py',
    solution_filename='exercise_02_solution.py',
    callable_name='longest_consistent_note',
)

CASES = [{'name': 'normal', 'args': ['abc12345z'], 'expected': 5}, {'name': 'empty', 'args': [''], 'expected': 0}, {'name': 'single', 'args': ['7'], 'expected': 1}, {'name': 'duplicates', 'args': ['aa11bbb22'], 'expected': 3}, {'name': 'invalid_chars', 'args': ['ab!!123'], 'expected': 3}, {'name': 'large_basic', 'args': ['abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc123456'], 'expected': 120}]


@pytest.mark.parametrize('case', CASES, ids=[case['name'] for case in CASES])
def test_cases(case):
    if 'raises' in case:
        with pytest.raises(getattr(builtins, case['raises'])):
            TARGET(*case['args'])
        return
    assert TARGET(*case['args']) == case['expected']
