# text

working with text:\\
https://pandas-docs.github.io/pandas-docs-travis/user_guide/text.html


## filter col
```python
df = df[df['tech'].str.contains('|'.join(techs))] #only keep selected techs
```

## regex replace
```python
#replace 'New' or 'new' by 'New_'
df2 = df.replace(to_replace ='[nN]ew', value = 'New_', regex = True) 

#use apply
#remove (*
def clean_names(nam): 
    #search for opening bracket in the name followed by any characters repeated any number of times 
    if re.search('\(.*', nam): 
        pos = re.search('\(.*', nam).start()  #extract the position of beginning of pattern           
        return nam[:pos]  # return the cleaned name 
    else: 
        return nam
df['city'] = df['city'].apply(clean_names) #replace 'city (abc)' by 'city'

txt2 = re.sub(r'(Ave|Rd|Dr)\s+#?\d+\s*\n',r'\1\n', txt, re.MULTILINE|re.IGNORECASE)
```

## re no capturing
**(?:...)**  A non-capturing version of regular parentheses. Matches whatever regular expression is inside the parentheses, but the substring matched by the group cannot be retrieved after performing a match or referenced later in the pattern
```python
msk = np.where(df['id'].str.contains(r'^(?:pie|dog|dinner_[^_]+)_[^_]+_.*',flags=re.IGNORECASE))[0]
```