# Regex

## find a word after another word
  re.compile(r'(?:from|join (\w+)') #word after from or join

## replace empty cell by NaN
```py
df = df.replace(r'^\s*$', np.nan, regex=True).fillna(value=np.nan)
```

## replace special characters
```py
#replace hyphen, en-dash, em-dash by dash
pattern = b'(\xe2\x80\x90|\xe2\x80\x93|\xe2\x80\x94)'
txt2 = re.sub(pattern, b'-', txt.encode('utf-8')).decode('utf-8')
```
