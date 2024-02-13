# ODBC

##  turbodbc vs pyodbc
Turbodbc and pyodbc are both Python libraries used to interact with relational databases through the Open Database Connectivity (ODBC) interface. 
While they share the same core functionality, they have some key differences:

**Performance:**
- Turbodbc: Generally considered faster, especially for retrieving large datasets. This is primarily due to its use of buffers and NumPy for data type conversions.
- pyodbc: Typically slower than turbodbc, but the exact performance difference can vary depending on the specific scenario and database system.

**Features:**
- Turbodbc: Supports Apache Arrow columnar data format, potentially improving performance for specific use cases. Offers additional features like batching and query optimization.
- pyodbc: More mature and feature-rich library, including support for stored procedures, transactions, and more connection options.

**Ease of Use:**
- Turbodbc: Can have a steeper learning curve due to its more advanced features and focus on performance.
- pyodbc: Generally considered easier to learn and use, with a simpler API and wider documentation.

**Community and Support:**
- Turbodbc: Smaller community and less extensive documentation compared to pyodbc.
- pyodbc: Larger community and more active development, leading to better documentation and support resources.

**Licensing:**
- Turbodbc: Available under both paid and open-source licenses (Apache 2.0).
- pyodbc: Free and open-source (MIT license).
