import streamlit as st 
from io import StringIO 
import validators 

from summarizer import Summarizer

model = None 

def valid_url(url: str) -> bool:
    # Check the url to make sure it's valid
    if validators.url(url):
        return True
    else:
        return False
    
def summarize_article(url: str, model: Summarizer) -> str:
    summary = model.summarize_page(url)
    return summary 

def main():
    st.title('Short Summary of News Articles')

    st.header('OpenAI API Key')
    st.markdown('An API Key can be generated [here](https://platform.openai.com/account/api-keys)')
    st.markdown('Your API key file should contain the generated key in plain text.')
    st.info("Your API key will not be saved. This is required to enable the use of the OpenAI API.")
    api_key_file = st.file_uploader('Upload your OpenAI API key file')
    if api_key_file is not None: 
        file_bytes = StringIO(api_key_file.getvalue().decode('utf-8'))
        api_key = file_bytes.read()
        model = Summarizer(api_key=api_key)

        st.subheader('Compute Article Summary')
        url_input = st.text_input('Enter URL of the form: https://www.google.com/')
        if url_input: 
            if valid_url(url_input):
                with st.spinner('Processing article...'):
                    summary = summarize_article(url_input, model)
                    st.markdown('### Summary')
                    st.write(summary)
            else: 
                st.error("Please supply a valid URL")

if __name__ == '__main__':
    main()
