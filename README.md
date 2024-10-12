
# Review Extraction API

This project implements a Review Extraction API that dynamically scrapes product reviews from any given product page, like Flipkart and Amazon etc. The API identifies dynamic CSS selectors for reviews using OpenAI’s Large Language Model (LLM), interacts with the webpage via Selenium and Firefox browser automation, and handles pagination to retrieve all reviews. The extracted reviews are returned in a JSON format.

## Features

- Dynamic Review Scraping: Uses OpenAI's GPT model to dynamically identify the relevant CSS selectors for reviews on any product page.
- Browser Automation: Selenium with Firefox browser is employed to simulate browser activity and interact with the product pages.
- Pagination Handling: Automatically detects and handles pagination to extract reviews from all pages.
- Universal Compatibility: Works with any product page with reviews and ensures extraction of titles, body text, ratings, and reviewer names


## Installation

Install my-project with npm

```bash
 git clone https://github.com/Er-Sadiq/DynamicCascadingStyleSheets-Scraper-Flask-API.git
cd review-extraction-api
```

```bash
 python3 -m venv venv
source venv/bin/activate
$ pip install Flask selenium openai
```

```bash
export OPENAI_API_KEY="your-api-key-here"
flask run / App.py
```


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Tech Stack 

- Programming Language: Python
- Web Framework: Flask
- Browser Automation: Selenium with Firefox
- LLM Integration: OpenAI GPT

For any questions or issues, feel free to contact:

📧 sadiqkhan.2503@gmail.com
