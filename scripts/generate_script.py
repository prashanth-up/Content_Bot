import os
from openai import OpenAI, OpenAIError
import time

def generate_script(api_key, topic):
    client = OpenAI(api_key=api_key)
    prompt = f"Generate an explanation on the topic: {topic}."
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="gpt-3.5-turbo",
        )
        return response.choices[0].message.content.strip()
    except OpenAIError as e:
        print(f"Error: {e}")
        # Implement retry logic if necessary
        if "rate limit" in str(e).lower():
            print("Waiting for 60 seconds before retrying...")
            time.sleep(60)
            return generate_script(api_key, topic)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
