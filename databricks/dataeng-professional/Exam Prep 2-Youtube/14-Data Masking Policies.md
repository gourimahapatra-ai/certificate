# Data Masking Policies for Sensitive Data

## 1. Protecting Sensitive Information
- Data masking obscures sensitive fields to prevent unauthorized access.
- Ensures that confidential information is not exposed in analytics or shared environments.
- Commonly applied to PII, financial data, and regulated attributes.

## 2. Ensuring Compliance with Regulations
- Supports compliance with GDPR, HIPAA, PCI-DSS, and other data protection standards.
- Helps organizations enforce least‑privilege access and reduce risk.
- Provides auditability and traceability for masked fields.

## 3. Maintaining Data Usability
- Masked data remains useful for testing, development, and analytics.
- Allows teams to work with realistic datasets without exposing real values.
- Techniques include partial masking, tokenization, hashing, and null masking.

## 4. Role-Based Access to Masked Data
- Access to masked or unmasked data is controlled through roles and permissions.
- Unity Catalog policies determine who can see full values vs. masked values.
- Ensures sensitive data is only visible to authorized users.

## 5. Regular Review and Updates
- Masking policies should be reviewed periodically to ensure effectiveness.
- Update rules as new data fields are added or regulations evolve.
- Monitor access logs to detect unauthorized attempts to view sensitive data.

## 6. Summary
Data masking protects sensitive information while maintaining usability for analytics and testing. By enforcing role-based access, ensuring compliance, and regularly updating policies, organizations can safeguard data effectively across their Lakehouse environment.
