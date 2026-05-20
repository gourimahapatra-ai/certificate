# OAuth Authentication in Snowflake — SnowPro Core SC0‑03 Study Guide

## 1. What Is OAuth Authentication?
**OAuth** is an industry‑standard authorization protocol that allows applications to access Snowflake **without storing or handling user passwords**.  
Instead of credentials, OAuth uses **access tokens** issued by an **OAuth authorization server**.

Snowflake supports OAuth for:
- External applications  
- BI tools  
- Custom integrations  
- Snowflake‑hosted applications  
- Programmatic access (Python, JDBC, ODBC, etc.)  

OAuth is heavily tested in SnowPro Core because it is a secure, modern alternative to username/password authentication.

---

## 2. OAuth Flow in Snowflake (High‑Level)
1. A user or application requests authorization.  
2. The OAuth provider (IdP or Snowflake) authenticates the user.  
3. The provider issues an **OAuth access token**.  
4. The client presents the token to Snowflake.  
5. Snowflake validates the token and grants access based on:
   - Token scopes  
   - Mapped Snowflake roles  
   - Security integration configuration  

---

## 3. Types of OAuth Supported by Snowflake

### **3.1 External OAuth**
Uses an external Identity Provider (IdP) such as:
- Azure AD  
- Okta  
- Ping Identity  
- Auth0  

External OAuth is used when organizations want centralized identity and SSO.

**Key points:**
- Requires an **EXTERNAL_OAUTH** security integration  
- Roles can be mapped from IdP groups  
- Supports both user and service‑based authentication  

---

### **3.2 Snowflake OAuth**
Snowflake acts as the OAuth authorization server.

Used for:
- Snowflake UI  
- SnowSQL  
- Native Apps  
- Custom applications  

**Key points:**
- Uses **SNOWFLAKE_OAUTH** security integration  
- Supports refresh tokens  
- Supports PKCE for browserless authentication  

---

### **3.3 OAuth for Custom Clients**
Applications can authenticate using:
- Authorization Code Flow  
- Client Credentials Flow (for service accounts)  
- PKCE Flow (for CLI tools and scripts)  

---

## 4. OAuth Scopes (Exam‑Relevant)
Scopes define **what the token is allowed to do**.

Common scopes:
- `session:role:<role_name>` → Assigns a Snowflake role  
- `session:all` → Allows switching roles  
- `refresh_token` → Allows token refresh  
- `user` → Identifies the authenticated user  

**Exam Tip:**  
OAuth tokens **must include a role scope** or Snowflake will assign the **PUBLIC** role.

---

## 5. Security Integrations for OAuth

### **5.1 External OAuth Integration**
```sql
CREATE SECURITY INTEGRATION my_ext_oauth
  TYPE = EXTERNAL_OAUTH
  ENABLED = TRUE
  OAUTH_CLIENT = CUSTOM
  OAUTH_ISSUER = 'https://login.microsoftonline.com/...'
  OAUTH_SCOPE_MAPPING = ( ... );
```

### **5.2 Snowflake OAuth Integration**
```sql
CREATE SECURITY INTEGRATION my_sf_oauth
  TYPE = OAUTH
  ENABLED = TRUE
  OAUTH_CLIENT = 'MY_APP'
  BLOCKED_ROLES_LIST = ('ACCOUNTADMIN');
```

**Exam Tip:**  
OAuth integrations are **account‑level objects** created by administrators.

---

## 6. Role Mapping in OAuth
OAuth tokens can map IdP groups → Snowflake roles.

Example:
```
Azure AD Group: MarketingTeam  
→ Snowflake Role: MARKETING_ROLE
```

Mapping is defined in the security integration.

**Important:**  
If no mapping is provided, Snowflake defaults to the **PUBLIC** role.

---

## 7. OAuth Token Validation
Snowflake validates:
- Token signature  
- Issuer (IdP)  
- Audience  
- Expiration  
- Scopes  

If any validation fails → authentication is rejected.

---

## 8. OAuth vs Other Authentication Methods

| Method | Passwordless | Supports SSO | Best For |
|--------|--------------|--------------|----------|
| OAuth | **Yes** | **Yes** | Apps, BI tools, integrations |
| Key Pair Auth | Yes | No | Automation, service accounts |
| MFA | No | Yes | User login security |
| Federated SSO (SAML) | Yes | Yes | UI login, enterprise SSO |

---

## 9. Common SnowPro Exam Questions

### **Q: Does OAuth require storing passwords?**  
No — OAuth uses tokens, not passwords.

### **Q: Can OAuth assign Snowflake roles?**  
Yes — via scopes or IdP group mapping.

### **Q: What object configures OAuth in Snowflake?**  
A **SECURITY INTEGRATION**.

### **Q: What happens if no role scope is included?**  
Snowflake assigns the **PUBLIC** role.

### **Q: Can OAuth be used for service accounts?**  
Yes — via **Client Credentials Flow**.

---

## 10. Summary
OAuth authentication provides secure, passwordless access to Snowflake using access tokens issued by Snowflake or an external IdP. It supports role mapping, SSO, and modern authentication flows, making it a key topic in the SnowPro Core SC0‑03 exam.

