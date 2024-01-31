# CSV

## Read CSV in Zip file
```c#
public void ReadCsvInZip(string dirout, string zipfile)
{
    string file = Path.Combine(dirout, Path.GetFileNameWithoutExtension(zipfile) + ".csv");
    using (var sw = new StreamWriter(file)) {
        using (ZipArchive zip = ZipFile.OpenRead(zipfile)) {
            foreach (var entry in zip.Entries) {
                Console.WriteLine($"  {entry.Name}");
                using (var sr = new StreamReader(entry.Open())) {
                    while (sr.Peek() >= 0) {
                        var line = sr.ReadLine();
                        if (line.Length > 0) {
                            sw.WriteLine(line);
                        }
                    }
                }
            }
        }
    }
}
```

## Read specific col in row
```c#
string GetColInRow(string line, int icol)
{
    int i = -1;
    int j = -1;
    int k = -1;
    while (++j < line.Length) {
        switch (line[j]) {
            case ',':
                ++k;
                if (k == icol) {
                    return line.Substring(i + 1, j - i - 1);
                }
                i = j;
                break;
            case '"':
                MoveToEndQuote(ref j, line);
                break;
            default:
                break;
        }
    }
    if (k == icol - 1) {
        return line.Substring(i + 1, j - i - 1);
    }
    return null; //not found
}      

void MoveToEndQuote(ref int j, string line)
{
    while (++j < line.Length) {
        if (line[j] == '"') {
            if (line[j - 1] != '"') {
                if (j + 1 == line.Length) {
                    break;
                }
                else if (line[j + 1] != '"') {
                    break;
                }
            }
        }
    }
}
```
