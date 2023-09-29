# Add

## ADD failed: Forbidden path outside the build context
This error occurs because the path you're trying to add with the ADD instruction is located outside the Docker build context. 
Docker restricts file operations to within the build context directory for security reasons.

To resolve this issue, we need to copy the folder to under the build contect directory.
