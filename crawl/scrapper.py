import httpx
from bs4 import BeautifulSoup as bs4

from decimal import Decimal

URL = "http://indonesiaspftware.com/dc_gold2012.php"


async def fetch_kurs() -> str:
    try:
        async with httpx.AsyncClient() as client:
            headers = {
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
                )
            }

            response = await client.get(URL, headers=headers)
            return response.text
    except httpx.RemoteProtocolError as e:
        return ""


async def get_latest_kurs() -> dict:
    content = await fetch_kurs()

    if not content:

        return {
            "dinar": {
                "jual": Decimal(323243.25),
                "beli": Decimal(34.342),
            },
            "dirham": {
                "jual": Decimal(3452.787),
                "beli": Decimal(3432452.6564),
            },
        }

    # 解析爬虫
    soup = bs4(content, "html.parser")
    prices = soup.find_all("td", {"class": "harga"})
    prices = [price.get_text().strip().replace(",", "") for price in prices]

    return {
        "dinar": {
            "jual": Decimal(prices[2]),
            "beli": Decimal(prices[3]),
        },
        "dirham": {
            "jual": Decimal(prices[4]),
            "beli": Decimal(prices[5]),
        },
    }
