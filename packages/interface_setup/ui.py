import streamlit as st

def init_ui(preloaded_message="Hello! I'm Sonata, your assistant. How can I help you today?"):
    st.set_page_config(page_title="Sonata v1.0", page_icon="🤖", layout="centered")
    st.markdown('<h1>Supercharge with <span style="color:red;">Sonata</span></h1>', unsafe_allow_html=True)

    st.markdown("### Featured Highlights")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://picsum.photos/300/200")
        st.caption("AI breakthroughs of the week")

    with col2:
        st.image("https://picsum.photos/300/200?2")
        st.caption("Tech market snapshot")

    with col3:
        st.image("https://picsum.photos/300/200?3")
        st.caption("Innovation trends")

    st.markdown("---")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    if not st.session_state["messages"]:
        st.session_state["messages"].append({
            "role": "assistant",
            "content": preloaded_message
        })

    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
