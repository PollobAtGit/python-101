class FileWrapper:
    def __enter__(self):
        self._file = open('D:\\tmp', 'r')
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
