import requests
from bs4 import BeautifulSoup

# 1. Product URL (Aap apna pasandida product link yahan daal sakte hain)
URL = "https://www.amazon.in/dp/B0CHX1W1XY" # Example: iPhone 15

# 2. Headers (Google par "my user agent" search karke apna bhi nikal sakte hain)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    # Product Title dhundna
    title = soup.find(id="productTitle").get_text().strip()
    
    # Price dhundna (Amazon par price ki class aksar badalti hai, ye common wali hai)
    price_element = soup.find(class_="a-price-whole")
    
    if price_element:
        price = price_element.get_text().replace(',', '').replace('.', '')
        final_price = int(price)
        
        print(f"Product: {title}")
        print(f"Current Price: ₹{final_price}")

        # Deal Alert Logic
        my_budget = 70000 
        if final_price < my_budget:
            print("🚨 DEAL ALERT! Price aapke budget mein hai! 🚨")
        else:
            print("Abhi mehnga hai, thoda intezar karo.")
    else:
        print("Price nahi mil paya. Amazon block kar raha hai ya class badal gayi hai.")

check_price()

import requests
from bs4 import BeautifulSoup

# URL aur Headers ko functions se bahar rakhein
URL = "https://www.amazon.in/dp/B0CHX1W1XY"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

def check_price():
    try:
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        
        # Baki ka code yahan aayega (ek tab ke gap par)
        print("Function successfully run ho raha hai!")
        
    except Exception as e:
        print(f"Error: {e}")

# Function ko call karna mat bhoolna
check_price()