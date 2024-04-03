# How to create Pandas DataFrames for testing

When working with Pandas in Python, constantly we need some DataFrames for different purposes, such as testing your Python code to check any errors and benckmarking code performance.

Here I will explain how to create test Pandas DataFrames with the help of AI. At the end, I will put all the code together so we can use it everywhere to create different DataFrames when needed.

## Data types
The data types commonly used in a DataFrame are string, datetime, integer, and float. All other data types can be converted from these types. For example we can easily convert integer to bool and convert string to categorical. 

We will use AI to help us generate the draft code for each of the data types and then test and modify the code to ensure it works as expected. The propmpts and the replies will not be included here. But you should always try it yourself if interested.

## Create a string list
To create a list of strings with random lengths, we should be able to control the number of strings and the minimum and maximum string lengths. We should also be able to restrict the chracter set from which the strings are created.

To create a random string, we can first generate a random integer to represent the string length and then randomly select characters from the provided character set.
```py
characters = string.ascii_letters + string.digits
string_length = random.randint(min_length, max_length)
random_string = ''.join(random.choices(characters, k=string_length))
```

We can then use a list comprehension or a for loop to create a list of random strings. We can also use `numpy` for generating random numbers and selecting the characters.


## Create a datetime list
Assume we will create a datetime range for one year with a resolution unit of `second`.

Using `pandas`, this is straightforward
```py
timestamps = pd.date_range(
    start='2020-01-01', 
    end='2021-01-01', 
    freq='s', 
    inclusive='left', 
    unit='s',
)
```

To create a datetime range we can use `numpy` as well
```py
start = np.datetime64('2020-01-01', 's').astype(int)
stop = np.datetime64('2021-01-01', 's').astype(int)
timestamps = np.arange(
    start=start,
    stop=stop, 
    step=(stop - start)//(366*24*3600),
).astype('datetime64[s]')
```

The `pandas` version will be used as it is much faster and more convinient to generate datetime ranges with different frequencies.

We can also generate random datetime values between a range by randomly selecting datetimes from the generated datetime list.

## Create an integer/float list
We can use `random.randint` and `random.uniform` functions to generate random integer and float numbers. 

As the `numpy.random` is built on top of `random` and offers a much richer set of features, we will use the `numpy.random` module to generate random numbers.

```py
rng = np.random.default_rng(seed=rand_seed)
integers = rng.integers(low=low, high=high, size=size)
floats = rng.uniform(low=low, high=high, size=size)
```

## Create a list with missing values
Sometimes our data has missing values, to generate some missing values we can set the percentage of the missing values. We can determine if a value should be missing or not based on the uniform value assigned to that value. 

We should note that different type of data will have different types of missing values. For a string type the missing value is `None`, `np.datetime64('NaT')` for datetime, `np.nan` for float and we need to convert the integer data to float before assigning the missing values.
```py       
mask = rng.uniform(size=len(vals)) <= missing_pct
vals[mask] = missing_val
```

## Create a Pandas DataFrame
To create a DatafRame, we need to specify the number of columns and the data types as well as some properties associated with the columns. 

After putting all parts together and optimizing the code to reduce duplicated code, the final version is here.  
```py
from typing import Union
import string
import numpy as np
import pandas as pd

def gen_rand_strs(
    rng: np.random._generator.Generator,
    str_cnt: int,
    str_len: tuple[int, int],
    str_chars: list[str],
) -> list[str]:
    str_lens = rng.integers(low=str_len[0], high=str_len[1], size=str_cnt, endpoint=True)
    rand_strs = [''.join(rng.choice(str_chars, size=str_len)) for str_len in str_lens]
    return rand_strs

def gen_str_vals(
    size: int,
    rng: np.random._generator.Generator,
    str_cnt: int = None,
    str_len: Union[int, tuple[int, int]] = None,
    str_chars: list[str] = None,
    col_strs: list[str] = None,
) -> np.ndarray:
    if str_cnt is None:
        str_cnt = 10
    if str_len is None:
        str_len = (5, 5)
    elif type(str_len) == int:
        str_len = (str_len, str_len)
    if col_strs is None:
        if str_chars is None:
            str_chars = [c for c in string.ascii_letters + string.digits]
        col_strs = gen_rand_strs(rng, str_cnt, str_len, str_chars)
    val = rng.choice(col_strs, size=size)
    return val

def gen_ts_vals(
    size: int,
    rng: np.random._generator.Generator,
    start_date: str = None,
    end_date: str = None,
    freq: str = None,
    random: bool = False,
) -> np.ndarray:
    if start_date is None:
        start_date = '2024-01-01'
    if end_date is None:
        end_date = '2025-01-01'
    if freq is None:
        freq = 'D'
    if random is None:
        random = False
    val = pd.date_range(start_date, end_date, freq=freq, inclusive='left')[:size]
    if random:
        val = rng.choice(val, size=size)
    return val

def gen_num_vals(
    size: int,
    rng: np.random._generator.Generator,
    low: Union[int, float] = None,
    high: Union[int, float] = None,
    dtype: str = None,
) -> np.ndarray:
    if low is None:
        low = 0
    if high is None:
        high = 2
    func = rng.integers if dtype[0] == 'i' else rng.uniform
    vals = func(low=low, high=high, size=size)
    return vals

def gen_missing_vals(
    vals: np.ndarray,
    rng: np.random._generator.Generator,
    dtype: str,
    missing_pct: float = None,
) -> np.ndarray:
    if missing_pct is None or missing_pct <= 0 or missing_pct >= 1:
        return vals
    if dtype == 's':
        missing_val = None
    elif dtype == 't':
        missing_val = np.datetime64('NaT')
    else:
        missing_val = np.nan
    if dtype == 'i':
        vals = vals.astype(np.float64)
    mask = rng.uniform(size=len(vals)) <= missing_pct
    vals[mask] = missing_val
    return vals

def sanitize_parameters(
    name_prefix: str,
    params: dict,
    par_names: list[str],
):
    if type(params) == int:
        cnt = params
        par = {}
    else:
        cnt = params['count']
        par = {
            k: v + [None] * (cnt - len(v)) if type(v) == list else [v] * cnt
            for k, v in params.items()
        }
    if name_prefix in ('i', 'f'):
        par_names += ['dtype']
        par['dtype'] = [name_prefix] * cnt
    default_val = [None] * cnt
    parameters = [
        {key: par.get(key, default_val)[i] for key in par_names}
        for i in range(cnt)
    ]
    col_names = par.get('name', [f'{name_prefix}{i}' for i in range(1, cnt+1)])
    col_missing_pcts = par.get('missing_pct', default_val)
    return col_names, parameters, col_missing_pcts

def gen_rand_df(
    nrow: int,
    str_cols: dict = None,
    ts_cols: dict = None,
    int_cols: dict = None,
    float_cols: dict = None,
    rand_seed: int = 11,
) -> pd.DataFrame:
    col_types = ['s', 't', 'i', 'f']
    inputs = [str_cols, ts_cols, int_cols, float_cols]
    funcs = [gen_str_vals, gen_ts_vals, gen_num_vals, gen_num_vals]
    par_names = [
        ['str_cnt', 'str_len', 'str_chars', 'col_strs'],
        ['start_date', 'end_date', 'freq', 'random'],
        ['low', 'high'],
        ['low', 'high'],
    ]
    df = pd.DataFrame()
    rng = np.random.default_rng(seed=rand_seed)
    for i, params in enumerate(inputs):
        if params is not None:
            col_names, col_params, col_missing_pcts = sanitize_parameters(
                col_types[i], params, par_names[i]
            )
            df = pd.concat([df, pd.DataFrame({
                col: gen_missing_vals(
                    funcs[i](nrow, rng, **col_params[j]),
                    rng,
                    col_types[i],
                    col_missing_pcts[j],
                ) for j, col in enumerate(col_names)
            })], axis=1)
    return df
```

## Examples
Now let's show how to use the `gen_rand_df` function to create test DataFrames.

This example simply set the number of rows and column date types and leave all other properties as default.
```py
df = gen_rand_df(
    nrow=365*24*60,
    str_cols=1,
    ts_cols=2,
    int_cols=1,
    float_cols=2,
)
print(df[:2])
```

Output:
```
      s1         t1         t2  i1        f1       f2
0  IZD8v 2024-01-01 2024-01-01   0  1.593760  1.64884
1  P9r1i 2024-01-02 2024-01-02   0  1.622772  1.94318
```

Here we provide another example to show how to set all the properties for different data type columns.
```py
d2 = gen_rand_df(
    nrow=10,
    str_cols={
        'count': 2,
        'name': ['country', 'color'],
        'str_len': [3, (3,9)],
        'str_count': [2, 5],
        'col_strs': [['UK', 'US', 'AU'], ['blue', 'black', 'red']]
    },
    ts_cols={
        'count': 2,
        'name': ['start_date', 'end_date'],
        'start_date': ['2020-01-01', '2024-01-01'],
        'end_date': ['2021-01-01', '2025-01-01'],
        'freq': 'QS',
        'random': False,
    },
    int_cols={
        'count': 1,
        'name': ['quantity'],
        'low': [0],
        'high': [100],
        'missing_pct': [0.3],
    },
    float_cols={
        'count': 2,
        'name': ['price', 'charge'],
        'low': [1, 0.1],
        'high': [100, 0.9],
        'missing_pct': [0.3, 0.2],
    },
)
print(d2[:3])
```

Output
```
  country  color start_date   end_date  quantity      price    charge
0      UK  black 2020-01-01 2024-01-01      86.0        NaN  0.657889
1      UK    red 2020-04-01 2024-04-01      36.0  24.294822  0.371457
2      AU  black 2020-07-01 2024-07-01      14.0        NaN  0.113502
```
