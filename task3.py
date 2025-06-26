import requests
from bs4 import BeautifulSoup

# Target news website (change this if needed)
URL = 'https://indianexpress.com/'

# Send HTTP GET request
response = requests.get(URL)
html_content = response.text

# Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <h3> headline tags (depends on the website structure)
headlines = soup.find_all('h3')  # Try 'h2' or 'span' if h3 doesn't work

# Create a list to store extracted headlines
extracted_headlines = []

for idx, headline in enumerate(headlines):
    text = headline.get_text(strip=True)
    if text:
        extracted_headlines.append(f"{idx+1}. {text}")

# Save to a text file
with open("headlines.txt", "w", encoding='utf-8') as f:
    for line in extracted_headlines:
        f.write(line + "\n")

print("✅ Headlines have been saved to headlines.txt")
