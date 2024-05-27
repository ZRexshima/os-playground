# os module playground

## os-playground.py

This file demonstrates some uses of the Path object defined in the pathl ib library.

### Path.exists()

Using the Path.exists() method on a filesystem object, whether file or directory, returns a bool of True if the object exists.

### Path.is_file()

The Path.is_file() method can be used to verify an object exists and is a file, not a directory. False will be returned if the object does not exist or if the object exists and is a directory. True will only be returned if the object exists and is a regular file.

### Path.is_dir()

Likewise, Path.is_dir() can confirm the object exists and is a directory.
