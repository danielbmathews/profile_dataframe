import numpy as np
import pandas as pd

class Tests:
    """Base tests for all data types"""

    def __init__(self, data):
        self.data = data
        self.results = pd.DataFrame(columns=['Test', 'Result', 'Annotation'])
        self.results2 = []

    def store_result(self, test, result, annotation=''):
        self.results = self.results.append({'Test': test,
                             'Result': result,
                             'Annotation': annotation}, ignore_index=True)
        return

    def counts(self):
        # Prepare variables for count tests
        count = len(self.data)
        count_distinct = len(set(self.data))
        count_missing = self.data.isnull().sum()
        # Check for specific annotations
        annotation = ''
        if count == 0:
            annotation = 'no records'
        elif count_missing == count:
            annotation = 'all missing'
        elif count_distinct == 1:
            annotation = 'all identical'
        elif count_distinct == count:
            annotation = 'all unique'
        self.store_result('Count', count, annotation)

    def mode(self):
        """Mode"""
        return self.data.mode().to_string(index=False)


test_series = pd.Series([1, 1, 1, 1, 1, 1, 1])
report = Tests(test_series)
report.counts()
print report.results
