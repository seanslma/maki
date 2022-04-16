# to

## list of tuples
  list(df.itertuples(index=False, name=None))
  
## check type count in col
  df['col1'].apply(lambda x: type(x)).value_counts()
  df['col1'][df['col1'].apply(lambda x: isinstance(x,str))]
  df['col1'].dt.year.value_counts().sort_index()
  
## dict of list
  df.groupby('key')['val'].apply(list).to_dict()
  df.groupby('key')[['va1','va2']].apply(lambda g: g.values.tolist()).to_dict()