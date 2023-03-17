from transformers import pipeline
import streamlit as st

st.header("Galactica Client| ⚛️")

options = [
    'Citations',
    'LaTeX', 
    'Reasoning', 
    'Free-Form',
    'Question',
    'Documents',
    'Paper',
    'Summarization', 
    'Entity'
]
task = st.selectbox('Task', options)

prompt = st.text_input('Prompt')


if st.button('Submit'):
    if task == 'Citations':
        prompt = f'{prompt} [START_REF]' 
    if task == 'LaTeX':
        prompt = f'{prompt} \\[:' 
    if task == 'Reasoning':
        prompt = f'{prompt} <work>' 
    if task == 'Paper':
        prompt = f'Title: {prompt}' 
    if task == 'Question':
        prompt = f'Question: {prompt}' 
    if task == 'Summarization':
        prompt = f'{prompt} \n\nTLDR:' 
    if task == 'Entity':
        prompt = f'{prompt} \n\nWhat scientific entities are mentioned in the abstract above?\n\n' 

    model = pipeline("text-generation", model="facebook/galactica-6.7b")
    if task == 'Free-Form':
        answer = model(prompt, new_doc=False)
    else:
        answer = model(prompt)
    st.write(answer)