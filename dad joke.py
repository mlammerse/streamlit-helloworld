import streamlit as st
import requests

st.set_page_config(page_title="Dad Joke Generator", page_icon="😂")

st.title("Dad Joke Generator")
st.markdown("Click the button below to get a hilarious dad joke!")

def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["joke"]
    else:
        return "Oops! Failed to fetch a dad joke."

if st.button("Tell me a dad joke", key="joke_button"):
    joke = get_dad_joke()
    st.success(joke)

st.markdown("---")
st.markdown("Created with ❤️ using Streamlit")
