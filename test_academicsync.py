# test_academicsync.py
"""
Tests for AcademicSync module.
"""

import unittest
from academicsync import AcademicSync

class TestAcademicSync(unittest.TestCase):
    """Test cases for AcademicSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AcademicSync()
        self.assertIsInstance(instance, AcademicSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AcademicSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
