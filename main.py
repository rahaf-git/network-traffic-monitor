import scapy.all as scapy
from scapy.layers.http import HTTPRequest
import requests
import datetime
import os

# Directory setup
os.makedirs('logs', exist_ok=True)
os.makedirs('reports', exist_ok=True)

# Function to check if a URL is phishing
def check_phishing(url):
    try:
        response = requests.get(f'https://phishtank.com/check/{url}')
        if 'phishing' in response.text:
            return True
        return False
    except Exception as e:
        print(f'Error checking URL: {e}')
        return False

# Capture HTTP traffic using Scapy
def capture_traffic():
    print('Capturing network traffic...')
    packets = scapy.sniff(filter='tcp port 80 or tcp port 443', count=200)
    return packets

# Log the phishing URL
def log_url(url):
    with open('logs/phishing_log.txt', 'a') as file:
        file.write(f'{datetime.datetime.now()} - {url}\n')
    print(f'Logged phishing URL: {url}')

# Generate an HTML report
def generate_report():
    with open('reports/report.html', 'w') as file:
        file.write('<h2>Phishing URL Report</h2>')
        try:
            with open('logs/phishing_log.txt') as log:
                for line in log:
                    file.write(f'<p>{line}</p>')
        except FileNotFoundError:
            file.write('<p>No phishing URLs detected.</p>')
    print('HTML report generated.')

# Main function to run the monitor
def main():
    print('Starting network traffic monitor...')
    packets = capture_traffic()
    for packet in packets:
        if packet.haslayer(HTTPRequest):
            url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
            if url and check_phishing(url):
                print(f'Phishing URL detected: {url}')
                log_url(url)
    generate_report()
    print('Monitoring complete. Check the reports folder.')

if __name__ == '__main__':
    main()

