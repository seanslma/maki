# Landng Zones
https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/

An Azure landing zone is a blueprint that defines a secure and well-architected foundation for deploying your workloads in Microsoft Azure. It's essentially a set of design principles and best practices that help you organize your Azure environment effectively.

## Deployment tools
- For most organizations, Azure Landing Zone Accelerators (portal, Bicep, or Terraform) are the best option due to their ease of use and reduced risk.
- If you have a strong IaC background and require a highly customized landing zone, consider custom IaC templates.
- Manual deployment is generally not recommended due to the complexity and potential for errors.

## Azure landing zone characteristics
* **Multi-subscription Architecture:** It utilizes multiple Azure subscriptions to isolate and manage different aspects of your cloud environment. This helps with organization, security, and access control. There are typically two types of subscriptions:
    * **Platform Landing Zones:** These contain shared services used by various workloads across your organization.
    * **Application Landing Zones:** These are dedicated subscriptions for deploying specific applications or workloads.

* **Scalability and Modularity:** The architecture is designed to be scalable and modular. This means you can easily add new resources or services as your cloud adoption grows, and individual components can be modified to meet specific needs.

* **Security and Governance:**  Security and governance are central principles in an Azure landing zone. The architecture incorporates features like Azure Policy, Role-Based Access Control (RBAC), and Azure Blueprints to enforce security best practices, manage access controls, and ensure compliance with regulations.

* **Standardized Infrastructure:** The landing zone approach promotes a standardized way to deploy and manage your Azure resources. This simplifies operations, reduces the risk of errors, and makes it easier to manage your cloud environment at scale.

## Benefits of using an Azure landing zone
* **Improved Security and Governance:**  By following best practices and enforcing policies, landing zones help you maintain a secure and compliant cloud environment.
* **Simplified Management:** Standardized infrastructure and centralized management tools make it easier to manage and monitor your Azure resources.
* **Scalability and Agility:** The modular design allows you to easily scale your cloud environment and deploy new workloads quickly.
* **Cost Optimization:** Landing zones can help you optimize your cloud costs by promoting efficient resource utilization and avoiding unnecessary configurations.
