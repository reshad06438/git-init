# CLOUDNANO REMEDIATION PLAN
**Operator:** ## TOP 5 CRITICAL FIXES
*(From the 20 raw findings, select the 5 that pose the greatest ACTUAL risk. Explain your reasoning.)*

1. **[Remote Code Execution in Apache Struts]**
   * **Justification:** [This is internet-facing and could let an attackrun commands on the web server.]

2. **[SQL Injection in Login Page]**
   * **Justification:** [This affects the customer databaseportal, so it could expose or change customer data.]

3. **[Unauthenticated AWS S3 Bucket]**
   * **Justification:** [This contains customer PII, so the business impact is very high.]

4. **[SMBv1 Enabled]**
   * **Justification:** [This is on an internal HR file server and could expose sensitive employee files.]

5. **[Cross-Site Scripting (XSS) on Support Forum]**
   * **Justification:** [THis is user-facing and could steal sessions or attack customers and staff.]
