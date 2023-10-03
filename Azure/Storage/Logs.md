# Logs

## download logs
https://learn.microsoft.com/en-us/azure/storage/common/manage-storage-analytics-logs?tabs=azure-portal#download-storage-logging-log-data

## analyze logs
https://learn.microsoft.com/en-us/troubleshoot/azure/azure-storage/troubleshoot-latency-storage-analytics-logs

## why the folder $logs is empty in my azure blob storage account?
If the `$logs` folder in your Azure Blob Storage account is empty, it could be due to several reasons. Here are some common explanations:
- **Logging is Disabled:** By default, logging for Azure Blob Storage is not enabled. If you haven't configured logging for your storage account, no log files will be generated, and the `$logs` container will remain empty.
- **Log Retention Policy:** Even if you have enabled logging, log files may be automatically deleted based on your retention policy settings. Check your storage account's logging settings and retention policy to ensure that logs are being retained for a duration that suits your needs.
- **Log Settings:** It's possible that you have configured logging but with specific filters that are not generating any log entries. Check your logging settings to make sure you are capturing the events and operations you are interested in.
- **Delayed Logging:** Sometimes, it can take a little time for log data to appear in the `$logs` container. Logs may not be generated instantly, and there could be a delay in their availability.
- **Permissions:** Ensure that you have the necessary permissions to access the `$logs` container. If your account doesn't have the correct permissions, you won't be able to see the log files.

To address these issues, you can:
- Verify that logging is enabled for your storage account.
- Check the retention policy settings to ensure logs are kept for an adequate duration.
- Review your logging configuration to ensure it captures the necessary events.
- Wait for some time to see if logs appear with a slight delay.
- Confirm that you have the required permissions to access the `$logs` container.

Additionally, keep in mind that Azure services and configurations may change over time, so it's a good practice to refer to the Azure portal and documentation for the most up-to-date information regarding your Azure Blob Storage account and its logs.
