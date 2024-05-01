# Json

## save dict to json
```py
# to json strong
json_str = json.dumps(data)
# to json file
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
```

## load json to dict
```py
# json string to dict
json.loads(json_str)
# json file to dict
with open('data.json', 'r') as inputfile:
    data = json.load(inputfile)
```
