# VM
https://learn.microsoft.com/en-us/azure/virtual-machines/dedicated-host-memory-optimized-skus

https://www.cbtnuggets.com/blog/certifications/microsoft/how-to-choose-the-best-virtual-machine-for-your-workload-in-azure

## pricing
https://azure.microsoft.com/en-ca/pricing/details/virtual-machines/linux/

## vm cpu quota
https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quotas

Subscription > Settings > Usage + quotas
```
az vm list-usage --location "australiaeast" -o table
```

## how to select the VM series
- D-Series: CRM systems, more extensive databases, web-servers with medium web traffic, small production apps, desktop virtualization, e-commerce applications, enterprise-level applications
- E-Series: SAP Hana, Netweaver, large databases, data warehousing, BI apps, analytical apps, apps that perform heavy processing like financial or weather apps, apps that require heavy in-memory use
