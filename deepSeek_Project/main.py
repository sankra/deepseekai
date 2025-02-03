from openai import OpenAI

client = OpenAI(api_key="",
                base_url="https://openrouter.ai/api/v1")
#Give your api key in the blank.

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
