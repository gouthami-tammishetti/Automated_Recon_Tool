import dns.resolver

def run_dns(domain):
    results = {}
    # Looking for A (IP), MX (Mail), and TXT records
    for r_type in ['A', 'MX', 'TXT']:
        try:
            answers = dns.resolver.resolve(domain, r_type)
            results[r_type] = [str(rdata) for rdata in answers]
        except:
            results[r_type] = []
    return results