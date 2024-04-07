from dotenv import load_dotenv
import os

from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# runs the program using openAI api_key from www.platform.openai.com.
# gpt-3.5-turbo - is the newest and cheapest gpt model


def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user",
                   "content": prompt, }],
        # max_tokens=10
    )

    return response.choices[0].message.content.strip()


# run program
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break

        response = chat_with_gpt(user_input)
        print("ChatBot says:", response)
