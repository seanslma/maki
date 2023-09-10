# Security

## category
- storage security: data encryption, client-side encryption, key-vault
- network security: vpn, network security groups
- identity/access control: rbac, multi-factor authentication, password policies
- monitoring processes: storage analytics and security logs

## Ensure azure container app is not accecible from public internet
To avoid deploying an Azure Container App to the public internet, you can implement various security measures and configurations to restrict access to your container app. Here's a general outline of steps you can take:
- **Disable Public Endpoints:** Make sure that you haven't configured any public endpoints or exposed unnecessary ports that could potentially lead to public internet access.
- **Use Private Endpoints:** Azure Private Link allows you to access services privately over an Azure Virtual Network. You can create a private endpoint for your Azure Container App, which will enable you to connect to the container app over a private IP address from within your virtual network, rather than over the public internet.
- **Network Security Groups (NSGs):** Use NSGs to control inbound and outbound traffic to your container app. Configure NSGs to allow traffic only from specific IP ranges or virtual networks that need access, and deny all other traffic.
- **Firewalls:** Utilize Azure Firewall or third-party firewalls to control and filter traffic to and from your container app. Configure rules to allow only necessary traffic while blocking everything else.
- **Service Tags:** Azure provides service tags for various Azure services, including Azure Container Registry and Azure Storage. You can configure NSG rules to allow traffic only from these service tags, ensuring that your container app can interact with these services securely.
-  **VNet Integration:** If your container app needs to access other Azure services, you can integrate your virtual network with those services using Azure VNet Integration. This will allow your app to communicate privately with those services without exposing them to the public internet.
- **Authentication and Authorization:** Implement strong authentication mechanisms for your container app. Use Azure Active Directory (AAD) or other identity providers to manage access. Additionally, implement role-based access control (RBAC) to restrict access to specific users or roles.
- **SSL/TLS Encryption:** If your container app serves content over HTTPS, use SSL/TLS certificates to encrypt communication between clients and the app. This ensures data confidentiality and integrity.
- **Monitoring and Logging:** Implement robust monitoring and logging to detect any unauthorized access attempts or unusual activities. Azure Monitor and Azure Security Center can help you with this.
- **Regular Updates and Security Patches:** Keep your container app and its underlying components up to date with the latest security patches to prevent vulnerabilities that could be exploited.
- **Penetration Testing:** Conduct regular penetration testing to identify potential security weaknesses in your setup and address them before they can be exploited.
