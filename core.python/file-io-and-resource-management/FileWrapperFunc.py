from contextlib import contextmanager


@contextmanager
def file_wrapper():
    f = open('D:\\tmp', 'r')
    yield f
    f.close()
