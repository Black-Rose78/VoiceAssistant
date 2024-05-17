import openai

class GptResponse:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def get_response(self, input_text):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or "gpt-3.5-turbo" if you are using the GPT-3.5 version choose as you wish
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": input_text}
                ]
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"An error occurred: {e}"

# Usage example:
if __name__ == "__main__":
    api_key = "your_openai_api_key_here"  # Replace with your OpenAI API key
    chat_gpt = GetResponse(api_key)

    input_text = "hey how are you?"
    response = chat_gpt.get_response(input_text)
    print(response)
