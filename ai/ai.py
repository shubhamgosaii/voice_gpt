from openai import OpenAI
from apikey import api_data

prompt = " "

client = OpenAI(api_key=api_data)

def ai(query):
    global prompt
    prompt = f'sir: {query}\n '
    print(prompt)

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # or "gpt-3.5-turbo" if you want old model
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    words = response.choices[0].message.content
    answer = words
    return answer


