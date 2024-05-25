import os
from pathlib import Path


p = Path('test')


def exists(filename: str) -> bool:
    p = Path(filename)
    return p.exists()


def file_exists(filename: str) -> bool:
    f = Path(filename)
    return p.exists() and p.is_file()


def dir_exists(dirname: str) -> bool:
    d = Path(dirname)
    return d.exists() and d.is_dir()
