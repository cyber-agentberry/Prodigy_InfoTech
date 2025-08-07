## Prodigy Infotech: Task 05 - Packet Sniffer Tool

This project is a command-line tool that captures and analyzes network packets. It was completed as part of the Prodigy Infotech Cybersecurity Internship to provide a hands-on understanding of network protocols and traffic analysis.

## ⚠️ Ethical Considerations

This tool is strictly for educational and authorized purposes only. You should only use it to analyze network traffic on a network you own or have explicit permission to monitor. Unauthorized use is illegal and unethical.

## Project Description

The tool captures network packets and displays key information, including source and destination IP addresses, protocols (TCP, UDP, ICMP), and payload data. The project is built using the Scapy library, a powerful Python tool for packet manipulation.

## How to Run
- Make sure you have Scapy installed:
pip install scapy
- Navigate to the PRODIGY_CS_05 directory.
- Because packet capture requires special permissions, you must run the script with sudo:
sudo python3 sniffer.py
- To generate network traffic, try visiting a website or running a ping command in a separate terminal.
- To stop the sniffer, press Ctrl+C.

## Key Learnings

- Network Protocols: Gained a practical understanding of how network protocols like TCP, UDP, and ICMP are structured and how they function.

- Packet Capture: Learned how to use a specialized library (Scapy) to interact with and analyze low-level network traffic.

- System Permissions: Understood the importance of elevated privileges (sudo) for certain cybersecurity tasks.

- Ethical Hacking: Deepened my appreciation for the ethical responsibilities that come with developing and using network analysis tools.
