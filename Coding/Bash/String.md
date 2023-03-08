# String

## Quotes or not
Quote it if it can
- be empty
- contain spaces (or any whitespace)
- contain special characters (wildcards)
- not require word splitting and wildcard expansion

Not quoting strings with spaces
- often leads to the shell breaking apart a single argument into many

### Single quotes
Single quotes protect the text between them verbatim.
- want to suppress interpolation and special treatment of backslashes

### Double quotes
Double quotes are suitable when variable interpolation is required or single quotes are required in the string.
- want to suppress word splitting and globbing
- ant the literal to be treated as a string, not a regex

## Process logs to csv
```sh
# extract log info to csv
log_file="$1.log"
csv_file="$1.csv"

# write csv header
echo "ts,dept,type,value" > $csv_file

# extract the desired columns from each row of the log file
cat $log_file | while read line; do
    text=$(echo "$line" | cut -d "|" -f 1,7)                               #get columns 1 and 7
    ts=$(echo "$text" | cut -d "|" -f 1 | awk '{$1=$1};1' | sed "s/,/./g") #remove space and replace , by .
    dept=$(echo "$text" | grep -oP '(?<=\[)[^\]]+' | head -1)              #get dept in [dept]
    last_col=$(echo "$text" | rev | cut -d "]" -f 1 | rev)                 #get last col
    if [[ $last_col == *"Dept started"* ]]; then                           #is dept row
        typ="task"                                                         #get string after 'Dept: '
        val=\"$(echo "$last_col" | grep -oP '(?<=Dept: ).*' | head -1 | sed "s/\"/'/g")\"
    elif [[ $last_col == *"Finished getting"* ]]; then                     #get string between two strings
        typ=\"$(echo "$last_col" | grep -oP '(?<=Finished getting ).*(?= in)' | head -1)\"
        val=$(echo "$last_col" | grep -oP '(?<=in ).*(?= seconds.)' | head -1)
    else
        continue
    fi
    echo "$ts,$dept,$typ,$val" >> $csv_file
done
```
