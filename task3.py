import requests
from bs4 import BeautifulSoup

# Step 1: Get the page content
url = "https://indianexpress.com/"
response = requests.get(url)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find all headline tags
headlines = soup.find_all('h3')  # usually news headlines are in <h3> tags

# Step 4: Print and save them
with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in headlines:
        text = headline.get_text(strip=True)
        print(text)
        file.write(text + "\n")
