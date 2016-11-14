import numpy as np
import pandas as pd


class Tests:
    """Base tests for all data types"""

    def __init__(self, data):
        self.data = data
        self.results = pd.DataFrame(columns=['Test', 'Result', 'Annotation'])

    def store_result(self, test, result, annotation=''):
        self.results = self.results.append({'Test': test, 'Result': result,
                                           'Annotation': annotation},
                                           ignore_index=True)
        return

    def counts(self):
        # Prepare variables for count tests
        count = len(self.data)
        count_distinct = len(set(self.data))
        count_missing = self.data.isnull().sum()
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

    def mode(self):
        """Mode"""
        return self.data.mode().to_string(index=False)


test_series = pd.Series([1, 1, 1, 1, 1, 1, 1])
report = Tests(test_series)
report.counts()
print report.results
