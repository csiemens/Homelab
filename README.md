# Homelab Projects

This repository contains hands-on security simulations performed to strengthen my understanding of detection engineering, log analysis, and incident response.

---

## Network Architecture

All systems are virtualized using VirtualBox and connected through an isolated internal network.

### Lab Systems

- Kali Linux (Attacker) – 192.168.20.10
- Windows 11 Pro (Target) – 192.168.20.12
  - Splunk Enterprise
  - Sysmon
  - Splunk Universal Forwarder

Windows Security and Sysmon logs are forwarded to Splunk for centralized monitoring.

---

## Brute Force Attack – RDP Detection in Splunk

### Objective

Simulate an RDP brute-force attack from Kali Linux against a Windows 11 machine and develop detection logic in Splunk to identify excessive failed authentication attempts (`Event ID 4625`).

### Outcome

Successfully simulated an RDP brute-force attack from the attacker machine. Multiple failed logon events (Event ID 4625) were detected, with no corresponding successful logon events (Event ID 4624). The attack did not result in unauthorized access.

[Brute_Force_RDP_Report](./Brute_Force_RDP_Report.pdf)

---

## Wireshark Packet Captures

>**Note:** NAT and DHCP were used on Windows 11 for the Wireshark lab, allowing the VM to access external websites and capture real-world traffic.

### Objective

To capture and analyze network traffic using Wireshark, including ICMP, DNS, TCP handshakes, and HTTP requests, in order to better understand network protocol behavior and associated security implications.

### Outcome

Successfully captured and analyzed network traffic packets using Wireshark, learning about protocols such as ICMP, DNS, TCP connection establishment, and HTTP request/response behavior.

[Wireshark_Report](./Wireshark.pdf)
