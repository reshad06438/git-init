# TITANCORP: PERIMETER ASSESSMENT REPORT
**Operator:Reshad** **Target Subnet:** 172.88.0.0/24

## PHASE 1: ACTIVE ENUMERATION (NMAP)
*(List the live IPs discovered and their running services/versions)*
* **Host 1 (172.88.0.10):** [http - nginx 1.14.2]
* **Host 2 (172.88.0.15):** [No open ports found in first 1000 scanned ports]
* **Host 3 (172.88.0.20):** [http - Apache httpd 2.4.66 ((Unix))]

## PHASE 2: VULNERABILITY AUDIT (NIKTO)
*(Run Nikto against the TWO web servers discovered above. List one major finding for each.)*
* **Web Server 1 Finding:** [172.88.0.10 is missing the X-Frame-Option header. ]
* **Web Server 2 Finding:** [172.88.0.20 has HTTP TRACE enabled, which suggests XST risk.]

## PHASE 3: RISK TRIAGE
*(Review your findings. Identify the SINGLE highest-risk vulnerability across the entire DMZ. Justify why it is the top priority using the Likelihood x Impact formula.)*

* **Top Priority Remediation:** [Outdated nginx 1.14.2 on 172.88.0.10]
* **Justification:** [This is a public web server using an old nginx version, so it had higher real-world risk than a missing header alone.]
