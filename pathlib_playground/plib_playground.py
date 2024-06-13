from pathlib import Path
import sys

test_dir: Path = Path('test_dir')

if test_dir.is_dir():
    print(f'{test_dir} already exists. Would you like to remove it?')
    while True:
        remove: str = input("Enter Y or N ").strip()
        if remove == "N":
            sys.exit('Exiting')
        elif remove == "Y":
            test_dir.rmdir()
            sys.exit('Exiting')
else:
    test_dir.mkdir()

abs_path: Path = test_dir.resolve()
print(abs_path)


test_file: Path = Path(test_dir / 'test_file.txt')

test_file.touch()
test_file.write_text('Hello Path-made file!\n')

