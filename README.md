# 📰 News Headlines Web Scraper

This is a simple Python-based web scraping project that extracts the top headlines from a news website and saves them into a `.txt` file.

## 📌 Objective

To automate the process of collecting current news headlines from a publicly accessible news website using:

- Python
- `requests`
- `BeautifulSoup`

---

## 🛠 Features

- Fetches HTML content from a news website
- Extracts headline titles (`<h2>` or `<title>` tags)
- Saves the cleaned, formatted headlines into a `headlines.txt` file
- Simple, beginner-friendly CLI application

---

## 🚀 Technologies Used

- Python 3.x
- [requests](https://pypi.org/project/requests/) - for fetching webpage content
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) - for parsing HTML

---

## 💡 How to Run

### 1. Clone this repo or download the Python script

```bash
git clone https://github.com/yourusername/news-headlines-scraper.git
cd news-headlines-scraper
2. Install required packages
bash
pip install requests beautifulsoup4
3. Run the script
bash
python headlines_scraper.py
The top headlines will be saved to a file named headlines.txt.

📁 Output Example
1. PM addresses the nation on latest reforms
2. India wins the series against Australia
3. Tech companies release new AI features

✅ Project Outcome
Gained hands-on experience with web scraping
Learned to parse HTML tags using BeautifulSoup
Practiced saving clean data to .txt files
Applied real-world Python skills in data automation
