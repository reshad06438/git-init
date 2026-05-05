# TARGET THREAT PROFILE: CloudNano 
**Classification:** Passive Security Audit
** Target Proxy Domain** tesla.com
**Operator:** Reshad  
* **Tool Used:** Shodan, Sublist3r, BuiltWith/Wappalyzer, HaveIBeenPwned

## 1. Subdomain Discovery 
* **Tool used:** Sublist3r
* **Command Used:** 
  'sublist3r -d tesla.com'

* **Subdomains Found:**
  * www.tesla.com
  *shop.tesla.com
* ** Why this matters:**
Subdomains help map the target's public attack surface because each subdomain
may reveal login portals, web applications, exposed services, or misconfigured
systems.

## 2. Tech Stack Mapping 
* **Tool Used:** BuiltWith / Wappalyzer
* **Identified Technologies (CMS/CDN/Backend):** * [Akami - found using BuiltWIth/ Wappalyzer] 
  * [Google Analytics - found using BuiltWith/Wappalyzer] 

## 3. Major Exposure Points & Dangers 
*(List three major exposure points discovered during your OSINT audit and explain why they are dangerous)*
1. **[Geographic Shodan Results]:** [Shodan showed many publicly indexed internet-
facing devices in ALlentown, which is dangerous because attackers can narrow their search to exposed system in a specific city or organization area.] 
2. **[Public Remote Dekstop Protocol]:** [Shodan showed Remote Desktop Protocol services publicly visible on port 3389, which is dangerous because attackers 
often target RDP for password guessing, stolen credentials, and unauthorized remote access.] 
3. **[Public FTP Banner Exposure]:** [Shodan showed FTP banner information exposing server software and version details, which is dangerous because attackers can use exact version numbers to search for known vulnerabilities.] 
