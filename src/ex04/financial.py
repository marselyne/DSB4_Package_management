#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup


def get_financial_data(ticker, field):
    url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html",
    }

    try:
        r = requests.get(url, headers=headers, timeout=20)
        text = r.text
    except Exception:
        return "Incorrect URL"

    soup = BeautifulSoup(text, "html.parser")

    tags = soup.find_all(
        "div",
        {
            "class": [
                "rowTitle yf-t22klz",
                "column yf-t22klz alt",
                "column yf-t22klz",
            ]
        },
    )

    if not tags:
        return "Unknown ticker or field"

    texts = [tag.text.strip() for tag in tags]

    result = []
    target = field.strip().lower()

    for i in range(len(texts)):
        if texts[i].strip().lower() == target:
            for j in range(6):
                if i + j < len(texts):
                    result.append(texts[i + j])
            break

    if len(result):
        return tuple(result)

    return "Unknown ticker or field"


def main():
    if len(sys.argv) != 3:
        print("Incorrect number of arguments")
        return 1

    ticker = sys.argv[1]
    field = sys.argv[2]

    try:
        result = get_financial_data(ticker, field)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
