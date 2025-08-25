import requests
from bs4 import BeautifulSoup
import csv

# URL for OLX car cover search
url = "https://www.olx.in/items/q-car-cover"

# Set headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

# Fetch page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract item titles and prices
items = []
for listing in soup.find_all("li"):
    title = listing.find("span")
    price = listing.find("span", {"class": "_89yzn"})
    
    if title and price:
        items.append([title.text.strip(), price.text.strip()])

# Save to CSV file
with open("olx_car_cover_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])
    writer.writerows(items)

print("Scraped", len(items), "results. Saved to olx_car_cover_results.csv")
