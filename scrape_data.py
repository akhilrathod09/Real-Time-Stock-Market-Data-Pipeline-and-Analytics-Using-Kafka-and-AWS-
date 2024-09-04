from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the Yahoo Finance page
driver.get('https://finance.yahoo.com/quote/AAPL/history')

# Wait for the historical prices table to load
table = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//table[@data-test="historical-prices"]'))
)

# Get the page source after the table has loaded
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Find the table with the historical prices
table = soup.find('table', {'data-test': 'historical-prices'})
rows = table.find_all('tr')

# Extract data from the table
data = []
for row in rows[1:]:
    cols = row.find_all('td')
    data.append([col.text.strip() for col in cols])

# Create a DataFrame
df = pd.DataFrame(data, columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])
print(df.head())

# Data cleaning
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df['Open'] = df['Open'].str.replace(',', '').astype(float)
df['High'] = df['High'].str.replace(',', '').astype(float)
df['Low'] = df['Low'].str.replace(',', '').astype(float)
df['Close'] = df['Close'].str.replace(',', '').astype(float)
df['Adj Close'] = df['Adj Close'].str.replace(',', '').astype(float)
df['Volume'] = df['Volume'].str.replace(',', '').astype(int)

# Close the WebDriver
driver.quit()
