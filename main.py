import argparse
import json
import os
from jinja2 import Environment, FileSystemLoader

# Importing your custom worker modules
from modules.whois_lookup import run_whois
from modules.dns_enum import run_dns
from modules.port_scanner import run_nmap
from modules.header_check import run_headers

def main():
    parser = argparse.ArgumentParser(description="Automated Recon Tool (ART)")
    parser.add_argument("-d", "--domain", help="Target domain", required=True)
    args = parser.parse_args()

    target = args.domain
    print(f"\n{'='*50}")
    print(f"[*] INITIALIZING RECONNAISSANCE: {target}")
    print(f"{'='*50}\n")

    # Data Collection
    results = {
        "target": target,
        "whois": run_whois(target),
        "dns": run_dns(target),
        "headers": run_headers(target),
        "ports": run_nmap(target)
    }

    # 1. Save Raw JSON Data
    json_filename = f"report_{target.replace('.', '_')}.json"
    with open(json_filename, "w") as f:
        json.dump(results, f, indent=4, default=str)

    # 2. Generate Dark Mode HTML Report
    try:
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('report_template.html')
        html_output = template.render(results)

        html_filename = f"report_{target.replace('.', '_')}.html"
        with open(html_filename, "w") as f:
            f.write(html_output)
            
        print(f"\n[!] RECON COMPLETE")
        print(f"[+] Raw Data: {json_filename}")
        print(f"[+] Web Dashboard: {html_filename}")
        
    except Exception as e:
        print(f"[!] HTML Generation Failed: {e}")

if __name__ == "__main__":
    main()