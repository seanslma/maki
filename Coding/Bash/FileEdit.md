# File Edit

## merge and grep files to new file
```sh
cat ./*.txt | grep 'my-test-name' > test.txt
```
## merge two yml files
```sh
cat file1.yml <(echo "---") file2.yml > merged.yml
```
