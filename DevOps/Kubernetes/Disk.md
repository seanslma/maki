# Disk

## kubernetes node events
```
Type     Reason                Age                     Message
----     ------                ----                    -------
Warning  FreeDiskSpaceFailed   20m (x2195 over 8d)     Failed to garbage collect required amount of images.
                                                       Attempted to free 5852591718 bytes, but only found 1164052028 bytes eligible to free.
Warning  FreeDiskSpaceFailed   10m                     Failed to garbage collect required amount of images.
                                                       Attempted to free 11461842534 bytes, but only found 0 bytes eligible to free.
Warning  EvictionThresholdMet  9m28s (x20 over 7d17h)  Attempting to reclaim ephemeral-storage
```
This is because the node disk is full. 

How to identify which pod used most of the disk?
- if we cannot ssh into the node machine
- we can check the disk usage for each pod one by one `du -sh`
- this might include mounted storage as well
