from openai import OpenAI
client = OpenAI(api_key="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")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is Machine Learning?",
        }
    ],
    model="gpt-3.5-turbo",
)
