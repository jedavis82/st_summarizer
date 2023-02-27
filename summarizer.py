"""
Load up the OpenAI API key and pass a document through the API for summarization
"""

import openai 

class Summarizer: 
    # def __init__(self, api_key: str=None): 
    #     assert api_key is not None, "Must supply a valid API key"
    #     # There's no real way to verify the key path is valid without running the model to my knowledge
    #     openai.api_key = api_key

    def __init__(self):
        # Hard coding this for now to test deployment stuffs. 
        openai.api_key = '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'
    
    def summarize_from_url(self, url: str=None, num_paragraphs: str='one') -> str: 
        """
            Summarize an article from a URL using GPT3
        """
        text_prompt = f'Generate a {num_paragraphs} paragraph summary for the following news article: {url}'
        # text_prompt = f'Summarize the text in the following url: {url}\n\nTl;dr'

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text_prompt,
            temperature=0.7,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=1
        )

        summary = response['choices'][0]['text'].replace(':', '', 1).strip()
        return summary
    
    def summarize_from_text(self, text: str=None, num_paragraphs: str='one') -> str: 
        """
            Summarize a block of text input using GPT3
        """
        text_prompt = f'Generate a {num_paragraphs} paragraph summary for the following text: {text}'

        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=text_prompt,
            temperature=0.7, 
            max_tokens=1000, 
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=1
        )

        summary = response['choices'][0]['text'].replace(':', '', 1).strip()
        return summary 

