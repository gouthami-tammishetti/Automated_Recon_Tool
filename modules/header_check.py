import requests

def run_headers(domain):
    try:
        url = f"http://{domain}"
        # We use a 5-second timeout so the tool doesn't hang
        response = requests.get(url, timeout=5, allow_redirects=True)
        headers = response.headers
        
        security_headers = [
            "Content-Security-Policy", 
            "X-Frame-Options", 
            "X-Content-Type-Options", 
            "Strict-Transport-Security",
            "Referrer-Policy"
        ]
        
        results = {
            "server": headers.get("Server", "Unknown"),
            "missing_headers": [h for h in security_headers if h not in headers]
        }
        return results
    except Exception as e:
        return {"error": f"Connection failed: {str(e)}", "missing_headers": []}