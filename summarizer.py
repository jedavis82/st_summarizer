"""
Load up the OpenAI API key and pass a document through the API for summarization
"""

import openai 

class Summarizer: 
    def __init__(self, api_key: str=None): 
        assert api_key is not None, "Must supply a valid path to an API key file"
        # There's no real way to verify the key path is valid without running the model to my knowledge
        openai.api_key = api_key
    
    def summarize_page(self, url: str=None) -> str: 
        """
            Summarize an article from a URL using GPT3
        """
        text_prompt = f'Summarize the text in the following url: {url}\n\nTl;dr'

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text_prompt,
            temperature=0.7,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=1
        )

        summary = response['choices'][0]['text'].replace(':', '', 1).strip()
        return summary
