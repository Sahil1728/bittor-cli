import unittest
from src.bencoder import bencode


class TestBencoder(unittest.TestCase):
    def test_bencode_string(self):
        self.assertEqual(bencode("spam"), "4:spam")

    def test_bencode_integer(self):
        self.assertEqual(bencode(123), "i123e")

    def test_bencode_list(self):
        self.assertEqual(bencode(["spam", "eggs"]), "l4:spam4:eggse")

    def test_bencode_dictionary(self):
        self.assertEqual(bencode({"cow": "moo", "spam": "egg"}), "d3:cow3:moo4:spam3:egge")

    def test_bencode_all(self):
        self.assertEqual(bencode("spam"), "4:spam")
        self.assertEqual(bencode(123), "i123e")
        self.assertEqual(bencode(["spam", "egg"]), "l4:spam3:egge")
        self.assertEqual(bencode({"cow": "moo", "spam": "egg"}), "d3:cow3:moo4:spam3:egge")


if __name__ == "__main__":
    unittest.main()
