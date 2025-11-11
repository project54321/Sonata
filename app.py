import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.getenv("GITHUB_TOKEN")
)

def chat_with_gpt4o(prompt: str) -> str:
    """Send a prompt to GPT-4o and return its response."""
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=1,
            max_tokens=500
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {e}"


# --------------------------
# Streamlit UI
# --------------------------

st.set_page_config(page_title="Sonata v1.0", page_icon="🤖", layout="centered")

st.title("Supercharge with Sonata")

if "messages" not in st.session_state:
    st.session_state["messages"] = []


for msg in st.session_state["messages"]:
    role = msg["role"]
    content = msg["content"]
    with st.chat_message(role):
        if role == "assistant":
            st.markdown(content)
        else:
            st.write(content)

prompt = st.chat_input("Type a message...")

if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = chat_with_gpt4o(prompt)

    st.session_state["messages"].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
