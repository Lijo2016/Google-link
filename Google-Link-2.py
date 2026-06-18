import streamlit as st
from urllib.parse import quote_plus

def google_link(kereses: str) -> str:
    kodolt = quote_plus(kereses)
    return f"https://www.google.com/search?q={kodolt}"

st.title("Google kereső link generátor")

szoveg = st.text_input("Kérdezz bármit:")

if st.button("Link generálása"):
    if szoveg.strip():
        link = google_link(szoveg)

        st.write("Generált link:")
        st.write(link)

        st.markdown(f"[Megnyitás Google-ben]({link})")

        # Másolható mező
        st.text_input("Másolható link:", value=link)
    else:
        st.warning("Adj meg egy keresést!")