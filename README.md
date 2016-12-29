
# Profile Pandas DataFrame

## Goals

1. Leverage Pandas. Require input in DataFrame or Series inputs. 
1. Ease early stage data analysis. E.g. get quick, broad feel of the data.
1. Extensible to customizing for other data


### Sample usage

```
>>> df = pd.DataFrame({'col0': ['one','one','one','two','two'],
                       'col1': ['A', 'B', 'C', 'A', 'B'],
                       'col2': [1, 2, 3, 4, 5]})
>>> df
>>> df.profile()
```

## Tests on columns

Base tests

    * `Count`, [`Empty`]
    * `Count distinct`, [`All identical`, `All unique`] 
    * `Count missing`, [`All missing`]

Number tests

    * `Underlying data type`
    * `Min`
    * `Max`
    * `Quartiles`
    * `Mode`
    * `Standard Deviation`
    * `Skew`
    * `Kurtosis`
    * `Mean`
    * `Trimmed Mean`
    
    * `Example numeric outliers` e.g. >= 3 standard deviations

Date tests

    * Contiguous check
    * Odd looking dates e.g. bad conversion from epoch to give 1000x off


String tests

    * Value counts
    * `Min Length`
    * `Max Length`
    * `String Outliers` outliers by number of occurences, outliers by length of string
    * FLAG - Ignore Whitespace
    * Could actually be a date
    * Could actually be a currency
    
    * 'Example string outliers' e.g. 

## Tests across columns

Base

    * Columns with identical values; enable export of columns to enable easy correction
    * Columns with identical headers
    * Find possible combo keys to dataset.
    * multi-colinearity

Number(Base)

    * Pairs
    * Correlation between columns
    * Multicollinearity
    
String(Base)

    * Correlation between columns

## Tests across rows

Base

    * Count rows (if zero, then stop running tests)
    * Identical rows e.g. df.duplicated. Give user command to drop duplicate rows


### References
* [Stackoverflow with pandas](http://stackoverflow.com/questions/17095101/outputting-difference-in-two-pandas-dataframes-side-by-side-highlighting-the-d)
* [Practical business python example](http://pbpython.com/excel-diff-pandas.html)






print('\nexamining test_series_1')
test_series_1 = pd.Series([1, 1, 1, 1, 1, 1, 1])
report = Profile(test_series_1)
print(report.results)

print('\nexamining test_series_2')
test_series_2 = pd.Series([1, 3, 999, 1, 9, 1, 1])
report = Profile(test_series_2)
print(report.results)

print('\nexamining test_series_3')
test_series_3 = pd.Series(range(10))
report = Profile(test_series_3)
print(report.results)


DescribeBy like in the R psych package
http://www.statmethods.net/stats/descriptives.html