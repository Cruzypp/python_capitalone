from __future__ import annotations

import importlib.util
import os
from pathlib import Path


def load_callable(test_file: str, exercise_filename: str, solution_filename: str, callable_name: str):
    base = Path(test_file).resolve().parent.parent
    target = os.environ.get('INTERVIEW_PREP_TARGET', 'exercise')
    if target == 'solution':
        path = base / 'solutions' / solution_filename
    else:
        path = base / 'exercises' / exercise_filename
        if not path.exists():
            path = base / 'assessment' / exercise_filename
    spec = importlib.util.spec_from_file_location(f'{path.stem}_{target}', path)
    if spec is None or spec.loader is None:
        raise ImportError(f'Cannot load module from {path}')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, callable_name)
