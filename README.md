## Professional Introduction

My name is Reshad Hasnat, and I am currently pursuing a bachelor degree in Information Systems. I join the knowledge house on cybersecurity track to grow my technical skills. I am developing foundational skills in networking, system configuration, and secure infrastructure management. Through hands-on lab environments and virtual machine configuration, I am building practical experience in secure system deployment. My goal is to strengthen my understanding of defensive security practices and network protection strategies.

## Cybersecurity Focus

My primary area of interest is network security and infrastructure protection. I am focused on learning how to configure secure virtual environments, isolate systems using host-only networking, and analyze connectivity between devices. I am particularly interested in understanding how secure configurations prevent vulnerabilities and unauthorized access within enterprise networks.

## References

Oracle Corporation. (n.d.). *Oracle VM VirtualBox documentation*. https://www.virtualbox.org/wiki/Documentation

## Lab Infrastructure & Virtualization Setup

A hypervisor is software that allows multiple operating systems to run on a single physical machine by managing hardware resources between virtual environments. Examples include VirtualBox and VMware.

A virtual machine (VM) is a software-based computer that runs its own operating system and applications while sharing the physical resources of the host system. Each VM operates independently from the host and other virtual machines.

Isolation is critical in cybersecurity because it prevents malicious code or misconfigurations from affecting the host system or other environments. By isolating systems, security professionals can safely test software, analyze malware, and experiment with configurations without risking real infrastructure.

Virtualization directly supports the principles of Confidentiality, Integrity, and Availability (CIA). Confidentiality is maintained by separating systems and limiting unauthorized access between environments. Integrity is preserved because isolated environments prevent unintended modifications to critical systems. Availability is enhanced by allowing systems to be restored quickly through snapshots and backups.

## References

National Institute of Standards and Technology. (2023). *Security and privacy controls for information systems and organizations (SP 800-53 Rev. 5)*. https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final

## Reflection

Isolation is important when testing software or malware because it prevents harmful code from spreading to the host system or network. Virtualization supports secure experimentation by allowing environments to be created, modified, and deleted without impacting real systems. Snapshots and rollback features make it possible to test configurations safely and recover quickly from errors. Today’s material aligns most closely with the Network and Infrastructure security domain, as it focuses on system isolation and controlled connectivity. Understanding virtualization strengthens defensive security practices and safe lab experimentation.

## Security Philosophy
 
My lab environment uses virtualization through Oracle VirtualBox to create an isolated Linux virtual machine. Virtualization improves security by separating the guest operating system from the host system, which helps protect sensitive data and prevents unauthorized access (National Institute of Standards and Technology [NIST], 2011). This isolation supports confidentiality because only authorized users and processes inside the virtual machine can access its data. Integrity is maintained by verifying installed tools such as Git and Python using the lab_verify.sh script and by using version control to prevent unauthorized or accidental modifications. These security practices align with established federal information system security controls (NIST, 2020). Availability is ensured because the virtual machine can be started, stopped, and restored when needed without affecting the host system, allowing continuous and reliable access to the lab environment.

## Reference

NIST. (2020). Security and privacy controls for information systems and organizations (SP 800-53 Rev. 5). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-53r5

NIST. (2011). Guide to security for full virtualization technologies (SP 800-125). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-125