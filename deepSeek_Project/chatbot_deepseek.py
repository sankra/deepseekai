from openai import OpenAI

client = OpenAI(api_key=" ",
                base_url="https://openrouter.ai/api/v1")
#api_key has been removed.
question = 0

while True:
    question += 1
    if question == 1:
        print("Welcome to OpenAI ChatBot")
        print("Question 1:")
    else:
        print(f'Question {question}',end='')
    prompt = input()

    if prompt.lower() in ["exit", "quit"]:
        print("Exiting ChatBot. Goodbye!")
        break

    chat = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
            {
                "role":"user2",
                "content":prompt,
            }
        ]
    )
    print(chat.choices[0].message.content)
