# db connection

## encrypt connection string
- Ensure in the datbase server the `encryption` is enabled
- In the connection string add `;encrypt=yes;trustservercertificate=no`

When connecting to MS SQL Server with Python and pyodbc, 
the `encrypt=yes` parameter is not a standalone encryption mechanism. 
It works in conjunction with TLS/SSL to enforce encrypted communication between the client and server.

1. **TLS/SSL Configuration:**
   - The `encrypt=yes` parameter is typically used in conjunction with other TLS/SSL-related parameters in the connection string,
     such as `sslmode`, `sslkey`, `sslcert`, and `sslrootcert`.
     These parameters specify the keys and certificates required for secure communication.
2. **Client-Server Negotiation:**
   - When the connection attempt is made with `encrypt=yes`, the driver initiates a TLS/SSL handshake with the MS SQL Server.
   - The server presents its SSL certificate, which is verified by the client against a trusted root certificate authority (CA).
   - If the server certificate is valid, a secure encrypted communication channel is established using symmetric encryption algorithms.
3. **Data Encryption:**
   - All data transmitted between the client and server, including the connection string itself, is encrypted using the established TLS/SSL channel.
   - This prevents sensitive information, such as login credentials and database queries, from being intercepted or read in plain text.

**Important Considerations:**
- **TrustServerCertificate**
   - While you can use `TrustServerCertificate=YES` to bypass server certificate verification,
     this is **strongly discouraged in production environments** due to security risks.
     Always validate server certificates against trusted CAs.
- **Best Practices**
   - Always use valid SSL certificates issued by trusted CAs.
   - Ensure proper configuration of TLS/SSL settings on both client and server sides.
   - Stay updated with the latest driver versions and security patches.
