import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello there!",
        page_icon="👋",
    )

    st.write("# Welcome to App Analysis tool 👋")

    st.sidebar.success("Select an app version above.")

    st.markdown(
        """
        This tool provides basic visualizations for the App ratings scrapped from the Appstore. 
    """
    )


if __name__ == "__main__":
    run()
