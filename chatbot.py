import os
from groq import Groq
from dotenv import load_dotenv
from monday_client import get_work_orders_data

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_question(question):

    data = get_work_orders_data()[:10]

    response = client.chat.completions.create(
        model="groq/compound-mini",
        messages=[
            {"role": "system", "content": "You are a business intelligence assistant."},
            {"role": "user", "content": f"Data: {str(data)} Question: {question}"}
        ]
    )

    return response.choices[0].message.content
