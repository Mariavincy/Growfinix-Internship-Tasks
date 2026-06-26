import requests
from bs4 import BeautifulSoup
import re
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Input URL
url = input("Enter website URL: ")

# Download webpage
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    html = page.content()
    browser.close()

soup = BeautifulSoup(html, "html.parser")

# Extract text
text_content = soup.get_text(separator=" ", strip=True)

# Extract emails
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text_content)

# Extract phone numbers
phones = re.findall(
    r'(?:\+91[- ]?)?[6-9]\d{9}|0\d{2,4}[- ]?\d{6,8}',
    text_content
)

# Prompt for Gemini
prompt = f"""
Extract the following information from this webpage:

1. Company Name
2. Price Information
3. Short Summary

Content:
{text_content[:15000]}
"""

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    print("\n===== AI Output =====")
    print(response.text)

except Exception as e:
    print("\nGemini Error:")
    print(e)

print("\n===== Emails Found =====")
print(emails if emails else "No emails found")

print("\n===== Phone Numbers Found =====")
print(phones if phones else "No phone numbers found")