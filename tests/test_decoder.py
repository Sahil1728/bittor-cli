import unittest
from src.bdecoder import bdecode


class TestDecoder(unittest.TestCase):
    def test_bdecode_string(self):
        self.assertEqual(bdecode("4:spam"), "spam")

    def test_bdecode_integer(self):
        self.assertEqual(bdecode("i123e"), 123)
        self.assertEqual(bdecode("i-123e"), -123)
        self.assertEqual(bdecode("i0e"), 0)

    # def test_bdecode_list(self):
    #     self.assertEqual("l4:spam4:eggse", bdecode(["spam", "eggs"]))

    # def test_bdecode_dictionary(self):
    #     self.assertEqual(bdecode("d3:cow3:moo4:spam3:egge"), {"cow": "moo", "spam": "egg"})

    # def test_bdecode_all(self):
    #     self.assertEqual(bdecode("4:spam"), "spam")
    #     self.assertEqual(bdecode("i123e"), 123)
    #     self.assertEqual(bdecode("l4:spam3:egge"), ["spam", "egg"])
    #     self.assertEqual(bdecode("d3:cow3:moo4:spam3:egge"), {"cow": "moo", "spam": "egg"})


if __name__ == "__main__":
    unittest.main()
