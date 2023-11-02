# Spreadsheet

## Syncfusion Essential Studio
https://ej2.syncfusion.com/home/

To create a website showing a table like Excel with filters and formats, you can use a C# library such as Syncfusion Essential Studio or Telerik UI for ASP.NET AJAX.

Syncfusion Essential Studio and Telerik UI for ASP.NET AJAX both provide powerful Grid controls that allow you to create Excel-like tables with filters and formats. 
These Grid controls are easy to use and provide a number of features that make them ideal for creating web applications, including:
- **Filtering:** You can allow users to filter the data in the Grid by any column. Filters can be applied using a variety of operators, such as equals, contains, and greater than.
- **Formatting:** You can format the data in the Grid using a variety of options, such as font, color, and alignment. You can also format individual cells or rows.
- **Exporting:** You can allow users to export the data in the Grid to a variety of formats, such as Excel, PDF, and CSV.

To use a C# Grid control to create a website showing a table like Excel with filters and formats, you would follow these steps:
- Add the Syncfusion Essential Studio or Telerik UI for ASP.NET AJAX NuGet package to your project.
- Create a new ASP.NET web application.
- Add a Grid control to your web page.
- Bind the Grid control to the data that you want to display in the table.
- Configure the Grid control's filtering and formatting options.
- Run the web application and you should see a table that looks like Excel with filters and formats.

Here is an example of how to create a website showing a table like Excel with filters and formats using Syncfusion Essential Studio:
```c#
using Syncfusion.JavaScript.Controls.Grid;

public partial class Default : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        // Create a Syncfusion Grid control
        SfGrid grid = new SfGrid();

        // Bind the grid to the data
        grid.DataSource = GetData();

        // Configure the grid's filtering and formatting options
        grid.AllowFiltering = true;
        grid.AllowFormatting = true;

        // Render the grid to HTML
        string htmlTable = grid.Render();

        // Write the HTML table to the response
        Response.Write(htmlTable);
    }

    private DataTable GetData()
    {
        // Create a DataTable
        DataTable dataTable = new DataTable();

        // Add columns to the DataTable
        dataTable.Columns.Add("Name");
        dataTable.Columns.Add("Age");
        dataTable.Columns.Add("Occupation");

        // Add rows to the DataTable
        dataTable.Rows.Add("John Doe", 30, "Software Engineer");
        dataTable.Rows.Add("Jane Doe", 25, "Doctor");
        dataTable.Rows.Add("Peter Parker", 20, "Student");

        return dataTable;
    }
}
```

This code will create a simple website with a table that shows the names, ages, and occupations of three people. 
The table will have filters and formats that allow users to filter the data and format the cells.

You can customize the Grid control to meet your specific needs. For example, you can add more columns to the table, change the order of the columns, 
and add different types of filters and formats. You can also use CSS to style the table.

Syncfusion Essential Studio and Telerik UI for ASP.NET AJAX also provide a number of other components for creating web applications, 
such as charts, menus, and calendars. You can use these components to create a complete and professional web application.
