# Blob

## move files within blob storage based on dates
```ps1
# Set storage account name, container name, destination root folder and number of days to keep old blobs
$accountName = "storage-account-name"
$containerName = "container-name"
$destinationRootFolder = ""
$daysToKeep = 5

# Create a storage context with the given account name
$context = New-AzStorageContext -StorageAccountName $accountName -UseConnectedAccount

# Get all the blobs from the container using the storage context
$blobs = Get-AzStorageBlob -Context $context -Container $containerName

# Loop through each blob.
foreach ($blob in $blobs) {
    # Get the name of the blob
    $blobName = $blob.Name
    
    # Extract the timestamp string from the blob name using a regular expression
    $blobTimestampString = ($blobName -split '[-.]')[1]
    
    # Convert the timestamp string to a datetime object using the specified format
    $blobTimestamp = [datetime]::ParseExact($blobTimestampString, "yyyyMMddHHmmss", $null)
    
    # Calculate the age of the blob in days
    $ageInDays = (Get-Date) - $blobTimestamp

    # Check if the blob is older than the specified number of days
    if ($ageInDays.Days -gt $daysToKeep) {
        # Construct the destination folder path using the year and month from the blob timestamp
        $destinationFolder = Join-Path $destinationRootFolder ($blobTimestamp.ToString("yyyy/MM"))
        
        # Construct the destination blob name by appending the folder path to the original blob name
        $destinationBlobName = Join-Path $destinationFolder $blobName
        
        # Move the blob to the destination using the storage context and output a message
        Write-Output "Moving blob '$blobName' to '$destinationBlobName'"
        Move-AzStorageBlob -Context $context -Container $containerName -Blob $blobName -Destination $destinationBlobName
    }
}
```
