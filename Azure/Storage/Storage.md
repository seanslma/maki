# Storage

## Storage types
- Azure Blob storage:
  - for unstructured data such as documents, image
- Azure File storage:
  - shared storage based on the SMB protocol, can be mounted as networkdrive
  - accessible by pods on multiple nodes simultaneously
- Azure Disk Storage:
  - block-level storage for Azure Virtual Machines
  - mounted as ReadWriteOnce, only available to a single node
- Azure Table storage: NoSQL key-attribute data store for structured data
- Azure Queue storage: for storing large numbers of messages, message can be up to 64 KB in size

## Message queue
Azure Service Bus
- provides support for 256 KB messages
- can store messages for an unlimited period
- higher cost and latency

Azure Queue storage 
- provides support for 64 KB messages
- can store messages for 7 days
