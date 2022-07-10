# Package

## attempted relative import with no known parent package
```
from ..utils import check_date
```
The previous line will crash with the error if run the code from a subfolder and import the methods from the parent folder. In this case, function call must be from the parent folder.
