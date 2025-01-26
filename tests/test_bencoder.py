import logging
import unittest
from src.bencoder import bencode

# setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestBencoder(unittest.TestCase):
    """
    Test cases for bencode funtionality testing
    """
    def test_bencode_string(self):
        """Simple string encoding tests"""
        logger.info("Running test_bencode_string")
        self.assertEqual(bencode("spam"), "4:spam")

    def test_bencode_integer(self):
        """Simple integer encoding tests"""
        logger.info("Running test_bencode_integer")
        self.assertEqual(bencode(123), "i123e")

    def test_bencode_list(self):
        """Simple list encoding tests"""
        logger.info("Running test_bencode_list")
        self.assertEqual(bencode(["spam", "eggs"]), "l4:spam4:eggse")

    def test_bencode_dictionary(self):
        """Simple dictionary encoding tests"""
        logger.info("Running test_bencode_dictionary")
        self.assertEqual(bencode({"cow": "moo", "spam": "egg"}), "d3:cow3:moo4:spam3:egge")

    def test_bencode_all(self):
        """All encoding tests"""
        logger.info("Running test_bencode_all")
        self.assertEqual(bencode("spam"), "4:spam")
        self.assertEqual(bencode(123), "i123e")
        self.assertEqual(bencode(["spam", "egg"]), "l4:spam3:egge")
        self.assertEqual(bencode([123, "spam", ["eggs", "ham"]]), "li123e4:spaml4:eggs3:hamee")
        self.assertEqual(bencode({"cow": "moo", "spam": "egg"}), "d3:cow3:moo4:spam3:egge")


if __name__ == "__main__":
    unittest.main()
