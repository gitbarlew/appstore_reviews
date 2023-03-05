import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

#Define the default welcome page
def run():
    st.set_page_config(
        page_title="Hello there!",
        page_icon="👋",
    )
    #Write welcome top message
    st.write("# Welcome to App Analysis tool 👋")

    #Create a text box in the sidebar asking to select version of the app.
    st.sidebar.success("Select an app version above.")

    #Wirte body of the main page with a welcome message.
    st.markdown(
        """
        This tool provides basic visualizations for the App ratings scrapped from the Appstore. 
    """
    )

#Top-level code environment check
if __name__ == "__main__":
    run()
