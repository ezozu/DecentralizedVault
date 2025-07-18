# test_decentralizedvault.py
"""
Tests for DecentralizedVault module.
"""

import unittest
from decentralizedvault import DecentralizedVault

class TestDecentralizedVault(unittest.TestCase):
    """Test cases for DecentralizedVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DecentralizedVault()
        self.assertIsInstance(instance, DecentralizedVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DecentralizedVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
