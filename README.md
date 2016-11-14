
# Profile Pandas DataFrame

## Tests on individual columns

Tests consists of a name, tests and when applicable an interpretation.

Base

    * `Count`, [`Empty`]
    * `Count distinct`, [`All identical`, `All unique`] 
    * `Count missing`, [`All missing`]
    * `Mode`

Number(Base) e.g. Float, Int, Date, Datetime

    * `Min`
    * `First quartile`
    * `Second quartile`
    * `Third quartile`
    * `Fourth quartile`
    * `Max`
    * `Standard Deviation`
    * `Skew`
    * `Kurtosis`
    
    * `Example Numeric Outliers` - >= 3 standard deviations
    * ``
    
    

String(Base)

    * `Min Length`
    * `Max Length`
    * `String Outliers`
    * FLAG - Ignore Whitespace

## Tests across columns

Base

    * Columns with identical values
        * Give user command to drop duplicate columns
    * Columns with identical headers

Number(Base)

    * Pairs
    * Correlation between columns
    * Multicollinearity
    
String(Base)

    * Correlation between columns

## Tests across rows

Base

    * Count rows (if zero, then stop running tests)
    * Identical rows e.g. df.duplicated
        * Give user command to drop duplicate rows


### References
* [Stackoverflow with pandas](http://stackoverflow.com/questions/17095101/outputting-difference-in-two-pandas-dataframes-side-by-side-highlighting-the-d)
* [Practical business python example](http://pbpython.com/excel-diff-pandas.html)