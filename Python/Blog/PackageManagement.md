# How to manage python packages
The package management is actually one of the most challenging part of Python programming.

## pin package version
due to bugs or siginificant changes in new versions

## one pinned version might block many packages to be updated

## worse - there are depedency conflicts

## solution
- temporally pin a package version till the system is broken
- find a workaround for the bug so we can still use the new version

# Best Practices for Pinning Python Dependencies

When building Python applications into docker images, ideally we should always update to the latest version of the packages that we use in the application.
However, in reality there are many issues related to the packages and we are forced to pin some of the packages to a specific version. 
Here based on my work expereience I will discuss the best practices for pinning your Python dependencies - what you should and should not do and how to do it correctly.

## Record all package versions
Consider using a lock file even with pip: Generate a requirements.txt file with specific versions for more control.

## Don't over-pin
Allow some flexibility for minor or patch updates to benefit from bug fixes and security patches.

Specify version ranges (e.g., >=1.2.3,<2.0.0) to allow updates within compatible ranges.

## Regularly review and update pinned versions
Stay current with security patches and bug fixes.

## Avoid major changes if there are issues
New major release usually has many new features and changes - will break your apps
test locally using the new version first 

## Only pinning package versions as a temporal solution
if not workaround, pin it
major versions due to latge changes - update the changes later
need to check the latest version
