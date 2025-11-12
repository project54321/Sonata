import streamlit as st
from packages.utils.utils import sonata
from packages.interface_setup.ui import init_ui

init_ui()

prompt = st.chat_input("Ask Anything")

if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = sonata(prompt)

    st.session_state["messages"].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
