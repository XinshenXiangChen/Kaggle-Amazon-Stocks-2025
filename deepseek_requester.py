from enum import Enum, auto
import OpenAI
import os
import requests
import json

from googleapiclient.discovery_cache import autodetect


class LLMMode(Enum):
    LOCAL = auto()
    CLOUD = auto()


class DeepSeekRequester(object):
    def __init__(self):
        self.prompt = """
        
        """

    def prediction(self):
        answer = self.request()
        prediction = self.interpret_response()


    def request(self, mode):
        if mode == LLMMode.LOCAL:
            self.local_request()
        elif mode == LLMMode.CLOUD:
            self.cloud_request()

    def local_request(self, url="http://localhost:11434/api/chat", mode=LLMMode.CLOUD):
        model_name = "deepseek_model"


        # find the url

        # Get user input for the query

        prompt = self.build_prompt()
        # Define the payload with the user's input
        payload = {
            "model": model_name,  # Replace with the model name you're using
            "messages": [{"role": "user", "content": self.prompt}],
        }

        # Send the HTTP POST request with streaming enabled
        response = requests.post(url, json=payload, stream=True)

        # Check the response status
        if response.status_code == 200:
            for line in response.iter_lines(decode_unicode=True):
                if line:  # Ignore empty lines
                    try:
                        # Parse each line as a JSON object
                        json_data = json.loads(line)
                        # Extract and print the assistant's message content
                        if "message" in json_data and "content" in json_data["message"]:
                            print(json_data["message"]["content"], end="")
                    except json.JSONDecodeError:
                        print(f"\nFailed to parse line: {line}")
            print()  # Ensure the final output ends with a newline
        else:
            print(f"Error: {response.status_code}")
            print(response.text)


    def cloud_request(self):
        client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": self.prompt},
            ],
            stream=False
        )

        return response.choices[0].message.content


    def interpret_response(self, response):
        pass


    def _build_prompt(self):
        return self.prompt