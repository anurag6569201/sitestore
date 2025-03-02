import whois

def get_domain_info(domain):
    try:
        domain_info = whois.whois(domain)
        return {
            "Domain Name": domain_info.domain_name,
            "Registrar": domain_info.registrar,
            "Whois Server": domain_info.whois_server,
            "Creation Date": domain_info.creation_date,
            "Expiration Date": domain_info.expiration_date,
            "Updated Date": domain_info.updated_date,
            "Status": domain_info.status,
            "Name Servers": domain_info.name_servers,
            "Owner": domain_info.org,
            "Country": domain_info.country,
            "Emails": domain_info.emails
        }
    except Exception as e:
        return {"Error": str(e)}

# Example Usage
domain = "anurag.icu"
info = get_domain_info(domain)
for key, value in info.items():
    print(f"{key}: {value}")
