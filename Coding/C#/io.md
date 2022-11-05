# io
if you use **StreamWriter** and **StreamReader** without the **FileStream**, FileStream will be automatically created. But when you created FileStream by yourself, you have options to specify file mode and share access.

## system shutdown
StreamWriter Writing NUL characters at the end of the file when system shutdown abruptly

## write to file
```c#
const int BufferSize = 65536;  // 64 kB
var writer = new StreamWriter("filename", true, Encoding.UTF8, BufferSize);

using (var writer = new StreamWriter(filepath, true, Encoding.UTF8, 65536)) {
    for (int i = 1; i < repeats; i++) {
        writer.WriteLine("Some line of text");
    }
}
```

## write to zipped csv file
```c#
using(var zf = ZipFile.Open("file.zip", ZipArchiveMode.Create)) {
   var ze = zf.CreateEntry("file.csv");
   using(var zs = ze.Open()) {
      using(var sw = new StreamWriter(zs, Encoding.UTF8)) {
         sw.WriteLine("Name,Address,Email")
      }
   }
}
```

## concurrent write and read file
```c#
var writer = File.Open("C:\\f.txt", FileMode.Create, FileAccess.Write, FileShare.ReadWrite));
var reader = new StreamReader(File.Open("C:\\f.txt", 
                                      FileMode.Open, FileAccess.Read, FileShare.ReadWrite)));
```

## append to log file
```c#
public static void ToFile(string msg, bool writeline = false)
{
    using (var w = File.AppendText(_logpath)) {
        if (!writeline) {
            w.Write(msg);
        }
        else {
            w.WriteLine(msg);
        }
    }
}
```

## color console
```c#
public static void ConsoleColorWLine(string msg, ConsoleColor? fgc = null, ConsoleColor? bgc = null)
{
    ConsoleColorWrite($"{msg}\n", fgc, bgc);
}

public static void ConsoleColorWrite(string msg, ConsoleColor? fgc = null, ConsoleColor? bgc = null)
{
    var fgColor = Console.ForegroundColor;
    if (fgc.HasValue) {
        Console.ForegroundColor = fgc.Value;
    }
    var bgColor = Console.BackgroundColor;
    if (bgc.HasValue) {
        Console.BackgroundColor = bgc.Value;
    }
    Console.Write(msg);
    if (fgc.HasValue) {
        Console.ForegroundColor = fgColor;
    }
    if (bgc.HasValue) {
        Console.BackgroundColor = bgColor;
    }
}
```
