from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Set up Chrome options for headless mode
s = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')  # Required for headless mode on certain platforms

# Set up Selenium WebDriver with Chrome
driver = webdriver.Chrome(service=s,options=chrome_options)

# Replace 'https://example.com' with your target URL
url = 'https://www.realtor.com/realestateandhomes-detail/M2953304470'

# Navigate to the URL
driver.get(url)

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extract text from the first h1 tag
h1_text = soup.find('h1').text

# Print the extracted text
print(f'Text of the first h1 tag: {h1_text}')

# Close the WebDriver
driver.quit()
