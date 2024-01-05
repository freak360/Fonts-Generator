from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()   #Loads the api key from .env file


#Defining a function that gets the response from the Open AI API
def openai_response(textt, numberr):
    llm = OpenAI(openai_api_key = os.getenv("OPENAI_API_KEY"), temperature=0.7)

    template = """
    You are a stylish fonts generator. Your job is to convert the given {textt} into {numberr} number of different stylish fonts and return it.
    """
    prompt = PromptTemplate(template=template, input_variables=['textt', 'numberr'])
    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    response = chain.predict(textt=textt, numberr=numberr)
    #print(response)
    return response


#Defining the main function using streamlit framework to develop the GUI.
def main():
    st.set_page_config(page_title="Stylish Fonts Generator", page_icon="✨")
    st.header("Stylish Fonts Generator")
    text = st.text_input("Input Text Here")
    number = st.number_input("Select the Number of Styles you want")
    submit = st.button("Generate")

    if submit:
        responsee = openai_response(text, number)
        with st.expander("Styles"):
           st.write(responsee)

if __name__ == "__main__":
    main()

