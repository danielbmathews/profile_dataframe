import numpy as np
import pandas as pd


def find_series_type(self):
    """Determine data type of series"""
    # todo(danmat) Are the values in the list homogeneous
    # Are they strings?
    if self.dtype in (np.float64, np.int64, int, float):
        return 'numeric'
    else:
        return 'string'


class Profile:
    """Base tests for all data types."""

    def __init__(self, data):
        self.data = data
        self.results = pd.DataFrame(columns=['Test', 'Result', 'Annotation'])

        # Direct tests as needed
        if find_series_type == 'numeric':
            self.counts()
        elif find_series_type == 'string':
            self.test_strings()

    def store_result(self, test, result, annotation=''):
        self.results = self.results.append({'Test': test, 'Result': result,
                                           'Annotation': annotation},
                                           ignore_index=True)
        return

    def counts(self):
        """Calculate tests on counts."""
        # Prep variable to be used later
        data = self.data
        count = int(len(data))
        count_distinct = int(len(set(data)))
        count_missing = int(data.isnull().sum())
        mode = data.mode().tolist()

        # count
        if count == 0:
            count_note = 'no records'
        else:
            count_note = ''
        self.store_result('Count', count, count_note)

        # count_distinct
        if count_distinct == 1:
            count_distinct_note = 'all identical'
        elif count_distinct == count:
            count_distinct_note = 'all unique'
        else:
            count_distinct_note = ''
        self.store_result('Count distinct', count_distinct, count_distinct_note)

        # count_missing
        if count_missing == count:
            count_missing_note = 'all missing'
        else:
            count_missing_note = 'no missing'
        self.store_result('Count missing', count_missing, count_missing_note)

        self.store_result('Mode', mode)

        self.store_result('Quantiles', data.quantile([.25, .50, .75]).data)

    def test_dates(self):
        """Create tests on dates."""
        # Test dates
        # Test for contiguous ranges
        # Test for sensical dates, typically this means between 1900 and 2050, make configurable
        pass

    def test_strings(self):
        """Create teats on strings."""
        # Prep variable to be used later
        data = self.data

        # Are all values UPPER or lower case?
        self.store_result('All upper', all([x.upper() for x in data]))
        self.store_result('All lower', all([x.lower() for x in data]))
        self.store_result('Any upper', any([x.lower() for x in data]))
        self.store_result('Any lower', any([x.lower() for x in data]))

        # Duplicates when all values are UPPERED or lowered
        # pandas.Series.str.isupper()

        # What character set?

        # Whitespace? At the beginning? At the end?

        # Some values the same if _ replaced with space?

        # Value counts
        # self.store_result('Value counts', data.value_counts())

        # First according to alphabetical order

        # Last according to alphabetical order

        # Are all strings valid dates?

        # Are all strings valid ints or floats
