
# Profile DataFrame

## Tests on individual columns

Base 
    * `Count Missing`
    * `Mode`
    * `All Unique`
    * `All Same`
    * `All Null`

Number(Base) e.g. Float, Int, Date, Datetime
    * `Min`
    * `Max`
    * `Percentiles`
    * `Outliers`

String(Base)
    * `Min Length`
    * `Max Length`
    * `Outliers`
    * FLAG - Ignore Whitespace

## Tests across columns

Base
    * Identical columns

Number(Base)
    * Pairs
    * Correlation between columns
    * Multicollinearity
    
String(Base)
    * Correlation between columns

## Tests across rows

Base
    * Identical rows


### References
* [Stackoverflow with pandas](http://stackoverflow.com/questions/17095101/outputting-difference-in-two-pandas-dataframes-side-by-side-highlighting-the-d)
* [Practical business python example](http://pbpython.com/excel-diff-pandas.html)