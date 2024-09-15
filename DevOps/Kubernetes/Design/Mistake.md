# common mistakes

https://medium.com/@seifeddinerajhi/most-common-mistakes-to-avoid-when-using-kubernetes-anti-patterns-%EF%B8%8F-f4d37586528d
- resources: cpu, mem
- ignore health check
- avoid using `latest` tag
- overprivileged containers
- lack of monitoring and logging
- default namespace for all objects
- missing security configurations: Authorization, Networking, Storage
- missing poddisruptionbudget: avoid unnecessary service outages due to draining nodes
