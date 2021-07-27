# ssma for mysql

## Timeout for large tables
change batch-size to 1000 and time-out to max value 1440 in default project settings.

## SQL Server does not exist or access denied
To check it:
  - Open SQL Server Configuration Manager from start program.
  - Expand SQL Server Network Configuration
  - Click on Protocols for XXXX
  - Right Click on TCP/IP and open properties
     * Enable TCP/IP
     * Double click TCP?IP, In IP Address Tab, Set Port 1433 in the last option (IPAll)

## Port is not added in the firewall exception list
  - Go to Control Panel -> Open Adminstrative Tool -> Select Windows firewall with Advanced Security
  - From the left panel, click on the Inbound Rules and from right panel select New Rule…
  - In New Inbound Rule Wizard window, select Port and click on Next button
  - In the next tab, enter ‘1433’ in Specific local ports and click on Next button
  - Under What action should be taken when a connection matches the specified condition? section, select Allow the connection option and click on Next
  - Check Domain, Private, Public under which does this rule apply section? and click on Next
  - Enter the Name and click on the Finish button