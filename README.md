# Security Header Scanner Command-Line Automation Tool
The Security Header Scanner Command-Line Automation Tool is a Python script that enables you to automate the scanning of security headers in web applications from your Linux terminal. This tool offers a user-friendly interface and saves the scan results in a text file for further analysis.

## Prerequisites
Before using the Security Header Scanner Tool, ensure you have the following prerequisites:

- Python 3: Make sure you have Python 3 installed on your Linux system.

- Dependencies: Install the required Python libraries using the following command:
```bash
pip install requests click
```
## Usage
Download the Script: Download the header_scanner.py script to your Linux system.

- Run the Script: Open a terminal and navigate to the directory where the script is located. Run the script using the following command:
```bash
python3 header_scanner.py
```
- Enter the URL: You will be prompted to enter the URL of the web application you want to scan. For example, enter the URL of the target web application.

- View Results: The script will send an HTTP GET request to the specified URL, extract security headers from the response, and display the results on the terminal.

- Save Results: The scan results, including security headers and their values, will be saved in a text file named header_scan_results.txt in the same directory where the script is located.

## Example
Here's an example of running the script:
```bash
python3 header_scanner.py
```
You will be prompted to enter the URL of the web application you want to scan. After entering the URL, the script will perform the security header scan, display the results in the terminal, and save them in header_scan_results.txt.

# Responsible Use
This tool is intended for legitimate security testing and analysis purposes. Always ensure you have proper authorization before scanning any web application, and use it responsibly and in compliance with applicable laws and regulations.

# Disclaimer
The Security Header Scanner Tool is provided for informational and educational purposes only. Any misuse or unauthorized use of this tool is the sole responsibility of the user. Use it responsibly and within the bounds of the law.

