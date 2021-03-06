import numpy as np
import pandas as pd
import string
import re


def fuzzy_compare(str1, str2):
    """Compare strings ignoring whitespace, punctuation and case."""
    remove = string.whitespace + string.punctuation
    rgx = re.compile('[%s]' % remove)
    str1 = rgx.sub('', str1).lower()
    str2 = rgx.sub('', str2).lower()
    # TODO(danmat) Create series version. Use pandas.Series.str.replace.
    return str1 == str2


def find_series_type(ser):
    """Determine data type of series"""
    # todo(danmat) Are the values in the list homogeneous
    # todo(danmat) Add detection for dates
    # Are they strings?
    if ser.dtype in (np.float64, np.int64, int, float):
        return 'numeric'
    else:
        return 'string'


def series_to_string(self,ser):
    pass


class Profile:
    """Base tests for all data types."""

    def __init__(self, data):
        self.data = data
        self.results = pd.DataFrame(columns=['Test', 'Result', 'Annotation'])
        # TODO(danmat) Add actual data type of series to result

        # Direct tests as needed
        self.base_stats()

        if find_series_type(self.data) == 'numeric':
            self.test_numeric()
        elif find_series_type(self.data) == 'string':
            self.test_strings()

    def store_result(self, test, result, annotation=''):
        self.results = self.results.append({'Test': test, 'Result': result,
                                           'Annotation': annotation},
                                           ignore_index=True)
        return

    def base_stats(self):
        """Calculate tests on counts."""
        # Prep variable to be used later
        data = self.data
        count = int(len(data))
        count_distinct = int(len(set(data)))
        count_missing = int(data.isnull().sum())

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

        self.store_result('Highest values', data.sort_values(ascending=False).head().values)

        self.store_result('Lowest values', data.sort_values().head().values)
        #TODO(danmat) Add logic to more intuitively display small lists e.g. overlap of above two.

    def test_numeric(self):
        """Test numeric data"""
        data = self.data
        mode = data.mode().tolist()

        self.store_result('Mode', mode)

        self.store_result('Quantiles', data.quantile([.25, .50, .75]).data)

        pass

    def test_dates(self):
        """Test dates"""
        # Test dates
        # Test for contiguous ranges
        # Test for sensical dates, typically this means between 1900 and 2050, make configurable
        pass

    def test_strings(self):
        """Test strings."""
        # TODO(danmat) Add special handling for categorical data
        # Prep variable to be used later
        data = self.data

        # Are all values UPPER or lower case?
        self.store_result('All upper', all([x.isupper() for x in data]))
        self.store_result('All lower', all([x.islower() for x in data]))
        self.store_result('Any upper', any([x.isupper() for x in data]))
        self.store_result('Any lower', any([x.islower() for x in data]))

        # Duplicates when all values are UPPERED or lowered
        # pandas.Series.str.isupper()

        # What character set?

        # Whitespace? At the beginning? At the end?
        # Values with whitespace


        # Some values the same if _ replaced with space?

        # Value counts
        # self.store_result('Value counts', data.value_counts())


        # Are all strings valid dates?

        # Are all strings valid ints or floats

if __name__ == '__main__':
    print('\nexamining test_series_1')
    test_series_1 = pd.Series([1, 1, 1, 1, 1, 1, 1])
    report = Profile(test_series_1)
    print(report.results)

    print('\nexamining test_series_2')
    test_series_2 = pd.Series([1, 3, 999, 1, 9, 1, 1])
    report = Profile(test_series_2)
    print(report.results)

    print('\nexamining test_series_3')
    test_series_3 = pd.Series(range(10000))
    report = Profile(test_series_3)
    print(report.results)

    print('\nexamining test_series_4')
    test_series_4 = pd.Series(['bob', 'bob', 'susan', 'frank', 'FRANK'])
    report = Profile(test_series_4)
    print(report.results)

