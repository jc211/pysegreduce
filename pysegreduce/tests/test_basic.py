"""
Basic tests for the pysegreduce package.
"""

import unittest
import pysegreduce

class TestBasic(unittest.TestCase):
    """Basic tests for the pysegreduce module."""
    
    def test_module_imports(self):
        """Test that the module functions can be imported."""
        self.assertTrue(hasattr(pysegreduce, 'reduce_vec3f'))
        self.assertTrue(hasattr(pysegreduce, 'reduce_mat33f'))
        
        # Check that these are callable
        self.assertTrue(callable(pysegreduce.reduce_vec3f))
        self.assertTrue(callable(pysegreduce.reduce_mat33f))

if __name__ == "__main__":
    unittest.main() 