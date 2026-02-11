import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("MeyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjYxOTgzNTc2MiwiYWFpIjoxMSwidWlkIjo5OTcwNjIwMywiaWFkIjoiMjAyNi0wMi0xMVQwNjoyMjoyMy4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MzM3NDgzMzEsInJnbiI6ImFwc2UyIn0.9qApiTy6eZKoAL5URn-DiC4TvJ0Ss8YrodsNot4wv40")

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MONDAY_API_KEY")

WORK_ORDERS_BOARD_ID = "5026563583"

url = "https://api.monday.com/v2"

headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}


def get_work_orders_data():

    query = f"""
    query {{
        boards(ids: {WORK_ORDERS_BOARD_ID}) {{
            items_page(limit: 50) {{
                items {{
                    name
                    column_values {{
                        text
                        column {{
                            title
                        }}
                    }}
                }}
            }}
        }}
    }}
    """

    response = requests.post(url, json={"query": query}, headers=headers)

    # ✅ Convert response to JSON
    data = response.json()

    # ✅ Debug print (you can remove later)
    print("MONDAY RESPONSE:", data)

    # ✅ SAFE ERROR HANDLING
    if "data" not in data:
        raise Exception(f"Monday API Error: {data}")

    boards = data["data"].get("boards", [])

    if not boards:
        raise Exception("No boards data returned from Monday")

    items = boards[0]["items_page"]["items"]

    cleaned_data = []

    for item in items:
        record = {"Project Name": item.get("name", "N/A")}

        for col in item.get("column_values", []):
            title = col["column"]["title"]
            value = col.get("text") or "N/A"
            record[title] = value

        cleaned_data.append(record)

    return cleaned_data
