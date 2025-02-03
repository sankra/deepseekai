from openai import OpenAI

client = OpenAI(api_key="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",
                base_url="https://openrouter.ai/api/v1")

chat = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=[
        {
            "role":"user",
            "content":"what are the uses of Python Django Framework"
        }
    ]
)

print(chat.choices[0].message.content)