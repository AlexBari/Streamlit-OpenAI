import streamlit as st
import openai
from PIL import Image
from io import BytesIO
import time

# Setup OpenAI client using your API key
openai.api_key = st.secrets['api_key']

def lookup_for_awnser(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": """
                    Act as a software developer working on Google.
                    Your field of expertise is the software development: you work as developer on multiple languages and libraries such as are React, Python, Java, Javascript, CSS, HTML, NodeJs.
                    The tone of your outputs is always concise and direct, you can search in external pages and developer's forums such as StackOverflow or the official pages from the languages/libraries.
                    Your outputs are always free of plagiarism, original, fluent, and rich in accurate and engaging information, you can answer with code or with ideas.
                """
            },
            {
                "role": "user",
                "content": f"""Take this question: '{question}' and search the response all over the internet using pages as stackoverflow or any page or forum related to software development.
                  In case you detect a language on the question provided you can relay to the official pages and documentation to give an answer.
                  Try to give the nearest or the correct question, always validate your answer on the pages you search.
                  You can provide code in your response if it's needed.
                """
            }
        ],
    )
    highlighted_text = response['choices'][0]['message']['content']
    return highlighted_text

st.title("Wizeline GPTOverflow")
st.text("""Esta aplicación puedes hacer consultas con relación a dudas de promación y sus diferentes rubros,
        te sevirá como un cerebro con conglomerará todos los conocimientos de mulitples páginas.""")

question = st.text_input("Cual es tu duda el día de hoy:")

if st.button("Buscar Respuesta"):
    status = st.status("Buscando respuesta...", expanded=False)
    res = lookup_for_awnser(question)
    status.update(
        label="Se encontró una posible respuesta.", state="complete", expanded=False
    )
    st.subheader('Respuesta: ')
    st.code(res)
    
