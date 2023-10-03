# Performance

https://learn.microsoft.com/en-us/troubleshoot/azure/azure-storage/troubleshoot-storage-performance

## why sometimes the blob storage read can be more then 10 times slower???
not helpful: https://learn.microsoft.com/en-us/answers/questions/829113/sometimes-download-from-azure-blob-storage-is-very

## metrics
https://learn.microsoft.com/en-gb/azure/storage/common/storage-metrics-migration?WT.mc_id=Portal-Microsoft_Azure_Storage

- `SuccessE2ELatency` and `SuccessServerLatency` metrics show the average time the storage service or API operation type is taking to process requests.
- `SuccessE2ELatency` is a measure of end-to-end latency that includes the time taken to read the request and send the response in addition to the time taken to process the request (therefore, it includes network latency once the request reaches the storage service).
- `SuccessServerLatency` is a measure of just the processing time and therefore excludes any network latency related to communicating with the client.
- `Egress` and `Ingress` metrics show the total amount of data, in bytes, coming in to and going out of your storage service or through a specific API operation type.
- `Transactions` metric shows the total number of requests that the storage service of API operation is receiving. Transactions is the total number of requests the storage service receives.
