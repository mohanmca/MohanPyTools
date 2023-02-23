import unittest
from mapping import recon


class TestMapping(unittest.TestCase):

    def test_common_kv(self):
        in_dict1 = {"a": 1, "b": 2, "c": 3, "d": "9"}
        in_dict2 = {"a": 1, "b": 7, "e": 4, "f": 3, "k": 8, "l": 13}
        result = recon(dict1=in_dict1, dict2=in_dict2)
        self.assertEqual(result['common_kv_1'], [("a", 1)], "Should have same kv")

    def test_common_v(self):
        in_dict1 = {"a": 1, "b": 2, "c": 3, "d": "9"}
        in_dict2 = {"a": 1, "b": 7, "e": 4, "f": 3, "k": 8, "l": 13}
        result = recon(dict1=in_dict1, dict2=in_dict2)
        self.assertEqual(result['common_k_2'], [("b", 2, 7)], "Should have same kv")


if __name__ == '__main__':
    unittest.main()
