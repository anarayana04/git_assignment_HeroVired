import requests
import time
from tabulate import tabulate

def check_subdomain_status(subdomains):
    results = []

    for subdomain in subdomains:
        url = f"http://{subdomain}"
        try:
            response = requests.get(url, timeout=5)
            status = response.status_code
        except requests.ConnectionError:
            status = "Down"
        
        results.append((subdomain, status))

    return results

def display_results(results):
    headers = ["Subdomain", "Status"]
    table = tabulate(results, headers, tablefmt="grid")
    print(table)

def main():
    subdomains = ["awesomeweb", "subdomain2.example.com", "subdomain3.example.com"]

    while True:
        results = check_subdomain_status(subdomains)
        display_results(results)
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
