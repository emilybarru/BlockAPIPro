# test_blockapipro.py
"""
Tests for BlockAPIPro module.
"""

import unittest
from blockapipro import BlockAPIPro

class TestBlockAPIPro(unittest.TestCase):
    """Test cases for BlockAPIPro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockAPIPro()
        self.assertIsInstance(instance, BlockAPIPro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockAPIPro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
