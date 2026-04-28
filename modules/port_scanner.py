import nmap

def run_nmap(target_ip):
    nm = nmap.PortScanner()
    try:
        # Scanning the top 100 most common ports
        # -sV detects service versions (e.g., Apache 2.4.1)
        print(f"    [..] Scanning {target_ip} (this may take a minute)...")
        nm.scan(target_ip, arguments='--top-ports 100 -sV')
        
        scan_results = []
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                ports = nm[host][proto].keys()
                for port in ports:
                    state = nm[host][proto][port]['state']
                    service = nm[host][proto][port]['name']
                    product = nm[host][proto][port].get('product', 'Unknown')
                    scan_results.append({
                        "port": port,
                        "state": state,
                        "service": service,
                        "version": product
                    })
        return scan_results
    except Exception as e:
        return {"error": f"Nmap error: {str(e)}"}