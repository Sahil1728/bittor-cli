import logging
import unittest
from src.bdecoder import bdecode

# setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestDecoder(unittest.TestCase):
    def test_bdecode_string(self):
        logger.info("Running test_bdecode_string")
        self.assertEqual(bdecode("4:spam"), "spam")

    def test_bdecode_integer(self):
        logger.info("Running test_bdecode_integer")
        self.assertEqual(bdecode("i123e"), 123)
        self.assertEqual(bdecode("i-123e"), -123)
        self.assertEqual(bdecode("i0e"), 0)

    def test_bdecode_list(self):
        logger.info("Running test_bdecode_list")
        self.assertEqual(bdecode("l4:spam4:eggse"), ["spam", "eggs"])
        self.assertEqual(bdecode("l1:a3:bcde"), ["a", "bcd"])
        self.assertEqual(bdecode("li3e5:abcdee"), [3, "abcde"])
    # def test_bdecode_dictionary(self):
    #     logger.info("Running test_bdecode_dictionary")
    #     self.assertEqual(bdecode("d3:cow3:moo4:spam3:egge"), {"cow": "moo", "spam": "egg"})

    def test_bdecode_all(self):
        logger.info("Running test_bdecode_all")
        self.assertEqual(bdecode("4:spam"), "spam")
        self.assertEqual(bdecode("i123e"), 123)
        self.assertEqual(bdecode("l4:spam3:egge"), ["spam", "egg"])
    #     self.assertEqual(bdecode("d3:cow3:moo4:spam3:egge"), {"cow": "moo", "spam": "egg"})


if __name__ == "__main__":
    unittest.main()
