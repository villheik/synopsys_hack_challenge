import unittest
from ddt import ddt, data, file_data, unpack
from pydoc import locate
from synopsys.pesti import processor

# Data-driven tests.
# Takes input data from "test_data.json" and generates test cases based on
# contents of the file.
@ddt
class DdtRunner(unittest.TestCase):
    @file_data("test_data.json")
    def test_all_processors(self, classname, input, output):
        self.assertEqual(processor.process(classname, input), output)
        
