import streamlit as st
from pdfChat import main as pdf_chat_app
from sqlConvert import main as text_to_sql
from imageChat import main as image_chat

def main():
    st.title("Gemini Chat Toolkit")

    # Create a menu with three options
    menu_options = ["Text-to-SQL", "Talk To Me", "Chat with PDF"]
    choice = st.sidebar.selectbox("Select Option", menu_options)

    # Depending on the selected option, call the respective function
    if choice == "Text-to-SQL":
        text_to_sql()
    elif choice == "Talk To Me":
        image_chat()
    elif choice == "Chat with PDF":
        pdf_chat_app()

if __name__ == "__main__":
    main()
