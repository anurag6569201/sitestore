import requests
from bs4 import BeautifulSoup

def get_metadata(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "No Title"
    description = soup.find("meta", attrs={"name": "description"})
    description = description["content"] if description else "No Description"

    keywords = soup.find("meta", attrs={"name": "keywords"})
    keywords = keywords["content"] if keywords else "No Keywords"

    return {
        "Title": title,
        "Description": description,
        "Keywords": keywords
    }

print(get_metadata("https://google.com"))
