import os
from pathlib import Path


def exists(filename: Path) -> bool:
    p: Path = Path(filename)
    return p.exists()


def file_exists(filename: Path) -> bool:
    f = Path(filename)
    return f.is_file()


def dir_exists(directory: Path) -> bool:
    d = Path(directory)
    return d.is_dir()


if __name__ == '__main__':
    my_file = Path('fake-file')
    my_dir = Path('fake-directory')

    os.system('touch fake-file')

    assert exists(my_file) is True
    assert file_exists(my_file) is True

    os.system('rm fake-file')

    os.system('mkdir fake-directory')

    assert exists(my_dir) is True
    assert dir_exists(my_dir) is True

    os.system('rmdir fake-directory')
