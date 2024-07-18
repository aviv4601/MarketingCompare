import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = 'https://digitalinvoice.shufersal.co.il/?e=0&t=CaUG0nmt6eZJ4VQT1DFIOQ2'  # Replace with the actual URL
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all elements with the class 'invoice-product-number'
elements = soup.find_all(class_='invoice-product-number')

# Step 4: Extract and print the text
for element in elements:
    print(element.get_text(strip=True))
