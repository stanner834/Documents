from openai import OpenAI
client = OpenAI(api_key="")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is Machine Learning?",
        }
    ],
    model="gpt-3.5-turbo",
)

print()
