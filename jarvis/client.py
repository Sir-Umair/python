from openai import OpenAI

client = OpenAI(api_key="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")

response = client.chat.completions.create(
    model="gpt-4o",  # Updated model name
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please."},
        {"role": "user", "content": "Hello Jarvis, can you open Google, YouTube, or GitHub? Also, play some music from my library or fetch the latest news for me."}
    ]
)

print(response.choices[0].message.content)
