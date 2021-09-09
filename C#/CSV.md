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
