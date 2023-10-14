import streamlit as st
import openai


if __name__ == "__main__":
    st.title("COPAIN")
    openai.api_key = "EMPTY"
    openai.api_base = "http://localhost:8000/v1"

    if "model" not in st.session_state:
        st.session_state["model"] = "Mistral-7B-Instruct-v0.1"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Envoyez un message"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = "...```print('hello world !')```"
            # for response in openai.ChatCompletion.create(
            #     model=st.session_state["openai_model"],
            #     messages=[
            #         {"role": m["role"], "content": m["content"]}
            #         for m in st.session_state.messages
            #     ],
            #     stream=True,
            # ):
            #     full_response += response.choices[0].delta.get("content", "")
            #     message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
