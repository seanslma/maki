# tip

## remove empty items
  l2 = list(filter(None, l1))

## diff between two lists
  s1 = set(l1).difference(l2)
  
## list of lists to csv
  csv.writer(open('out.csv', 'w', newline='')).writerows(lls)