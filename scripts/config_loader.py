
import json

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def load_topics():
    with open('topics.json', 'r') as file:
        data = json.load(file)
    return data['topics']
