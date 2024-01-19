# Reference Table

The term "reference table" in Power BI can have two different meanings depending on the context:

**1. Referencing a Query (Power Query):**

In Power Query, a reference table is not actually a separate table itself, but rather a way to **reuse the steps of another query** within your current query. Imagine you have two queries:

* **Query1:** Extracts data from a specific source and performs some transformations.
* **Query2:** Needs the transformed data from Query1, but also wants to do some additional calculations.

Here, you can create a reference to Query1 within Query2. This means Query2 will execute the steps of Query1 first, then apply its own additional steps to the resulting data. This eliminates the need to duplicate the steps of Query1, making your queries more efficient and organized.

**2. Dimension Table in Data Model:**

In the Power BI data model, a reference table can refer to a **dimension table** that serves as a source of information for one or more fact tables. Dimension tables typically hold static data like customer names, product categories, or dates. Instead of storing the same information repeatedly in each fact table, you can create a reference to the dimension table to avoid data redundancy and improve performance.

Therefore, understanding the context of which type of reference table you're encountering is crucial to interpret its function accurately.

Here are some additional points to consider:

* **Performance:** Referencing queries can improve performance if used strategically, as it eliminates redundant data retrieval. However, overuse can also backfire if the referenced query has slow execution times.
* **Maintainability:** Using reference tables in the data model promotes better data organization and maintainability, as changes to the dimension table will automatically be reflected in all connected fact tables.
* **Clarity:** Always name your reference tables clearly to avoid confusion and ensure easy understanding of your data model.

I hope this explanation clarifies the concept of reference tables in Power BI. If you have any further questions about specific scenarios or need more details, feel free to ask!
