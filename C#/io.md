# io
if you use **StreamWriter** and **StreamReader** without the **FileStream**, FileStream will be automatically created. But when you created FileStream by yourself, you have options to specify file mode and share access.

## system shutdown
StreamWriter Writing NUL characters at the end of the file when system shutdown abruptly

## write to file
```csharp
const int BufferSize = 65536;  // 64 kB
var writer = new StreamWriter("filename", true, Encoding.UTF8, BufferSize);

using (var writer = new StreamWriter(filepath, true, Encoding.UTF8, 65536)) {
    for (int i = 1; i < repeats; i++) {
        writer.WriteLine("Some line of text");
    }
}
```

## concurrent write and read file
```csharp
var writer = File.Open("C:\\f.txt", FileMode.Create, FileAccess.Write, FileShare.ReadWrite));
var reader = new StreamReader(File.Open("C:\\f.txt", 
                                      FileMode.Open, FileAccess.Read, FileShare.ReadWrite)));
```
