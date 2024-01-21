import streamlit as st
from io import StringIO
from vector_search import *
import qa
#from utils import *

st.header("i-Tax Adviser")
url = False
query = False
# options = st.
# options = st.radio(
#    'Choose task',
#    ('Ask a question'))

# if 'Update the Database' in options:
#     url = st.text_input("Enter the url of the document")

# if 'Ask a question' in options:
query = st.text_input("Enter your question")

button = st.button("Submit")

if button and (query):
    with st.spinner("Searching for the answer..."):
        urls,res = find_match(query,3)
        context= "\n\n".join(res)
        st.expander("Context").write(context)
        prompt = qa.create_prompt(context,query)
        # st.success("Answer: "+prompt)
        answer = qa.generate_answer(prompt)
        st.success("Answer: "+answer)
        options = st.radio(
        'Are you satisfied with the response?',
        ('Yes', 'No'))
        
        # if 'No' in options:
        #     correctResponse = st.text_input("Please share the correct response")
        #     button = st.button("Submit Response")

