# Network Traffic Monitor

## Project Description
A Python script to monitor network traffic and detect potential phishing URLs. The script captures HTTP traffic and logs any detected phishing URLs, generating an HTML report.

### Features
- Monitors HTTP traffic using Scapy.
- Detects phishing URLs by checking against PhishTank.
- Generates an HTML report of detected phishing URLs.

## Installation
1. Clone the repository:
git clone https://github.com/yourusername/network-traffic-monitor.git

2. Install dependencies:
pip install -r requirements.txt

3. Run the script:
python main.py

## Project Structure
network-traffic-monitor/ 
logs/
reports/ 
main.py
README.md
requirements.txt

## Dependencies
- scapy
- requests

## License
MIT License

