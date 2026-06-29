# Task 3: AI Web Scraper

## Description

This project is an AI-powered web scraper built using Python, Playwright, BeautifulSoup, and Google Gemini API. It extracts webpage content, identifies emails and phone numbers, and generates an AI summary of the webpage.

## Technologies Used

* Python
* Playwright
* BeautifulSoup4
* Google Gemini API
* Regular Expressions
* Python Dotenv

## Features

* Scrapes static and dynamic websites
* Extracts webpage text
* Detects email addresses
* Detects phone numbers
* Generates AI-powered summaries using Gemini
* Handles JavaScript-rendered pages

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### Create .env file

```text
GEMINI_API_KEY=<gemini_api_key>
```

### Run

```bash
python scraper.py
```

## Input

```text
https://www.python.org
```

## Output Screenshots

<img width="892" height="470" alt="image" src="https://github.com/user-attachments/assets/53748780-1ef8-45e4-aa99-b173b4173398" />
