import os
from openai import OpenAI, OpenAIError
import requests
from tqdm import tqdm

def generate_images(api_key, prompt, num_images, output_dir):
    client = OpenAI(api_key=api_key)
    image_paths = []
    try:
        for i in tqdm(range(num_images), desc="Generating images"):
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,  # The model requires n=1
            )
            image_url = response.data[0].url
            image_data = requests.get(image_url).content
            image_path = os.path.join(output_dir, f'image_{i}.png')
            with open(image_path, 'wb') as handler:
                handler.write(image_data)
            image_paths.append(image_path)
    except OpenAIError as e:
        print(f"Error: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
    return image_paths
