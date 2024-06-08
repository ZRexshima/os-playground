import os
from pathlib import Path


def exists(filename: str) -> bool:
    p = Path(filename)
    return p.exists()


def file_exists(filename: str) -> bool:
    f = Path(filename)
    return f.is_file()


def dir_exists(dirname: str) -> bool:
    d = Path(dirname)
    return d.is_dir()


if __name__ == '__main__':
    p = Path('fake-file')
    d = Path('fake-directory')

    os.system('touch fake-file')

    assert exists(p) is True
    assert file_exists(p) is True

    os.system('rm fake-file')

    os.system('mkdir fake-directory')

    assert exists(d) is True
    assert dir_exists(d) is True

    os.system('rmdir fake-directory')
