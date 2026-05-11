# test_yamlwriter.py
"""
Tests for YAMLWriter module.
"""

import unittest
from yamlwriter import YAMLWriter

class TestYAMLWriter(unittest.TestCase):
    """Test cases for YAMLWriter class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = YAMLWriter()
        self.assertIsInstance(instance, YAMLWriter)
        
    def test_run_method(self):
        """Test the run method."""
        instance = YAMLWriter()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
