from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file("numbers.txt", "r") as f:
    print(f.read())

print(f.closed)
