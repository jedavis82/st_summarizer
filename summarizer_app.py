import streamlit as st 
# from io import StringIO 
import validators 

from summarizer import Summarizer

model = None 

def valid_url(url: str) -> bool:
    # Check the url to make sure it's valid
    if validators.url(url):
        return True
    else:
        return False
    
def summarize_news_article(url: str, num_paragraphs: str, model: Summarizer) -> str:
    summary = model.summarize_from_url(url, num_paragraphs)
    return summary 

def summarize_plain_text(text: str, num_paragraphs: str, model: Summarizer) -> str: 
    summary = model.summarize_from_text(text, num_paragraphs)
    return summary 

def main():
    ## OLD VERSION BEFORE I HAD THE KEY EMBEDDED 
    # st.title('Short Summary of News Articles')

    # st.header('OpenAI API Key')
    # st.markdown('An API Key can be generated [here](https://platform.openai.com/account/api-keys)')
    # st.markdown('Your API key file should contain the generated key in plain text.')
    # st.info("Your API key will not be saved. This is required to enable the use of the OpenAI API.")
    # api_key = st.text_input('Paste your OpenAI API Key')
    # # api_key_file = st.file_uploader('Upload your OpenAI API key file')
    # if api_key != '': 
    # # if api_key_file is not None: 
    #     # file_bytes = StringIO(api_key_file.getvalue().decode('utf-8'))
    #     # api_key = file_bytes.read()
    #     model = Summarizer(api_key=api_key)

    #     st.subheader('Compute Article Summary')
        
    #     url_input = st.text_input(label='Enter URL of the form: https://www.google.com/')
    #     num_paragraphs_radio = st.radio('Number of paragraphs for the summary', ('One', 'Two'))
    #     if url_input != '': 
    #         if valid_url(url_input):
    #             with st.spinner('Processing article...'):
    #                 num_paragraphs = num_paragraphs_radio.lower()
    #                 summary = summarize_article(url_input, num_paragraphs, model)
    #                 st.markdown('### Summary')
    #                 st.write(summary)
    #         else: 
    #             st.error("Please supply a valid URL")

    model = Summarizer()
    with st.sidebar: 
        choose = st.selectbox('Choose a type of document to summarize', ("News Article", "Plain Text"))
    
    num_paragraphs_radio = st.radio('Number of paragraphs for the summary', ('One', 'Two'))
    if choose == 'News Article':
        st.title('Short Summary of a News Article From a Given URL') 
        url_input = st.text_input(label='Enter URL of the form: https://www.google.com')
        if url_input != '': 
            if valid_url(url_input): 
                with st.spinner('Processing article...'): 
                    num_paragraphs = num_paragraphs_radio.lower()
                    summary = summarize_news_article(url_input, num_paragraphs, model)
                    st.markdown('### Summary')
                    st.write(summary)
            else: 
                st.error('Please supply a valid URL')
    elif choose == 'Plain Text': 
        st.title('Short Summary of a Text Snippet')
        text_to_summ = st.text_area(label='Enter the text you want to summarize')
        if text_to_summ != '': 
            with st.spinner('Processing text...'): 
                num_paragraphs = num_paragraphs_radio.lower()
                summary = summarize_plain_text(text_to_summ, num_paragraphs, model)
                st.markdown('### Summary')
                st.write(summary)

if __name__ == '__main__':
    main()
