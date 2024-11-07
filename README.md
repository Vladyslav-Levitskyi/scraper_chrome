# Automated Web Scraper with Chromedriver

This project is an automated web scraper based on Selenium with the `chromedriver.exe` driver. It consists of two main scripts: `searcher_se.py` for login automation and saving HTML page templates, and `scraper_bs.py` for local data parsing.

## Overview

1. **File `searcher_se.py`**:
   - Automates website login.
   - Navigates to the desired section of the site.
   - Saves HTML templates for a specified range of pages.
   - This reduces server load as the pages are downloaded locally.

2. **File `scraper_bs.py`**:
   - Parses the saved HTML templates on the local machine.
   - This method is effective for obtaining data from obfuscated or protected pages, as it doesn’t generate many requests to the server.

This approach is particularly useful when data is protected or challenging to extract with standard HTTP requests.

## Project Components

### `searcher_se.py`
- **Purpose**: Automates login and navigation on the website.
- **Capabilities**:
  - Logs in using Selenium.
  - Can navigate to specific pages and download HTML templates for local storage.

### `scraper_bs.py`
- **Purpose**: Parses locally saved HTML templates using BeautifulSoup.
- **Output**: After parsing, data can be saved in a convenient format, such as JSON.

## Requirements

- **Python 3.x**
- **Selenium** and **BeautifulSoup**
- **Chromedriver**: Ensure that `chromedriver.exe` is either in the project directory or specified in your PATH.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   Download the appropriate version of chromedriver.exe for your browser and place it in the project directory or ensure it is in your PATH.

## Usage

Run searcher_se.py to automate site login and save HTML pages:

python searcher_se.py

This script will save HTML page templates for later parsing.

Run scraper_bs.py to parse saved HTML templates on your local machine:

python scraper_bs.py

## Benefits

Minimized server load: Storing HTML locally helps avoid excessive requests to the server.
Ideal for protected data: Saved HTML files simplify data extraction, even for obfuscated or protected content on the server.

## License

MIT
## Copyright

(c) 11-2024 Vladyslav Levytskyi