import numpy as np
import pandas as pd

class Tests:
    """Base tests for all data types"""

    def __init__(self, data):
        self.data = data

    def count(self):
        """Count of items"""
        return len(self.data)

    def count_distinct(self):
        """Distinct count of items"""
        return len(set(self.data))

    def count_missing(self):
        """Count missing items"""
        return self.data.isnull().sum()

    def mode(self):
        """Mode"""
        

    def report(self):
        """Report out tests"""
        tests = [self.count,
                 self.count_distinct,
                 self.count_missing]
        template = '{tests:<30}{results:>50}'
        print '--- Results ---'
        for t in tests:
            print template.format(tests=t.__doc__, results=t())


test_series = pd.Series([1, 2, 3, 3, np.NaN, 5, -3])
report = Tests(test_series)
report.report()