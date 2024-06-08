from osplayground import dir_exists
from osplayground import exists
from osplayground import file_exists


def test_file_exists(tmp_path):
    # create a temporary file and write text into it
    f = tmp_path / 'test.txt'
    f.write_text('blah blah blah')
    
    assert f.exists() is True
    assert file_exists(f) is True
    assert f.is_file() is True


def test_dir_exists(tmp_path):
    # create a temporary directory
    d = tmp_path / 'dir'
    d.mkdir()
    
    assert d.exists() is True
    assert dir_exists(d) is True
    assert d.is_dir() is True
