import requests
import click

# Output file to save results
OUTPUT_FILE = 'header_scan_results.txt'

# Define a command-line interface using Click
@click.command()
@click.option('--url', prompt='Enter the URL to scan', help='The URL of the web application')
def main(url):
    try:
        # Send an HTTP GET request to the specified URL
        response = requests.get(url)

        # Extract security headers from the response
        security_headers = {
            'Strict-Transport-Security': response.headers.get('Strict-Transport-Security', 'Not Found'),
            'X-Content-Type-Options': response.headers.get('X-Content-Type-Options', 'Not Found'),
            'X-Frame-Options': response.headers.get('X-Frame-Options', 'Not Found'),
            'X-XSS-Protection': response.headers.get('X-XSS-Protection', 'Not Found'),
            'Content-Security-Policy': response.headers.get('Content-Security-Policy', 'Not Found')
        }

        # Save the results to a text file
        with open(OUTPUT_FILE, 'w') as file:
            for header, value in security_headers.items():
                file.write(f"{header}: {value}\n")

        click.echo(f"Security headers scanned and results saved to {OUTPUT_FILE}")

    except requests.exceptions.RequestException as e:
        click.echo(f"Request Error: {e}")
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
