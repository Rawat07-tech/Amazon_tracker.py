import requests
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime

URL = "https://www.amazon.in/dp/B0CHX1W1XY"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

def track_price():
    try:
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")

        # 1. Price dhoondne ke liye multiple koshish
        price_element = soup.find("span", class_="a-price-whole")
        
        if price_element:
            # Sirf digits nikalna (Invalid literal error se bachne ke liye)
            price_raw = price_element.get_text()
            price_text = "".join(filter(str.isdigit, price_raw))
            
            if price_text:
                price = int(price_text)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] 💰 Current Price: ₹{price}")

                # 2. CSV mein save karna
                with open('amazon_prices.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([timestamp, price])
            else:
                print("⚠️ Price text mein numbers nahi mile.")
        else:
            print("❌ Amazon ne block kiya ya price nahi mila (Captcha?)")

    except Exception as e:
        print(f"🚨 Ek error aaya: {e}")

# --- Loop ---
print("🚀 Tracker active hai. Rokne ke liye Ctrl+C dabayein.")
while True:
    track_price()
    # Amazon blocking se bachne ke liye 2 minute ka gap (120 seconds)
    print("⏳ Agla check 2 minute mein...")
    time.sleep(120)
    




