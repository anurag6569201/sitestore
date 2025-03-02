import requests

API_KEY = "AIzaSyD3TPf_4xRIIscdUmL2sFJJrI5mJD4HSIA"  # Replace with your API Key


def get_performance(url):
    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={API_KEY}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        lighthouse = data['lighthouseResult']['categories']['performance']['score'] * 100

        metrics = data['lighthouseResult']['audits']
        fcp = metrics['first-contentful-paint']['displayValue']
        lcp = metrics['largest-contentful-paint']['displayValue']
        cls = metrics['cumulative-layout-shift']['displayValue']
        tti = metrics['interactive']['displayValue']
        speed_index = metrics['speed-index']['displayValue']
        
        return (
            f"Performance Score: {lighthouse}\n"
            f"First Contentful Paint (FCP): {fcp}\n"
            f"Largest Contentful Paint (LCP): {lcp}\n"
            f"Cumulative Layout Shift (CLS): {cls}\n"
            f"Time to Interactive (TTI): {tti}\n"
            f"Speed Index: {speed_index}"
        )
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example Usage
website = "https://github.com"
print(get_performance(website))
