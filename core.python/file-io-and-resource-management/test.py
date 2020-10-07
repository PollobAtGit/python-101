import unittest
from io import TextIOWrapper

from .FileWrapper import FileWrapper
from .FileWrapperFunc import file_wrapper


class ResourceManagementTest(unittest.TestCase):

    def test_underlying_object_of_file_wrapper_is_text_io_wrapper(self):
        with FileWrapper() as f:
            self.assertIsInstance(f, TextIOWrapper)

    # TODO rename
    def test_outside_scope_file_is_disposed(self):
        with FileWrapper() as f:
            pass
        self.assertTrue(f.closed)

    def test_underlying_object_of_file_wrapper_created_with_context_manager_decorator_is_text_io_wrapper(self):
        with file_wrapper() as f:
            self.assertIsInstance(f, TextIOWrapper)

    # TODO rename
    def test_file_wrapper_outside_scope_file_is_disposed(self):
        with file_wrapper() as f:
            pass
        self.assertTrue(f.closed)


if __name__ == "__main__":
    unittest.main()
