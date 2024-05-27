from osplayground import dir_exists
from osplayground import exists
from osplayground import file_exists


def test_file_exists(tmp_path):
    f = tmp_path / 'fake-file.txt'
    f.write_text('fake fake fake')
    
    assert f.exists() == True
    assert file_exists(f) == True
    assert f.is_file() == True


def test_dir_exists(tmp_path):
    d = tmp_path / 'dir'
    d.mkdir()
    
    assert d.exists() == True    
    assert dir_exists(d) == True
    assert d.is_dir() == True


def test_exists_with_dir(tmp_path):
    d = tmp_path / 'test_dir'
    d.mkdir()

    assert exists(d) == True
    assert d.exists() == True
    assert d.is_dir() == True

def test_exists_with_file(tmp_path):
    f = tmp_path / 'test.txt'
    f.write_text('blah blah blah')

    assert exists(f) == True
    assert f.exists() == True
    assert f.is_file() == True
