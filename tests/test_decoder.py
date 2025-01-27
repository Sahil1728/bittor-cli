import logging
import unittest
from src.bdecoder import bdecode

# setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestDecoder(unittest.TestCase):
    def test_bdecode_string(self):
        logger.info("Running test_bdecode_string")
        self.assertEqual(bdecode("4:spam"), b"spam")

    def test_bdecode_integer(self):
        logger.info("Running test_bdecode_integer")
        self.assertEqual(bdecode("i123e"), 123)
        self.assertEqual(bdecode("i-123e"), -123)
        self.assertEqual(bdecode("i0e"), 0)

    def test_bdecode_list(self):
        logger.info("Running test_bdecode_list")
        self.assertEqual(bdecode("li1eli2eli3eeee"), [1, [2, [3]]])
        self.assertEqual(bdecode("l4:spam4:eggse"), [b"spam", b"eggs"])
        self.assertEqual(bdecode("l1:a3:bcde"), [b"a", b"bcd"])
        self.assertEqual(bdecode("li3e5:abcdee"), [3, b"abcde"])
        self.assertEqual(bdecode("l2:ab2:cdli12ei2ei-3el2:ef2:ghee2:abe"), 
                         [b"ab", b"cd", [12, 2, -3, [b"ef", b"gh"]], b"ab"])
    
    def test_bdecode_dictionary(self):
        logger.info("Running test_bdecode_dictionary")
        self.assertEqual(bdecode("d3:cow3:moo4:spam3:egge"), {b"cow": b"moo", b"spam": b"egg"})

    # def test_bdecode_all(self):
    #     logger.info("Running test_bdecode_all")
    #     self.assertEqual(bdecode("4:spam"), b"spam")
    #     self.assertEqual(bdecode("i123e"), 123)
    #     self.assertEqual(bdecode("l4:spam3:egge"), [b"spam", b"egg"])
    #     self.assertEqual(bdecode("d3:cow3:moo4:spam3:egge"), {b"cow": b"moo", b"spam": b"egg"})


if __name__ == "__main__":
    unittest.main()
