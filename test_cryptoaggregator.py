# test_cryptoaggregator.py
"""
Tests for CryptoAggregator module.
"""

import unittest
from cryptoaggregator import CryptoAggregator

class TestCryptoAggregator(unittest.TestCase):
    """Test cases for CryptoAggregator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoAggregator()
        self.assertIsInstance(instance, CryptoAggregator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoAggregator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
