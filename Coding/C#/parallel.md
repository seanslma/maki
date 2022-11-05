```c#
using System.Threading.Tasks;
Parallel.For(0, lst.Count, idx => {
    MyFunc(par1, par2, lst[idx]);
});
```
