import unittest
import numpy as np
import pandas as pd
from profile import find_series_type, fuzzy_compare


class TestProfile(unittest.TestCase):

    def test_find_list_type(self):
        self.assertEqual(find_series_type(pd.Series([1, 1])), 'numeric')
        self.assertEqual(find_series_type(pd.Series([1, np.nan])), 'numeric')
        self.assertEqual(find_series_type(pd.Series(['a', 'b'])), 'string')
        self.assertEqual(find_series_type(pd.Series(['a', ''])), 'string')

    def test_fuzzy_compare(self):
        self.assertTrue(fuzzy_compare('MISSING DATA', 'Missing-data'))
        self.assertTrue(fuzzy_compare('fatal_error', 'Fatal Error'))

if __name__ == '__main__':
    unittest.main()
